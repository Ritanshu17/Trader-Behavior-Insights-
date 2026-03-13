import pandas as pd

def load_sentiment_data(path):
    return pd.read_csv(path)

def load_trader_data(path):
    return pd.read_csv(path)
