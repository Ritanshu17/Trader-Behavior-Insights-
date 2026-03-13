from src.data_loader import *
from src.preprocessing import *
from src.feature_engineering import *
from src.analysis import *
from src.clustering import *
from src.visualization import *

sentiment = load_sentiment_data("data/raw/historical_data.csv")

trades = load_trader_data("data/raw/fear-greed_index.csv")

sentiment = preprocess_sentiment(sentiment)

trades = preprocess_trader(trades)

merged = merge_datasets(trades,sentiment)

merged = create_features(merged)

merged.to_csv("data/processed/merged_dataset.csv",index=False)

summary = trader_summary(merged)

clusters = cluster_traders(summary)

print("Sentiment Strategy")

print(sentiment_strategy(merged))

print("Trade Size Analysis")

print(trade_size_analysis(merged))

print("Trade Activity")

print(sentiment_trade_activity(merged))

print("Contrarian Strategy Result")

print(contrarian_strategy(merged))

sentiment_profit_plot(merged)

pnl_distribution(merged)

leverage_vs_pnl(merged)

correlation_plot(merged)