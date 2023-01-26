### TODO

MLP-Mixer����ԡ�

��������ǵ�ԭͼ/�����maskͼ�ϡ����޸�post_process.py)

�������Ƭ���ݸ�ʽ��

ѡƬ��ע�����µ�����ѵ����

early-stopping?

### nb!

��Ҫ�ֶ��ָ�ѵ�����Ͳ��Լ���

���ݼ�����4:1�ı�������ѵ�����Ͳ��Լ���

ѵ��������3:1�ı�������train:validate��

ģ��λ��archs.py��

ѵ����������Ҫ�ڲ���֮ǰ�޸���Ӧmodel��yml�ļ�����dataset��Ϊ��Ӧ�Ĳ��Լ�dataset���ơ�

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