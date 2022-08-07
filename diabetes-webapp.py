# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 01:27:50 2022

@author: Lenovo
"""

import numpy as np
import pickle 
import streamlit as st
#loading the saved model
loaded_model=pickle.load(open('trained_model.sav','rb'))
#creating a function for prediciting

def diabetes_prediction(input_data):


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
      return 'THE PERSON IS :NON DIABETIC'
    else:
      return 'THE PERSON IS :DIABETIC'
  
    

#giving a title
st.title('DIABETES PREDICTION WEBAPP')
    # getting the input data from user
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
Pregnancies=st.text_input('Number of Pregnancies')
Glucose=st.text_input('Glucose Levels')
BloodPressure=st.text_input('Blood pressure value')
SkinThickness=st.text_input('SkinThickness value')
Insulin=st.text_input('Insulin Levels')
BMI=st.text_input('BMI value')
DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction Levels')
Age=st.text_input('age of the person')
    
    #code for prediciton
diagnosis=''
    
    #creating a button  for prediction 
if(st.button('Diabetes test result')):
     diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    
st.success(diagnosis)
      



    
    
    
    
    
    
    
    
    
    
    
      



    
    
    
    
    
    
    
    
    
    
    
    
