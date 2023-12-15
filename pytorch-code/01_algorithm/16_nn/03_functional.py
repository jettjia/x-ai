import torch
import torch.nn as nn
import torch.nn.functional as F

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc1 = nn.Linear(10, 5)

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)  # 使用 nn.functional 中的 ReLU 激活函数
        return x

# 创建模型实例
model = MyModel()

# 创建一个随机输入张量
input = torch.randn(1, 10)

# 通过模型进行前向传播
output = model(input)

print(output)

'''
在这个例子中，我们定义了一个名为 MyModel 的类，它继承自 nn.Module。
在 __init__ 方法中，我们定义了一个全连接层 fc1。在 forward 方法中，
我们首先使用 fc1 对输入数据进行线性变换，然后使用 torch.nn.functional.relu 函数对结果进行 ReLU 激活。

最后，我们创建了一个 MyModel 的实例，创建了一个随机输入张量，然后使用模型进行了前向传播，并打印了结果。
'''