import numpy as np
#Save the Model file
import pickle
filename = "./genrated_models/model_3.h5"
from keras.models import load_model

#load the model File and predict
#Prediction
# load the model from disk
model = load_model(filename)

import numpy
import numpy as np
filename1 = "./data/cnn/test_set/Normal_Condition/1413919861994.jpg"
from keras.preprocessing import image

def CNN_predict(filename) :
    test_image = image.load_img(filename1, target_size =(64,64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    test_image /= 255.
    result = []
    result = model.predict(test_image)
    label = model.predict_classes(test_image)
    print(result[0])
    print(label)
    index =0
    resulttext = ["Corrosion","Damaged_Coating_Images","Joint_Failure_Images","Leak_Images","Normal_Condition"]
    return(resulttext[label[0]])


result = CNN_predict(filename)
print(result)