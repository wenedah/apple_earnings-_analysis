# Apple Earnings Announcements and Stock Price Analysis


## Project Description
This project analyzes 4.7 (approx 5 years) of Apple Inc. (AAPL) quarterly earnings announcements using Python and PostgreSQL, it examines the relationship between earnings per share (EPS) and revenue surprises and short term stock price performance across 20 earnings announcements.

Developed as a proof of concept for a financial new publication, seeking to produce data driven articles on market reaction to company news,  whether Apple's earnings results relative to analyst expectations consistently correspond with stronger or weaker stock returns after an announcement.


## Business Context and Problem

A financial news publication wants to create a new content section featuring data driven articles on market reactions to company news. This project serves as a proof of concept, demonstrating how the relationship between company earnings announcements and stock price performance can be investigated using historical financial data.

Quarterly earnings announcements provide investors and financial analysts with important information about a company’s financial performance. Two commonly evaluated metrics are earnings per share (EPS) and revenue, which are compared against analysts estimates to determine whether a company has exceeded or fallen short of expectations.

However, reporting better than expected financial results does not necessarily explain how the stock market will react. A company’s share price may rise or fall following an earnings announcement, even when its reported results exceed expectations.

The publication therefore needs an evidence based approach to compare earnings surprises with subsequent stock returns and determine whether stronger than expected financial results consistently coincide with stronger short term stock performance.

## Project Objective

Analyze 20 Apple earnings announcements to examine the relationship between EPS and revenue surprises and subsequent stock returns over one, three, and five trading sessions.

## Business Question

Do larger positive earnings surprises consistently coincide/ lead to stronger short-term stock returns following Apple's quarterly earnings announcements?


## Data Sources and Data Structure

### Data Sources

The project uses historical financial data obtained from
[Financial Modeling Prep (FMP)](https://site.financialmodelingprep.com/).

**1. Earnings Data**

- Source: [FMP Earnings API](YOUR_FMP_SOURCE_LINK)
- Dataset: [Download Apple Earnings Dataset](Data/appl_earnings_report.csv)

**2. Historical Stock Price Data**

- Source: [FMP Historical Price API](YOUR_FMP_SOURCE_LINK)
- Dataset: [Download Historical Stock Price Dataset](Data/appl_historical_prices.csv)


## Analytical Approach

The analysis was carried out using Python for data extraction and PostgreSQL for data validation, transformation, and analysis.

| Stage | Description | Supporting Files |
|---|---|---|
| Data Extraction | Retrieved earnings announcements and historical stock prices from the Financial Modeling Prep API. | [Python Extraction Script](scripts/Python_Extraction_Script.py) |
| Data Preparation and Validation | Prepared the datasets, checked for missing values, duplicates and inconsistencies, and investigated identified anomalies. | [Data Preparation / Validation Queries](ADD_SQL_SCRIPT_LINK) |
| Earnings Surprise Analysis | Calculated EPS and revenue surprises by comparing actual results against analyst estimates. | [Earnings Surprise SQL Queries](ADD_SQL_SCRIPT_LINK) |
| Stock Performance Analysis | Calculated Apple's stock returns over one, three, and five trading sessions following earnings announcements. | [Stock Performance SQL Queries](ADD_SQL_SCRIPT_LINK) |
| Combined Analysis | Joined the earnings and historical price datasets to examine the relationship between earnings surprises and subsequent stock returns across 20 announcements. | [Complete SQL Analysis](ADD_COMPLETE_SQL_SCRIPT_LINK) |

### Earnings Surprise Calculation

The percentage surprise for each financial metric was calculated as:

**EPS Surprise (%)**

\[
\frac{\text{Actual EPS}-\text{Estimated EPS}}{|\text{Estimated EPS}|}\times100
\]

**Revenue Surprise (%)**

\[
\frac{\text{Actual Revenue}-\text{Estimated Revenue}}{|\text{Estimated Revenue}|}\times100
\]

Positive values indicate results above estimates, while negative values indicate results below estimates.

### Stock Return Calculation

Post-announcement stock performance was measured using:

\[
\text{Return (\%)}=
\frac{\text{Ending Price}-\text{Starting Price}}
{\text{Starting Price}}\times100
\]

Returns were examined over one, three, and five trading sessions following each announcement. See the SQL scripts for the precise price references and trading-session logic.

