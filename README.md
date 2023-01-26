### TODO

MLP-Mixer搭建测试。

将输出覆盖到原图/输入的mask图上。（修改post_process.py)

处理骨骼片数据格式。

选片标注，用新的数据训练。

early-stopping?

### nb!

需要手动分割训练集和测试集。

数据集中以4:1的比例划分训练集和测试集。

训练集中以3:1的比例划分train:validate。

模型位于archs.py。

训练结束后，需要在测试之前修改相应model的yml文件，将dataset改为对应的测试集dataset名称。

### RESULTS

| Name | Model | Epochs | dataset | Time cost | IoU | Dice |
|-------|:---------:|:------:|------:|------:|------:|------:|
| exp0 | UneXt | 500 | pancreas | 125min | 0.7168 | 0.8326 |
| exp1 | UneXt | 100 | pancreas | 25min | 0.6752 | 0.8019 |
| exp2 | UneXt_S | 500 | pancreas | 98min | 0.7101 | 0.8285 |
| exp3 | Unet | 100 | pancreas | 197min | 0.6603 | 0.7759 |
| exp4 | Unet | 500 | pancreas | 
| exp5 | MLP-Mixer |

### Commands

exp0:python train.py --dataset pancreas --arch UNext --name exp0 --img_ext .png --mask_ext .png --lr 0.0001 --epochs 500 --input_w 512 --input_h 512 --b 8 --input_channels 1

exp1:python train.py --dataset pancreas --arch UNext --name exp1 --img_ext .png --mask_ext .png --lr 0.0001 --epochs 100 --input_w 512 --input_h 512 --b 8 --input_channels 1

exp2:python train.py --dataset pancreas --arch UNext_S --name exp2 --img_ext .png --mask_ext .png --lr 0.0001 --epochs 500 --input_w 512 --input_h 512 --b 8 --input_channels 1

exp3:python train.py --dataset pancreas --arch Unet --name exp3 --img_ext .png --mask_ext .png --lr 0.0001 --epochs 100 --input_w 512 --input_h 512 --b 8 --batch_size 4

exp4:python train.py --dataset pancreas --arch Unet --name exp4 --img_ext .png --mask_ext .png --lr 0.0001 --epochs 500 --input_w 512 --input_h 512 --b 8 --batch_size 4

exp5:python train.py --dataset pancreas --arch MLPMixer --name exp5 --img_ext .png --mask_ext .png --lr 0.0001 --epochs 100 --input_w 512 --input_h 512 --b 8 --input_channels 1

testing:python val.py --name exp0