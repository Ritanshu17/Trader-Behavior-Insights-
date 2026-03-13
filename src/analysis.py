import pandas as pd

def merge_datasets(trader_df, sentiment_df):

    sentiment_df["date"] = pd.to_datetime(sentiment_df["date"]).dt.date

    merged = trader_df.merge(sentiment_df,on="date",how="left")

    return merged


def trader_summary(df):

    summary = df.groupby("Account").agg({

        "Closed PnL":"sum",
        "Size USD":"mean",
        "Leverage":"mean",
        "Account":"count"

    }).rename(columns={"Account":"trade_count"})

    return summary.reset_index()


def sentiment_strategy(df):

    return df.groupby("classification")["Closed PnL"].mean()


def trade_size_analysis(df):

    return df.groupby("trade_size_category")["Closed PnL"].mean()


def sentiment_trade_activity(df):

    return df.groupby("classification").size()


def contrarian_strategy(df):

    fear_trades = df[df["classification"].isin(["Fear","Extreme Fear"])]

    return fear_trades["Closed PnL"].mean()