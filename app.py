
import streamlit as st
import pandas as pd
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder,StandardScaler
from sklearn.ensemble import RandomForestRegressor
import pickle

st.title("Swiggy Delivery Time Prediction")
df = pd.read_csv(r'swiggy_cleaned.csv')
df.dropna(inplace=True)

age = st.number_input("Enter the Rider Age :",min_value=20,max_value=50)
ratings = st.number_input("Enter the Rider Rating",min_value=0,max_value=5)
weather = st.selectbox('ENter the weather condition',df['weather'].unique())
traffic = st.selectbox('ENter the traffic condition',df['traffic'].unique())
vehicle_condition = st.selectbox('ENter the Vehicle condition',df['vehicle_condition'].unique())
type_of_vehicle = st.selectbox('ENter the Type of vehicle',df[ 'type_of_vehicle'].unique())
multiple_deliveries = st.selectbox('ENter the multiple_deliveries',df['multiple_deliveries'].unique())
festival = st.selectbox('Is it festival',df['festival'].unique())
city_name  = st.selectbox('Enter city_name ',df['city_name'].unique())
is_weekend = st.selectbox('Is it weekend',df['is_weekend'].unique())
pickup_time_minutes = st.number_input("ENter the Pick up Time")
order_time_hour = st.number_input("Enter the Order hour",min_value=0,max_value=24)
distance = st.number_input("Enter the Distance between restaurent and delivery location")

X = df.drop(columns='time_taken')


with open("Deployment.pkl", "rb") as file:
    model = pickle.load(file)

if st.button("Predict"):
    # Create a dictionary with user inputs
    input_data = {
        'age': [age],
        'ratings': [ratings],
        'weather': [weather],
        'traffic': [traffic],
        'vehicle_condition': [vehicle_condition],
        'type_of_vehicle': [type_of_vehicle],
        'multiple_deliveries': [multiple_deliveries],
        'festival': [festival],
        'city_name': [city_name],
        'is_weekend': [is_weekend],
        'pickup_time_minutes': [pickup_time_minutes],
        'order_time_hour': [order_time_hour],
        'distance': [distance]
    }
    
    # Convert to DataFrame
    input_df = pd.DataFrame(input_data)

    # Make prediction
    time = model.predict(input_df)[0]
    st.write(f"The Delivery Time is {time:.2f} mins")
    st.snow()
