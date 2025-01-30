# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle 

load_model = pickle.load(open('C:/Users/victoria/Desktop/ML/project - milling prediction/prediction_model.pkl', 'rb'))



input_data = (0,298.9,309.1,2861,4.6,143,13160.599999999999,10.200000000000045,657.8)

#changing the input to a numpy array
pred_data_array = np.array(input_data)
    
#reshaping array since we are predicting for one instance
reshaped_data = pred_data_array.reshape(1, -1)

prediction = load_model.predict(reshaped_data)
print(prediction)


if np.all(prediction[0]== 0):
    print('No machine failure')
elif np.any(prediction == 1):
    print('Machine failure')