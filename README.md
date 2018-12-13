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

#### 1. Provide a basic summary of the data set. In the code, the analysis should be done using python, numpy and/or pandas methods rather than hardcoding results manually.

```
Number of training examples = 34799
Number of testing examples = 12630
Image data shape = (32, 32)
Number of classes = 43
```

#### 2. Include an exploratory visualization of the dataset.

每个label对应的内容

![label对应图片](https://raw.githubusercontent.com/Aitical/CarND-Traffic-Sign-Classifier-Project/master/pic/labels1.png)

想同label的多幅图片

![label](https://raw.githubusercontent.com/Aitical/CarND-Traffic-Sign-Classifier-Project/master/pic/pic_one_label.png)

gray image

![灰度图](https://raw.githubusercontent.com/Aitical/CarND-Traffic-Sign-Classifier-Project/master/pic/gray.png)

### Design and Test a Model Architecture


#### 1. Describe what your final model architecture looks like including model type, layers, layer sizes, connectivity, etc.) Consider including a diagram and/or table describing the final model.

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



#### 3. Describe how you trained your model. The discussion can include the type of optimizer, the batch size, number of epochs and any hyperparameters such as learning rate.

```
rate = 0.00005 
EPOCHS = 40
BATCH_SIZE = 20
keep_probability = 0.5
beta = 0.01
```

#### 4. Accuracy

My final model results were:
* validation set accuracy of ?0.948
* test set accuracy of 0.938

The best one is 0.95 on test set.


### Test a Model on New Images

#### 1. Choose five German traffic signs found on the web and provide them in the report. For each image, discuss what quality or qualities might be difficult to classify.

![five](https://raw.githubusercontent.com/Aitical/CarND-Traffic-Sign-Classifier-Project/master/pic/%E9%A2%9D%E5%A4%96%E6%A0%87%E5%BF%97.png)

accuracy is  1.0

top 5 of softmax result.

![top5](https://raw.githubusercontent.com/Aitical/CarND-Traffic-Sign-Classifier-Project/master/pic/top5.png)
