import pickle
import json
import numpy as np

__data_columns = None
__model = None
__companies = None

def get_phone_price(company, ram, battery, display, external_memory, android, inbuilt_memory, fast_charging, t_rear, n_rear, m_rear, t_front, n_front, m_front, width, height, p_speed):
    if __data_columns is None:
        raise RuntimeError("Data columns have not been loaded. Call load_saved() first.")
    company_lower = company.lower()
    if company_lower not in __companies:
        raise ValueError(f"Company '{company}' is not recognized or not in the loaded data columns.")
    x = np.zeros(len(__data_columns))
    x[0] = ram
    x[1] = battery
    x[2] = display
    x[3] = external_memory
    x[4] = android
    x[5] = inbuilt_memory
    x[6] = fast_charging
    x[7] = t_rear
    x[8] = n_rear
    x[9] = m_rear
    x[10] = t_front
    x[11] = n_front
    x[12] = m_front
    x[13] = width
    x[14] = height
    x[15] = p_speed
    try:
        company_index = __data_columns.index(company_lower)
    except ValueError:
        raise ValueError(f"Company '{company}' is not recognized or not in the loaded data columns.")
    x[company_index] = 1
    if __model is not None:
        try:
            prediction = __model.predict([x])[0]
            rounded_prediction = round(prediction, 2)
            return rounded_prediction
        except Exception as e:
            raise RuntimeError(f"Error occurred during prediction: {str(e)}")
    else:
        raise RuntimeError("Model has not been loaded. Call load_saved() first.")

def load_saved():
    global __data_columns
    global __model
    global __companies

    print("Loading saved data...")
    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __companies = __data_columns[16:]
        print(f"Loaded __data_columns with {len(__data_columns)} entries.")

    if __model is None:
        with open('./artifacts/phone_price_model.sav', 'rb') as f:
            __model = pickle.load(f)
            print("Loaded model successfully.")

def get_companies_names():
    return __companies

def get_data_columns():
    return __data_columns

load_saved()
