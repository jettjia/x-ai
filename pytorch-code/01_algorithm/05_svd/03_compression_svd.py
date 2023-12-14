from itertools import count
from PIL import Image
import numpy as np

def img_compress(img,percent):
    U,s,VT=np.linalg.svd(img)
    Sigma = np.zeros(np.shape(img))
    Sigma[:len(s),:len(s)] = np.diag(s)
    # 根据压缩比 取k值

    # 方法1 # k是奇异值数值总和的百分比个数，（奇异值权重）
    count = (int)(sum(s))*percent
    k = -1
    curSum = 0
    while curSum <= count:
        k+=1
        curSum += s[k]

    # 方法2
    # k = (int)(percent*len(s)) # k是奇异值个数的百分比个数

    # 还原后的数据D
    D = U[:,:k].dot(Sigma[:k,:k].dot(VT[:k,:]))
    D[D<0] = 0
    D[D>255] = 255
    return np.rint(D).astype('uint8')

# 图像重建
def rebuild_img(filename,percent):
    img = Image.open(filename,'r')
    a = np.array(img)
    R0 = a[:,:,0]
    G0 = a[:,:,1]
    B0 = a[:,:,2]
    R = img_compress(R0,percent)
    G = img_compress(G0,percent)
    B = img_compress(B0,percent)
    re_img = np.stack((R,G,B),2)
    # 保存图片
    newfile = filename+str(percent*100)+'.jpg'
    Image.fromarray(re_img).save(newfile)
    img = Image.open(newfile)
    img.show()


rebuild_img('test.jpg',0.8)