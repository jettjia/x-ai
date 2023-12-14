import numpy as np
from numpy import linalg as la
#1. SVD分解
A= [[1,1,3,6,1],[5,1,8,4,2],[7,9,2,1,2]]
A=np.array(A)
U,s,VT = la.svd(A)
# 为节省空间，svd输出s只有奇异值的向量
print('奇异值：',s)
# 根据奇异值向量s，生成奇异值矩阵
Sigma = np.zeros(np.shape(A))
Sigma[:len(s),:len(s)] = np.diag(s)

print("左奇异值矩阵：\n",U)
print('奇异值矩阵：\n',Sigma)
print('右奇异矩阵的转置：\n',VT)

#2.SVD重构
B = U.dot(Sigma.dot(VT))
print('重构后的矩阵B：\n', B)

print('原矩阵与重构矩阵是否相同？',np.allclose(A,B))

# 3. SVD矩阵压缩（降维）
for k in range(3,0,-1):  # 3,2,1
    # U的k列，VT的k行
    D = U[:,:k].dot(Sigma[:k,:k].dot(VT[:k,:]))
    print('k=',k,"压缩后的矩阵：\n",np.round(D,1))  # round取整数