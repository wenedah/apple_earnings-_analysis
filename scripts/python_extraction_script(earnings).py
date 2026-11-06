
import requests
import pandas as pd

API_KEY = "YOUR_API_KEY"

url = "https://financialmodelingprep.com/stable/earnings"

params = {
    "symbol": "AAPL",
    "apikey": API_KEY
}

# Send API request
response = requests.get(url, params=params, timeout=30)

# Check whether the request was successful
response.raise_for_status()

# Convert API response to JSON
data = response.json()

# Convert JSON data into a DataFrame
df = pd.DataFrame(data)

# Rename columns for consistency
df = df.rename(columns={
    "date": "earnings_date",
    "epsActual": "eps_actual",
    "epsEstimated": "eps_estimated",
    "revenueActual": "revenue_actual",
    "revenueEstimated": "revenue_estimated",
    "lastUpdated": "last_updated"
})

# Inspect the extracted data
print(df.head())
print("Dataset shape:", df.shape)

# Export data to CSV
df.to_csv("aapl_earnings.csv", index=False)

print("Earnings dataset saved successfully!")
