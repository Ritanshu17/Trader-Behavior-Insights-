import pandas as pd

def preprocess_sentiment(df):

    df["date"] = pd.to_datetime(df["date"])

    return df[["date","classification","value"]]


def preprocess_trader(df):

    df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="ms")

    df["date"] = df["Timestamp"].dt.date

    df["Closed PnL"] = pd.to_numeric(df["Closed PnL"], errors="coerce")

    return df