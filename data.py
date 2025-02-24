import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Crypto Access")

# Fetching data from the API
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10, "page": 1, "sparkline": False}
response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data)

# Displaying price table
st.subheader("📌 Current Cryptocurrency Prices")
st.dataframe(df[['name', 'symbol', 'current_price', 'market_cap', 'price_change_percentage_24h']])

# Creating percentage variation chart
st.subheader("📉 Percentage Change in the Last 24h")
fig, ax = plt.subplots()
ax.bar(df['symbol'], df['price_change_percentage_24h'], color=['green' if x > 0 else 'red' for x in df['price_change_percentage_24h']])
ax.set_ylabel('Change %')
st.pyplot(fig)
