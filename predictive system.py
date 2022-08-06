# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle 

#loading the saved model
loaded_model=pickle.load(open('E:/Diabetes prediction/trained_model.sav','rb'))

input_data=(2,71,70,27,0,28,0.586,22)

#converting the array to anumpy array'
input_data_as_numpy_array=np.asarray(input_data)

# reshape the array as we are only predicting for one instance 
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

#standardize the input data 
#std_data=scaler.transform(input_data_reshaped)
#print(std_data)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]==0):
  print('THE PERSON IS :NON DIABETIC')
else:
  print('THE PERSON IS :DIABETIC')