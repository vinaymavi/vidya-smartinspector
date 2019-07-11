#https://medium.com/nybles/create-your-first-image-recognition-classifier-using-cnn-keras-and-tensorflow-backend-6eaab98d14dd
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

#https://www.analyticsindiamag.com/learn-image-classification-using-cnn-in-keras-with-code/
#Initialising the CNN
model = Sequential()
#Convolutional Layer
model.add(Convolution2D(filters = 32, kernel_size = (3, 3),input_shape = (64, 64, 3),activation = 'relu'))
#Pooling Layer
model.add(MaxPooling2D(pool_size = (2, 2)))
#Adding a second layer of Convolution and Pooling
model.add(Convolution2D(32, 3, 3, activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
#Flattening Layer
model.add(Flatten())
#Full-Connection Layer
model.add(Dense(units = 128, activation = 'relu'))
#Adding the Output Layer
#model.add(Dense(units = 1, activation = 'sigmoid'))
model.add(Dense(5, activation = 'softmax'))
#Compiling the CNN
model.compile(optimizer = 'adam',loss = 'categorical_crossentropy',metrics = ['accuracy'])
#Compiling the CNN
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255,shear_range = 0.1,zoom_range = 0.2,horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale=1. / 255)
#Fitting images to the CNN

training_set = train_datagen.flow_from_directory('./data/cnn/training_set', target_size = (64, 64),batch_size = 32,class_mode = 'categorical')
test_set = test_datagen.flow_from_directory('./data/cnn/test_set',target_size = (64, 64),batch_size = 32,class_mode = 'categorical')
#Training and Evaluating the model epoc 15

#nb_train_samples = 200  #total
#nb_validation_samples = 10  # total
#epochs = 6
#batch_size = 10

#2000 , 6 , 200
model.fit_generator(training_set,samples_per_epoch = 8000, nb_epoch = 1,validation_data = test_set,nb_val_samples = 800)

model.save('./genrated_models/model_3.h5')
print("Model genrated successfully.")
from keras.models import load_model
# load model
model = load_model("./genrated_models/model_3.h5")

import numpy
import numpy as np
filename1 = "./data/cnn/test_set/Normal_Condition/1413919861994.jpg"
from keras.preprocessing import image
test_image = image.load_img(filename1, target_size =(64,64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
test_image /= 255.
print("Image prediction start")
result = model.predict(test_image)
print(model.predict_classes(test_image))
print(result)
print("Image prediction end")