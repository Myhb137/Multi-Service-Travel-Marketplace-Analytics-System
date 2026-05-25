from src.cleaning_data import clean_data 
from src.data_loader import load_data  


def hotel_fe(data):      
    important_feature = ['arrival_date_year' , 'adults', 'children', 'is_repeated_guest',
                        'total_of_special_requests', 'adr', 'hotel' , 'lead_time' ,
                        'is_canceled' , 'previous_cancellations', 'booking_changes',
                        'required_car_parking_spaces']

    
    
    return data[important_feature] 

def flight_fe(data) : 
    
    important_feature = [] 
    
    
    return data[important_feature] 

def rating_fe(data): 
    
    
    important_feature = []
    
    
    return data[important_feature] 


