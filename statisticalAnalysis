import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statistics
from datetime import datetime
import os

# Fetch historical data
def fetch_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    return data['Adj Close']

# User input for stock tickers
ticker1 = input("Enter the ticker for the first stock: ")
ticker2 = input("Enter the ticker for the second stock: ")
tickers = [ticker1, ticker2]

# Define the date ranges for backtesting
backtest_start_date = "2021-01-01"
backtest_end_date = "2023-12-31"  # Last day of 2023

# Fetch the backtest data
backtest_data = fetch_data(tickers, backtest_start_date, backtest_end_date)

# Calculate the 'Difference' column for backtesting
backtest_data['Difference'] = backtest_data[ticker1] - backtest_data[ticker2]

# Calculate mean and standard deviation from backtest data
differences = backtest_data['Difference']
differences_mean = differences.mean()
std_dev = differences.std()

# Perform regression analysis
X = backtest_data[ticker1].values.reshape(-1, 1)
y = backtest_data[ticker2].values
reg = LinearRegression().fit(X, y)
print(f"R-squared: {reg.score(X, y)}")
print(f"Coefficient for {ticker1}: {reg.coef_[0]}")

# Plot the results
plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X, reg.predict(X), color='red', label='Regression Line')
plt.xlabel(tickers[0])
plt.ylabel(tickers[1])
plt.title('Linear Regression between {} and {}'.format(ticker1, ticker2))
plt.legend()
plt.show()

# Plot the price movements of the two stocks
plt.figure(figsize=(14, 7))
plt.plot(backtest_data[ticker1], label=ticker1, color='blue')
plt.plot(backtest_data[ticker2], label=ticker2, color='orange')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.title('Price Movement of {} and {} (2021-2023)'.format(ticker1, ticker2))
plt.legend()
plt.show()

# Plot the difference between the two stocks along with mean and standard deviation bands
plt.figure(figsize=(14, 7))
plt.plot(backtest_data['Difference'], label='Difference ({} - {})'.format(ticker1, ticker2), color='green')
plt.axhline(differences_mean, color='red', linestyle='--', label='Mean Difference')
plt.axhline(differences_mean + std_dev, color='red', linestyle=':', label='Mean + 1 Std Dev')
plt.axhline(differences_mean - std_dev, color='red', linestyle=':', label='Mean - 1 Std Dev')
plt.xlabel('Date')
plt.ylabel('Difference ($)')
plt.title('Difference Between {} and {} (2021-2023)'.format(ticker1, ticker2))
plt.legend()
plt.show()

# Output the calculated statistics
print(f"Mean of differences: {differences_mean}")
print(f"Standard deviation of differences: {std_dev}")

# Store the calculated statistics and tickers in a dictionary
statistics = {
    'ticker1': ticker1,
    'ticker2': ticker2,
    'mean_difference': differences_mean,
    'std_dev_difference': std_dev,
    'regression_coefficient': reg.coef_[0]
}

# Save the statistics to a Python script in the home directory
home_dir = os.path.expanduser("~")
file_path = os.path.join(home_dir, 'trading_statistics.py')
with open(file_path, 'w') as f:
    f.write(f"ticker1 = '{statistics['ticker1']}'\n")
    f.write(f"ticker2 = '{statistics['ticker2']}'\n")
    f.write(f"differences_mean = {statistics['mean_difference']}\n")
    f.write(f"std_dev = {statistics['std_dev_difference']}\n")
    f.write(f"regression_coefficient = {statistics['regression_coefficient']}\n")

print(f"Statistics and tickers saved to {file_path}")
