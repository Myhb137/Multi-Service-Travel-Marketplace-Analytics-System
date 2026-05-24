from src.cleaning_data import clean_data 
from src.data_loader import load_data  


def hotel_fe(file_path):  

    data = load_data(file_path) 

    data = clean_data(data)
    
    important_feature = data[['arrival_date_year' , 'adults', 'children', 'is_repeated_guest',
                        'total_of_special_requests', 'adr', 'hotel' , 'lead_time' ,
                        'is_canceled' , 'previous_cancellations', 'booking_changes',
                        'required_car_parking_spaces']]

    data = data[important_feature]
    
    return data 

def flight_fe(file_path) : 

    data = load_data(file_path)
    
    data = clean_data(data) 
    
    important_feature = [] 
    
    data = data[important_feature]
    
    return data 

def rating_fe(file_path): 
    
    data = load_data(file_path) 
    
    data = clean_data(data)
    
    important_feature = []
    
    data = data[important_feature]
    
    return data 


dataset_type = input("Enter dataset type (hotel / flight / rating): ")

file_path = input("Enter dataset path: ")

if dataset_type.lower() == "hotel":
    data = hotel_fe(file_path)

elif dataset_type.lower() == "flight":
    data = flight_fe(file_path)

elif dataset_type.lower() == "rating":
    data = rating_fe(file_path)

else:
    print("Unknown dataset type")