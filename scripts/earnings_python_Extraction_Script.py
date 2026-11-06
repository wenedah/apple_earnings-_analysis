
import requests
import pandas as pd

# API configuration
API_KEY = "MY_API_KEY"

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


-- # EARNINGS SCRIPT

import requests
import pandas as pd

API_KEY = "YOUR_API_KEY"

url = "https://financialmodelingprep.com/stable/earnings"

params = {
    "symbol": "AAPL",
    "apikey": API_KEY
}

# Send request to the API
response = requests.get(url, params=params)

print(response.status_code)

# Check whether the request was successful
response.raise_for_status()

# Convert API response to JSON
data = response.json()

# Convert JSON data into a Pandas DataFrame
df = pd.DataFrame(data)

# Inspect the data
print(df.head())
print(df.shape)
print(df.columns)

# Rename columns to snake_case
df = df.rename(columns={
    "epsActual": "eps_actual",
    "epsEstimated": "eps_estimated",
    "revenueActual": "revenue_actual",
    "revenueEstimated": "revenue_estimated",
    "fiscalDateEnding": "fiscal_date_ending",
    "updatedFromDate": "updated_from_date"
})

# Export data to CSV
df.to_csv("AAPL_earnings.csv", index=False)

print("Earnings data saved successfully!")
