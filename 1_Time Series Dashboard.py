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

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Time-Series-Analysis.jpg")

st.image(image.imread(os.path.join(dir_of_interest, "images", "logo.jpeg")))
st.title(":violet[Dashboard - Time Series Data]")

img = image.imread(IMAGE_PATH)
st.image(img)

st.header(":green[Bitcoin Stock Price Dataset]")
df = yf.download('BTC-USD')
st.dataframe(df)

df.reset_index(inplace=True)
df = df[['Date','Adj Close']]
df.columns = ['ds','y']


model = Prophet(daily_seasonality=True)
model.fit(df)

future_dates = model.make_future_dataframe(periods=1000,freq='D')
prediction = model.predict(future_dates)

fig, ax = plt.subplots(figsize=(10, 5))
fig = model.plot(prediction, ax=ax)
ax.set_title('Prophet Forecast')

st.subheader(":orange[Bitcoin Share Price]")
st.pyplot(fig)

st.subheader(":orange[Bitcoin Forecasting]")
fig2 = model.plot_components(prediction)
st.pyplot(fig2)


st.subheader(":orange[Insights]")

st.write("The World witnessed its highest Bitcoin price in 2021, reflecting a period of significant growth and increased value for the cryptocurrency.")

st.write("The peak of Bitcoin's price occurred on a Wednesday, highlighting a particular day of notable market activity and value for the cryptocurrency.")

st.write("The lowest Bitcoin price was observed in 2015, representing a period of relatively lower valuation for the cryptocurrency.")

st.write("A notable dip in Bitcoin's price transpired on a Thursday, signifying a specific day when the cryptocurrency experienced its lowest value.")




