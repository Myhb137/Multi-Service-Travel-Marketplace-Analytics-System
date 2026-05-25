from src.data_loader import load_data
from pandas.api.types import is_numeric_dtype


def clean_data(data):
    

    # 1. Missing values
    for col in data.columns:
        if data[col].dtype == 'object':
            data[col] = data[col].fillna(data[col].mode()[0])
        if data[col].dtype in ['int64', 'float64']:
            data[col] = data[col].fillna(data[col].mean())

    # 2. Remove duplicates
    data = data.drop_duplicates()

    

    return data

    
    