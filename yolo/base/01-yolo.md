# 安装

```
pip install torch torchvision torchaudio
```



```
# https://github.com/ultralytics/ultralytics/releases

pip install ultralytics
```



> **ai**⼤概的流程（**mode**）
>
> 训练，验证，预测/推理，导出部署
>
> Train，Validation，Predict，Export
>
> 
>
> **ai**⼤概的流程（**mode**）
>
> 训练，验证，预测/推理，导出部署
>
> Train，Validation，Predict，Export

# quick start

```python
from ultralytics import YOLO
yolo = YOLO('yolov8n.pt',task='detect')
result = yolo(source='detect_footage.png',save=True) # .\ultralytics\cfg\default.yaml这个文件里面包含了所有的参数
# source=video.mp4
# source='screen'检测屏幕
# source=0检测摄像头
# save=True就会将检测结果存出来,存到run里
# conf=0.05置信区间
```

结果

```
display(result[0].names)
display(result[0].boxes.cls)
display(result[0].boxes.xywh)
```



# 标注

```
ultralytics-8.1.0 1
|__datasets
    |__icon
        |__images # 存放图片
        	| |__train # 训练集 注意要和labels里的对应
        	| |__val # 验证集 注意要和labels里的对应
        |__labels # 存放标注信息
        	|__train # 注意要和images里的对应
        	|__val # 注意要和images里的对应
```



# 训练

icon.yaml

```yaml
path: icon # dataset root dir
train: images/train
val: images/val
# Classes
names:
  0: geek
  1: trash
```

train.py

```python
from ultralytics import YOLO
# Load model
model = YOLO('yolov8n.pt')
# Train model
model.train(data='icon.yaml',workers=0, epochs=300, batch=16)
```

