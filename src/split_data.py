from sklearn.model_selection import train_test_split 

def split_data(data): 
    
    Train_data , Test_data = train_test_split(
                                            data ,
                                            test_size=0.3,
                                            train_size=0.7, 
                                            random_state=42
                                            ) 
    
    
    
    
    return Train_data , Test_data