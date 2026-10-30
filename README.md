# apple_earnings_analysis

# project description
This project analyzes 4.7 (approx 5 years) of Apple Inc. (AAPL) quarterly earnings announcements using Python and PostgreSQL, it examines the relationship between earnings per share (EPS) and revenue surprises and short-term stock-price performance across 20 earnings announcements.

Developed as a proof of concept for a financial new publication, seeking to produce data driven articles on market reaction to company news,  whether Apple's earnings results relative to analyst expectations consistently correspond with stronger or weaker stock returns after an announcement.


## Project Background

Quarterly earnings announcements provide investors and analysts with important information about a company's financial performance. These reports include metrics such as revenue and earnings per share (EPS), which are commonly compared with analysts' estimates to determine whether a company performed better or worse than expected.

However, beating earnings expectations does not necessarily mean a company's stock price will increase. Stock-price movements may also reflect investor expectations, future growth prospects, company guidance, and broader market conditions.

For a financial news publication, understanding this relationship can support more evidence-based reporting on how financial results relate to market reactions. This project uses Apple's earnings announcements and historical stock-price data to investigate this relationship.

## Business Problem

A financial news publication wants to produce evidence based articles explaining how Apple's stock price behaves following quarterly earnings announcements. Reporting whether Apple beats or misses analyst expectations alone does not explain how the market responds to those results.

The publication therefore needs an analytical approach to compare earnings surprises with subsequent stock returns and determine whether stronger-than-expected financial results generally coincide with stronger short-term stock performance.

## Project Objective

Analyze 20 Apple earnings announcements to examine the relationship between EPS and revenue surprises and subsequent stock returns over one, three, and five trading sessions.

## Business Question

Do larger positive earnings surprises consistently coincide with stronger short-term stock returns following Apple's quarterly earnings announcements?
 Data Sources and Data Structure

Data Source

The project uses historical financial data obtained from the Financial Modeling Prep (FMP) API.

Two datasets were extracted for the analysis:

1. Earnings Data

Contains Apple's quarterly earnings announcements, including actual and estimated EPS and revenue figures.

Original source: Financial Modeling Prep Earnings Data

Project dataset: View Earnings Dataset

2. Historical Stock Price Data

Contains Apple's daily historical stock-price information, used to measure price movements following earnings announcements.

Original source: Financial Modeling Prep Historical Price Data

Project dataset: View Historical Stock Price Dataset

Database Structure

The extracted datasets were imported into PostgreSQL and organized into two tables:

Table

Description

earnings

Stores quarterly earnings announcement dates, actual EPS, estimated EPS, actual revenue, and estimated revenue.

daily_stock_prices

Stores daily historical stock-price information, including opening and closing prices and other market data.

The two tables were connected using the stock ticker symbol and relevant dates to compare earnings announcements with subsequent trading activity.

[ADD LINK: Database schema or SQL table creation script, if included in the repository]

6. Methodology and Data Preparation

The analysis followed these main stages:

Data Extraction: Used Python to retrieve earnings announcements and historical stock-price data from the Financial Modeling Prep API.

View Python Data Extraction Script

Data Preparation: Organized the extracted data into structured datasets suitable for analysis and database storage.

Database Storage: Imported the datasets into PostgreSQL, creating separate tables for earnings announcements and historical stock prices.

Data Quality Checks: Examined missing values, duplicate announcement dates, and inconsistencies in financial figures. Identified anomalies were investigated and corrected where necessary.

Earnings Surprise Calculation: Compared actual EPS and revenue against analyst estimates to calculate the percentage surprise for each metric.

Stock Price Performance Analysis: Used SQL queries to examine stock returns over one, three, and five trading sessions following each earnings announcement.

Comparative Analysis: Compared the magnitude of earnings surprises with subsequent stock returns to identify patterns in Apple's market reaction.

7. SQL Analysis

SQL was used to investigate the relationship between Apple's quarterly earnings results and subsequent stock-price performance.

The analysis was conducted in PostgreSQL using queries covering the following areas:

7.1 Data Exploration and Validation

Examined the structure and quality of the datasets, including missing values, duplicate records, and date coverage.

View SQL Queries – Data Exploration and Validation

7.2 Earnings Surprise Analysis

Calculated the percentage differences between actual and estimated EPS and revenue to determine the extent to which Apple exceeded or missed analyst expectations.

View SQL Queries – Earnings Surprise Analysis

7.3 Post-Earnings Stock Performance

Measured Apple's stock-price returns over one, three, and five trading sessions following each earnings announcement.

View SQL Queries – Stock Performance Analysis

7.4 Combined Earnings and Stock Performance Analysis

Combined the earnings and historical stock-price datasets to compare earnings surprises with subsequent market reactions across the 20 announcements.

View Complete SQL Analysis

8. Executive Summary and Key Findings

[ADD EXECUTIVE SUMMARY HERE]

Key Findings

[ADD YOUR VERIFIED KEY FINDINGS HERE]
