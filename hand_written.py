import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense,Flatten
from keras.layers import Dropout
from keras.layers import Conv2D
from keras.layers import MaxPooling2D

mnist =tf.keras.datasets.mnist

(x_train,y_train),(x_test,y_test)= mnist.load_data()



'''

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test =tf.keras.utils.normalize(x_test, axis =1)

#setup the models 

model =Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(128, activation='relu',))
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam',loss ='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(x_train,y_train,  epochs=10, batch_size=128, verbose=1, validation_data =(x_test,y_test))


model.save('handwritten.model')
'''

model =tf. keras.models.load_model('handwritten.model')

loss, accuracy = model.evaluate(x_test, y_test,verbose =0 )
print(loss)
print(accuracy)
