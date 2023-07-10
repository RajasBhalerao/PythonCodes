#This will be the step 4 and 5 of the project

import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
from tensorflow.keras.preprocessing import image
import itertools

# we will use the sequential model and convolutional layer for images as they are 2D in nature
trainmod = Sequential()
# For videos we can use Conv3D
trainmod.add(Conv2D(32,(3,3), input_shape=(64,64,3), activation='relu'))
trainmod.add(MaxPooling2D(pool_size=(2,2))) # downsample the images
trainmod.add(Flatten())
trainmod.add(Dense(units=128, activation='relu'))
trainmod.add(Dense(units=1, activation='sigmoid'))
trainmod.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(input("Enter path to training dataset") ,
                                                 target_size=(64,64),
                                                 batch_size=32,
                                                 class_mode='binary')

test_set = train_datagen.flow_from_directory(input("Enter path to testing dataset") ,
                                                 target_size=(64,64),
                                                 batch_size=32,
                                                 class_mode='binary')

trainmod.fit(training_set,
                       steps_per_epoch=int(144/32),
                       epochs=25,
                       validation_data=test_set,
                       validation_steps=int(51/32))

repeat_training_set = itertools.cycle(training_set)
repeat_test_set = itertools.cycle(test_set)


test_loss, test_accuracy = trainmod.evaluate(test_set, steps=46)
        

test_image = image.load_img(input("Enter the path to the indiviual test image"), target_size=(64,64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result=trainmod.predict(test_image)
training_set.class_indices

#Currently just checking for 2 classes, Human or not human.
# We will build more classes as we move ahead.
if result[0][0] == 1:
    predict = 'Human'
else:
    predict = 'Other'
print(predict)
