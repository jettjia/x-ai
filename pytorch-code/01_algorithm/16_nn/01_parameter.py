import torch
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.weight = nn.Parameter(torch.randn(5, 5))

    def forward(self, x):
        return torch.mm(x, self.weight)

model = MyModel()
print(list(model.parameters()))

'''
在这个例子中，我们定义了一个名为 MyModel 的类，它继承自 nn.Module。在 __init__ 方法中，
我们定义了一个 nn.Parameter，并将其初始化为一个 5x5 的随机张量。在 forward 方法中，我们使用这个参数对输入数据进行线性变换。
最后，我们创建了一个 MyModel 的实例，并打印了它的参数列表。你会看到，我们定义的 weight 参数已经被自动添加到了参数列表中。
'''
