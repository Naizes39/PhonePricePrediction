![alt text](image.png)

# Phone Price Prediction Website

This project utilizes the Kaggle Mobile Phone Price Prediction dataset by Dewang Moghe to predict the prices of mobile phones. Initially, the data was cleaned and preprocessed using Python in a Jupyter Notebook (`phone_price_prediction.ipynb`). A RandomForestRegressor model was trained on the cleaned data, achieving a score of 0.88.

The trained model and necessary columns for data preprocessing were saved. Subsequently, a web application was developed using FastAPI to provide a user-friendly interface for predicting phone prices based on user inputs.

## Project Structure

The project consists of the following components:

- **`phone_price_prediction.ipynb`**: Jupyter Notebook for data cleaning, preprocessing, and model training.
- **`phone_price_model.sav`**: File containing the trained RandomForestRegressor model.
- **`columns.csv`**: CSV file containing the list of columns used in data preprocessing.
- **`app` directory**: Contains the FastAPI web application files.
- **`main.py`**: FastAPI main application file.
- **`templates` directory**: HTML templates for the web interface.
- **`static` directory**: Static files (e.g., CSS, JavaScript) for the web interface.

## Installation

To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Naizes39/PhonePricePrediction.git
   cd phone_prediction/server

2. Install the required Python dependencies from server directory:
    pip install -r requirements.txt

3. Run the FastAPI application:
    uvicorn app.main:app --reload

4. Open a web browser and go to http://127.0.0.1:8000 to access the application.

## Usage

1. Enter the required details in the form provided (e.g., phone specifications).

2. Click on the "Predict" button to obtain the predicted price of the phone.

## Credits

Dewang Moghe for providing the Kaggle Mobile Phone Price Prediction dataset.
https://www.kaggle.com/datasets/dewangmoghe/mobile-phone-price-prediction
