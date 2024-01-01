# import os
# os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'false'
# from OpenSSL import crypto, SSL

import pandas as pd 
df = pd.read_csv('survey_lung_cancer.csv')
x = df.iloc[:,:-1]
y = df.iloc[:,-1]
from keras.utils import to_categorical
y = to_categorical(y, num_classes=3, dtype='float32')


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test= train_test_split(x, y ,test_size=0.25,stratify=y)

import tensorflow as tf

# Create a simple model
# from keras.models import Sequential
# from keras.layers import Dense, Input
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(128, activation='relu', input_shape=(10,)),
  tf.keras.layers.Dense(64, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])


# model = Sequential()
# model.add(Dense(12, input_shape=(4,), activation='relu'))
# model.add(Dense(8, activation='relu'))
# model.add(Dense(4, activation='relu'))
# model.add(Dense(3, activation='softmax'))

model.compile(optimizer= 'adam',
              loss= 'categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, verbose=1, batch_size=10, validation_split=0.2)
model.evaluate(x_test, y_test)

#sigmoid output from 0,1 so we need to make threshold on output 
# loop on y >.5 =1 , y <.5 =0
#deploy by saving .h