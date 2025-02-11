import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.decomposition import PCA
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from scipy.optimize import minimize
#import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler


def main():
    start_date = '2022-01-01'
    end_date = '2023-12-31'

    # Download universe data
    tickers = [
        'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA', 'JPM', 'BAC', 'WMT',
        'PG', 'JNJ', 'UNH', 'HD', 'MA', 'V', 'DIS', 'NFLX', 'CSCO', 'INTC',
        'PFE', 'KO', 'PEP', 'MRK', 'VZ', 'T', 'CMCSA', 'ABT', 'MCD', 'ADBE',
        'CRM', 'NKE', 'TMO', 'COST', 'DHR', 'ACN', 'LLY', 'AVGO', 'TXN', 'UNP',
        'NEE', 'BMY', 'RTX', 'QCOM', 'ORCL', 'HON', 'UPS', 'IBM', 'LIN', 'AMT',
        'CVX', 'XOM', 'BA', 'CAT', 'GS', 'MS', 'BLK', 'C', 'WFC', 'AXP',
        'MMM', 'GE', 'F', 'GM', 'SBUX', 'MO', 'PM', 'CVS', 'LOW', 'TGT',
        'AMD', 'PYPL', 'BKNG', 'GILD', 'MDLZ', 'TMUS', 'TJX', 'SPGI', 'BDX', 'ADP',
        'ZTS', 'ISRG', 'CI', 'ANTM', 'CCI', 'DUK', 'SO', 'D', 'AEP', 'EXC',
        'PLD', 'COP', 'EOG', 'SLB', 'OXY', 'PSX', 'KMI', 'MPC', 'VLO', 'HAL'
    ]


    print(tickers)
    # df = pd.DataFrame()

    # for ticker in tickers:
    #     data = yf.download(ticker, start=start_date, end=end_date)
    #     data.columns = data.columns.droplevel(['Ticker'])
    #     data = data[['Close']]
    #     data = data.rename(columns={'Close': ticker})
    #     df = pd.concat([df, data], axis=1)


    # print(df.head())

if __name__ == "__main__":
    main()