from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def cluster_traders(summary):

    features = summary[
        ["Closed PnL","Size USD","Leverage","trade_count"]
    ]

    scaler = StandardScaler()

    scaled = scaler.fit_transform(features)

    model = KMeans(n_clusters=3, random_state=42)

    summary["cluster"] = model.fit_predict(scaled)

    return summary