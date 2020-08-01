# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:56:36 2020

@author: alin2
"""

import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.transform import resize
from tkinter import *

def train_ai():
    # Data Preprocessing
    train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    training_set = train_datagen.flow_from_directory('Training_Data', target_size=(64, 64), batch_size=32, class_mode='binary')
    
    test_datagen = ImageDataGenerator(rescale=1./255)
    test_set = train_datagen.flow_from_directory('Test_Data', target_size=(64, 64), batch_size=32, class_mode='binary')
    
    # Building the CNN
    cnn = Sequential()
    cnn.add(Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[64,64,3]))
    cnn.add(MaxPool2D(pool_size=2, strides=2))
    cnn.add(Conv2D(filters=32, kernel_size=3, activation='relu'))
    cnn.add(MaxPool2D(pool_size=2, strides=2))
    cnn.add(Flatten())
    cnn.add(Dense(128, 'relu'))
    cnn.add(Dense(1, 'sigmoid'))
    
    # Training the CNN
    cnn.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    cnn.fit(x = training_set,steps_per_epoch=250, epochs=25, validation_data=test_set, validation_steps=250)
    
    # Save the CNN
    cnn.save("hotdog_model.h5")
    
def single_prediction(path_txt_box, pred_txt_box):
    path_txt_box.configure(state = "normal")
    sample_path = path_txt_box.get("1.0", "end")
    path_txt_box.configure(state = "disabled")
    
    cnn = load_model("hotdog_model.h5")

    img = imread(sample_path.rstrip())
    img = resize(img,(64,64))
    img = np.expand_dims(img,axis=0)
    
    if(np.max(img)>1):
        img = img/255.0
    
    prediction = cnn.predict_classes(img)
    
    pred_txt_box.configure(state = "normal")
    pred_txt_box.delete("1.0", END)
    pred_txt_box.insert("1.0", "Not HotDog" if prediction[0][0] == 1 else "HotDog")
    pred_txt_box.configure(state = "disabled")
    