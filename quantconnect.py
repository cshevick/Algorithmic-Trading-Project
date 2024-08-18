from AlgorithmImports import *
import numpy as np
import pandas as pd

# Import statistics from the generated Python script
import trading_statistics as ts

class MyAlgorithm(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2024, 1, 1)
        self.SetEndDate(datetime.now().year, datetime.now().month, datetime.now().day)
        self.SetCash(100000)

        # Debugging prints to ensure correct import
        self.Debug(f"Ticker1: {ts.ticker1}")
        self.Debug(f"Ticker2: {ts.ticker2}")
        self.Debug(f"Differences Mean: {ts.differences_mean}")
        self.Debug(f"Standard Deviation: {ts.std_dev}")

        # Use imported statistics
        self.ticker1 = self.AddEquity(ts.ticker1, Resolution.Daily).Symbol
        self.ticker2 = self.AddEquity(ts.ticker2, Resolution.Daily).Symbol
        self.differences_mean = ts.differences_mean
        self.std_dev = ts.std_dev

        # Warmup period to initialize indicators
        self.SetWarmup(30, Resolution.Daily)

        # Schedule the trading function to run at the end of each day
        self.Schedule.On(self.DateRules.EveryDay(self.ticker1), self.TimeRules.BeforeMarketClose(self.ticker1, 10), self.Trade)

    def Trade(self):
        if self.IsWarmingUp:
            return

        history = self.History([self.ticker1, self.ticker2], 1, Resolution.Daily)
        if not history.empty:
            price1 = history.loc[self.ticker1]['close'].item()
            price2 = history.loc[self.ticker2]['close'].item()
            current_difference = price1 - price2

            if current_difference > self.differences_mean:
                overvalued_ticker, undervalued_ticker = self.ticker1, self.ticker2
                overvalued_price, undervalued_price = price1, price2
            else:
                overvalued_ticker, undervalued_ticker = self.ticker2, self.ticker1
                overvalued_price, undervalued_price = price2, price1

            allocation = 0.0
            if abs(current_difference - self.differences_mean) > 1.25 * self.std_dev:
                allocation = 1.00
            elif abs(current_difference - self.differences_mean) > 1.00 * self.std_dev:
                allocation = 0.80
            elif abs(current_difference - self.differences_mean) > 0.75 * self.std_dev:
                allocation = 0.50
            elif abs(current_difference - self.differences_mean) > 0.50 * self.std_dev:
                allocation = 0.25

            if allocation > 0:
                trade_cash = self.Portfolio.Cash * allocation
                num_shares_overvalued = int(trade_cash // overvalued_price)
                num_shares_undervalued = int(trade_cash // undervalued_price)

                if num_shares_overvalued > 0 and num_shares_undervalued > 0:
                    self.SetHoldings(overvalued_ticker, -allocation)
                    self.SetHoldings(undervalued_ticker, allocation)

    def OnData(self, data):
        pass
