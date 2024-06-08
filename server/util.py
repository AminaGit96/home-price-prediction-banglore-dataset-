import json
import pickle
import numpy as np

__location = None
__data_columns = None
__model = None


def get_location_names():
    return __location

def get_estimated_price(location,area_type,sqft,bath,balcony,bhk):
    try:
        loc_index = np.where(__data_columns==location)[0][0]
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = area_type
    x[1] = sqft
    x[2] = bath
    x[3] = balcony
    x[4] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(float(__model.predict([x])[0]), 2)


def load_saved_artifacts():

    print("load saved artifact ... satrting")
    global __data_columns
    global __location 


    with open('D:/Machine learning projects/House price prediction/server/artifact/columns.json','r') as f:  
       __data_columns = json.load(f)['data_columns']
       __location = __data_columns[5:]

    global __model

    with open('server/artifact/banglore_home_prices_model.pickle','rb') as f:  
        __model = pickle.load(f)

    print("load saved artifact ... done")
    
def get_location_names():
    return __location

def get_data_columns():
    return __data_columns
if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',3,1000, 3,2, 3))
    print(get_estimated_price('1st Phase JP Nagar',2, 1000, 2,1, 2))
    print(get_estimated_price('Kalhalli',0, 1000, 2,3, 2)) # other location
    print(get_estimated_price('Ejipura',1, 1000, 2,0, 2))  # other location
