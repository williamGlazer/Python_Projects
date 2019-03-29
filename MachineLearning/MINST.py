#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tensorflow as tf
import tensorflow.keras as keras

#load MINST
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

#Convert to one-hot encoding
# [1, 4, ...] -> [ [0,1,0,...], [0,0,0,0,1 ...] ... ]
y_train = keras.utils.to_categorical(y_train)
y_test  = keras.utils.to_categorical(y_test)


#Scale training to [0..1]
# [0..255] -> [0..1]
X_train = X_train / 255.
X_test  = X_test  / 255.




#Model
shallow_model = keras.models.Sequential([
        keras.layers.Flatten(),                          #28x28 -> 784x1
        keras.layers.Dense(10, activation=tf.nn.softmax) #784x1 -> 10x1      
])


# Define opt & loss
shallow_model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

#Train
shallow_model.fit(X_train, y_train, epochs=5)

#compute accuracy on test set
loss, accuracy = shallow_model.evaluate(X_test, y_test)
print('{:.4}'.format(accuracy))





#Model
deep_model = keras.models.Sequential([
        keras.layers.Flatten(),  
        keras.layers.Dense(512, activation=tf.nn.relu),
        keras.layers.Dense(10, activation=tf.nn.softmax)  
])


# Define opt & loss
deep_model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

#Train
deep_model.fit(X_train, y_train, epochs=5)

#compute accuracy on test set
loss, accuracy = deep_model.evaluate(X_test, y_test)
print('{:.4}'.format(accuracy))