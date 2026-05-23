import pandas as pd
from pyparsing import col
from sklearn.preprocessing import LabelEncoder

def clean_data(file_path):
    data = pd.read_csv(file_path)

    # 1. Missing values
    for col in data.columns:
        if data[col].dtype == 'object':
            data[col] = data[col].fillna(data[col].mode()[0])
        if data[col].dtype in ['int64', 'float64']:
            data[col] = data[col].fillna(data[col].mean())

    # 2. Remove duplicates (correct way)
    data = data.drop_duplicates()

    # 3. Encode categorical columns
    encoders = {}
    for col in data.columns:
        if data[col].dtype == 'object':
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col])
            encoders[col] = le 
            
            
    print(data.head())
    #

    return data, encoders


