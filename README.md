# Pairs Trading Algorithm with QuantConnect

This repository contains a pairs trading algorithm developed to exploit statistical relationships between correlated stocks. The project involves collecting and analyzing stock data, conducting regression analysis, visualizing the data, executing trades based on statistical thresholds, and backtesting the strategy.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Implementation Details](#implementation-details)
    - [Data Collection and Analysis](#data-collection-and-analysis)
    - [Regression Analysis](#regression-analysis)
    - [Visualization](#visualization)
    - [Trading Strategy](#trading-strategy)
    - [Backtesting](#backtesting)
3. [Code Structure](#code-structure)
    - [QuantConnect Algorithm](#quantconnect-algorithm)
    - [Visual Studio Code Analysis](#visual-studio-code-analysis)

## Project Overview

Pairs trading is a market-neutral strategy that involves matching a long position with a short position in two stocks that have a high correlation. The algorithm identifies overvalued and undervalued stocks based on their historical price differences and executes trades accordingly.

## Implementation Details

### Data Collection and Analysis

- **Libraries Used**: Python, pandas, yfinance
- **Description**: Collected historical stock data using the yfinance API. Utilized pandas to manage and analyze the data efficiently. Calculated the differences between the prices of the two stocks to identify statistical relationships.

### Regression Analysis

- **Libraries Used**: scikit-learn
- **Description**: Conducted regression analysis to understand the relationship between the two stocks. This helped in establishing the statistical foundation for the pairs trading strategy.

### Visualization

- **Libraries Used**: Matplotlib
- **Description**: Visualized the stock prices, their differences, and the regression line to better understand the data and the relationships between the stocks. This also included plotting the mean and standard deviation bands to identify trading signals.

### Trading Strategy

- **Description**: Executed trades based on mean reversion and standard deviation thresholds. When the price difference deviated significantly from the mean, the algorithm would take a long position in the undervalued stock and a short position in the overvalued stock.

### Backtesting

- **Platform Used**: QuantConnect
- **Description**: Backtested the trading strategy using QuantConnect to evaluate its performance over historical data. This involved simulating trades and analyzing the results to ensure the strategy's effectiveness.

## Code Structure

### QuantConnect Algorithm

- **quantconnect_algorithm.py**: Contains the main algorithm for executing trades based on statistical analysis.

### Visual Studio Code Analysis

- **statisticalAnalysis.py**: Script to fetch historical data, perform statistical analysis, and generate trading statistics.
- **trading_statistics.py**: Generated script containing the calculated statistics used by the QuantConnect algorithm.

