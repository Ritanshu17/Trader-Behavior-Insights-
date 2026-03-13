import pandas as pd

def create_features(df):

    df["is_profitable"] = df["Closed PnL"] > 0

    df["trade_size_category"] = pd.qcut(
        df["Size USD"],
        q=3,
        labels=["small","medium","large"]
    )

    df["risk_level"] = pd.cut(
        df["Leverage"],
        bins=[0,5,10,20,50],
        labels=["low","medium","high","extreme"]
    )

    return df