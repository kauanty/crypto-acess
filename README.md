## 🚀 **Crypto Access - Cryptocurrency Monitoring**

This is an interactive dashboard project that allows tracking prices, market volume, and variations of major cryptocurrencies in real time. The data is obtained from the CoinGecko API and presented in a visual and intuitive way.

🔹 Technologies used: Python, Pandas, Matplotlib, Streamlit, MySQL  

🔹 Data sources: CoinGecko API  
<hr>

### ⚙️ Features:

✅ List of major cryptocurrencies with real-time updated prices  

✅ Price variation chart for the last 24 hours  

✅ Interactive table with information such as Market Cap, Volume, and Percentage Change  

✅ Custom filters (search for specific currency, convert values, etc.)  

✅ Price history storage in a database  
<br><hr>

### 📦 Installation and Execution  

To run the project locally, follow these steps:

1️⃣ Clone the repository:

```bash
git clone https://github.com/kauanty/crypto-dashboard.git
cd crypto-dashboard
```

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Run the dashboard:

```bash
streamlit run app.py
```

<br><hr>

### 📊 Usage Example  

### API Endpoints Used  

| Endpoint | Description |  
| --- | --- |  
| /coins/markets | List of cryptocurrencies sorted by market cap |  
| /coins/{id}/market_chart | Price history of a cryptocurrency |  
| /simple/price | Current price of a cryptocurrency in different currencies |  