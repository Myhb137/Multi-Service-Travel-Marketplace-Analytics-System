from sklearn.preprocessing import LabelEncoder 
import pandas as pd 

def encouder(data): 
    
    
    data = data.copy() 
    
    enc_data = data.select_dtypes(include=["object"]).columns 
    
    
    for i in enc_data:
        le = LabelEncoder()
        data[i] = le.fit_transform(data[i].astype(str))
        
    return data