import pandas as pd

def load_graph(file):

    data = pd.read_csv(file)

    graph = {}

    for _, row in data.iterrows():

        c1 = row["Origin"]
        c2 = row["Destination"]
        d = row["Distance"]

        graph.setdefault(c1, []).append((c2, d))
        graph.setdefault(c2, []).append((c1, d))

    return graph
