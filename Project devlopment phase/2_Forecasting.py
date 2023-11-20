import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import image
import streamlit as st

import yfinance as yf
from prophet import Prophet

import os


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")


st.image(image.imread(os.path.join(dir_of_interest, "images", "logo2.png")))


st.title(":blue[Prediction - Time Series Data]")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "prophet.jpg")

img = image.imread(IMAGE_PATH)
st.image(img)

df = yf.download('BTC-USD')
st.subheader(":orange[Bitcoin Share Price]")
st.dataframe(df)

df.reset_index(inplace=True)
df = df[['Date','Adj Close']]
df.columns = ['ds','y']


model = Prophet(daily_seasonality=True)
model.fit(df)

future_dates = model.make_future_dataframe(periods=1000,freq='D')
prediction = model.predict(future_dates)
prediction = prediction[['ds','yhat']]
st.subheader(":orange[Bitcoin Share Price Forecasting]")
st.dataframe(prediction)


st.subheader(":orange[Predicting Bitcoin Prices]")

# Create a date input field in Streamlit
selected_date = st.date_input(":blue[Enter a date between 2015 and 2026]")

# Convert selected_date to string format
selected_date_str = selected_date.strftime('%Y-%m-%d')

# Check if the selected_date exists in the prediction data
if selected_date_str in prediction['ds'].astype(str).values:
    # Retrieve the predicted price for the selected_date
    price_prediction = prediction.loc[prediction['ds'].astype(str) == selected_date_str, 'yhat'].values[0]
    st.subheader(f"The predicted price of Bitcoin on {selected_date_str} is: :red[{price_prediction} $]")

else:
    st.write("Invalid date. Please enter a valid date.")


IMAGE_PATH2 = os.path.join(dir_of_interest, "images", "bitcoin.jpeg")
img2 = image.imread(IMAGE_PATH2)
st.image(img2)

def main():
    st.subheader(":red[Factors Contributing to Decreasing Bitcoin Price]")

    bullet_points = [
        "Market corrections following periods of rapid price increases.",
        "Negative global market trends impacting Bitcoin's value",
        "Uncertainty and negative sentiment due to regulatory developments.",
        "Investor selling pressure influenced by risk perception.",
        "Potential market manipulation by large-scale traders affecting Bitcoin's price."
    ]

    for point in bullet_points:
        st.write("- " + point)


if __name__ == '__main__':
    main()