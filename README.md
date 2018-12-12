# **Traffic Sign Recognition** 

**Build a Traffic Sign Recognition Project**

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report

### Data Set Summary & Exploration

#### 1. 数据集信息

```
Number of training examples = 34799
Number of testing examples = 12630
Image data shape = (32, 32)
Number of classes = 43
```

#### 2. 数据集可视化

每个label对应的内容

![label对应图片](https://raw.githubusercontent.com/Aitical/CarND-Traffic-Sign-Classifier-Project/master/pic/labels1.png)

想同label的多幅图片

![label](https://raw.githubusercontent.com/Aitical/CarND-Traffic-Sign-Classifier-Project/master/pic/pic_one_label.png)

转化为灰度图

![灰度图](https://raw.githubusercontent.com/Aitical/CarND-Traffic-Sign-Classifier-Project/master/pic/gray.png)

### Design and Test a Model Architecture

#### 1. 选择模型

​	测试了LeNet和NVIDIA 的网络结构


#### 2. 模型结构 

My final model consisted of the following layers:

| Layer         		|     Description	        					|
|:---------------------:|:---------------------------------------------:|
| Input         		| 32x32x3 RGB image   							|
| Convolution 3x3     	| 1x1 stride, same padding, outputs 30x30x64 |
| RELU					|												|
| Dropout	| 0.5 |
| Max pooling	      	| 2x2 stride,  outputs 15x15x64 |
| Convolution 3x3	    | 1x1 stride, same padding, outputs 13x13x96 |
| RELU	|  |
| Max pooling	| 2x2 stride,  outputs 7x7x96 |
| Dropout	| 0.5 |
| Convolution 3x3	| 1x1 stride, same padding, outputs 5x5x128 |
| RELU	|  |
| Max pooling	| 2x2 stride,  outputs 3x3x128 |
| Dropout	| 0.5 |
| Fully connected		| input 9x128,output 9x64 |
| Fully connected	| input 9x64,output 9x32 |
| Fully connected | input 9x32,output 43 |
| Softmax |												|



#### 3. 训练参数

```
rate = 0.00005 
EPOCHS = 40
BATCH_SIZE = 20
keep_probability = 0.5
beta = 0.01
```

#### 4. 准确率

My final model results were:
* validation set accuracy of ?0.948
* test set accuracy of 0.938

最好一次测试集是0.954已保存在model/下


### Test a Model on New Images

找了额外5张交通标志

![five](https://raw.githubusercontent.com/Aitical/CarND-Traffic-Sign-Classifier-Project/master/pic/%E9%A2%9D%E5%A4%96%E6%A0%87%E5%BF%97.png)

测试准确率是 1.0

每张图片预测top5展示

![top5](https://raw.githubusercontent.com/Aitical/CarND-Traffic-Sign-Classifier-Project/master/pic/top5.png)