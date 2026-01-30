# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:08:17 2024

@author: victoria
"""

import numpy as np
import pickle
import streamlit as st


#loading the data
with open("prediction_model.pkl", "rb") as f:
    load_model = pickle.load(f)





#creating a function for prediction

def milling_machine_prediction(Air_temperature, Process_temperature, Rotational_speed, Torque, Tool_Wear, Type):


    Power = Rotational_speed * Torque
    Temperature_difference = Process_temperature - Air_temperature
    Strain = Torque * Tool_Wear

    #changing the input to a numpy array
    pred_data_array = np.array([Air_temperature, Process_temperature, Rotational_speed, Torque, Tool_Wear, Type, Power, Temperature_difference, Strain])
    
    #reshaping array since we are predicting for one instance
    reshaped_data = pred_data_array.reshape(1, -1)

    prediction = load_model.predict(reshaped_data)
    print(prediction)
    
    
    failure_type =''
    if prediction[0,1]==1:
        failure_type='TWF'
    
    elif prediction[0,2]==1:
        failure_type='HDF'
    
    elif prediction[0,3]==1:
        failure_type='Power Failure (PWF)'
    
    elif prediction[0,4]==1:
        failure_type='OSF'
    
    elif prediction[0,5]==1:
        failure_type='RNF'
    
    else:
        failure_type='NO FAILURE'



    if failure_type != 'NO FAILURE':
        out = f'There is a machine failure, Most likely  {failure_type}'
    else:
        out = 'There is no failure'
    print(out)
    return out





def mapping(level):
    
    if level == 'Low': 
        out = 0
    elif level == 'Medium':
        out = 1 
    elif level == 'High':
        out = 2
    else:
        out = None    
    return float(out)
    
    
    
    
def main():
    
    
   
    #giving the webpage a title
    st.title('Failure Prediction Web App')
    
    st.write("""
    This application predicts potential failures in milling machines by analyzing various input parameters.
    
    
    """)
    
    col1,col2 = st.columns(2)
    
    #gettig the input data from the user
    with col1:
        Air_temperature = st.slider('Air temperature', min_value=100, max_value=350)
        Process_temperature = st.slider('Process temperature', min_value=100, max_value=350)
    with col2:
        Type = st.radio('Quality Type', ['Low', 'Medium', 'High'])
    
    Rotational_speed = st.number_input('Rotational speed')
    Torque = st.number_input('Torque')
    Tool_Wear = st.number_input('Tool Wear')
    
    # Map the Quality Type to its corresponding value
    Quality_Type_value = mapping(Type)
    
    #code for the prediction
    output = ''
    
    #submission button
    if st.button('Prediction Result'):
        output = milling_machine_prediction(Air_temperature, Process_temperature, 
                                            Rotational_speed, Torque, Tool_Wear, Quality_Type_value)
        
        
    st.success(output)
    
    
    
if __name__ == '__main__':
    main()
    


    




