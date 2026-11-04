
import requests
import pandas as pd

# API configuration
API_KEY = "YOUR_API_KEY"

url = "https://financialmodelingprep.com/stable/historical-price-eod/full"

params = {
    "symbol": "AAPL",
    "apikey": API_KEY
}

# Extract historical stock price data
response = requests.get(url, params=params)

print(response.status_code)

data = response.json()

# Convert API response into DataFrame
df = pd.DataFrame(data)

# Inspect extracted data
print(df.head())
print(df.shape)

# Standardize column naming
df = df.rename(columns={
    "changePercent": "change_percent"
})

# Export dataset to CSV
df.to_csv("AAPL_historical_prices.csv", index=False)

print("CSV file saved successfully!")
