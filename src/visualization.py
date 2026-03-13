import matplotlib.pyplot as plt
import seaborn as sns

def sentiment_profit_plot(df):

    plt.figure(figsize=(10,6))

    sns.boxplot(data=df,x="classification",y="Closed PnL")

    plt.xticks(rotation=45)

    plt.savefig("results/sentiment_vs_profit.png")

    plt.show()


def pnl_distribution(df):

    plt.figure(figsize=(10,6))

    sns.histplot(df["Closed PnL"],bins=40,kde=True)

    plt.savefig("results/pnl_distribution.png")

    plt.show()


def leverage_vs_pnl(df):

    plt.figure(figsize=(10,6))

    sns.scatterplot(data=df,x="Leverage",y="Closed PnL",alpha=0.4)

    plt.savefig("results/leverage_vs_pnl.png")

    plt.show()


def correlation_plot(df):

    plt.figure(figsize=(10,6))

    sns.heatmap(df.corr(numeric_only=True),annot=True,cmap="coolwarm")

    plt.savefig("results/correlation_matrix.png")

    plt.show()