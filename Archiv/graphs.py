import pandas as pd
from operator import itemgetter
import numpy as np
import networkx as nx


class create_graph:
    
    def __init__(self):
        data = 'European_electricity_network.csv'
        self.Network = pd.read_csv(data)
        self.graph = np.asarray(self.Network[['Origin', 'Destination']])
        self.nodes = np.unique(self.graph)
        self.weights = list(map(float, self.Network['Electricity_Flow']))
    
    def networkList(self):
        # create network graph with nodes
        G = nx.DiGraph()
        for node in self.nodes:
            G.add_node(node)
        
       # add edges 
        self.graph_1 = []
        for edge in self.graph:
            G.add_edge(edge[0], edge[1])
            self.graph_1.append((edge[0], edge[1]))

        labels = dict(list(zip(self.graph_1, self.weights)))
        
        return G, labels

    
class graphStats:
    
    def calculate_degree_centrality(self, graph):
        dgc_key = []
        dgc_value = []
        g = graph

        dc = nx.degree_centrality(g)
        nx.set_node_attributes(g, dc, 'degree_cent')
        
        degcent_sorted = sorted(dc.items(), key=operator.itemgetter(1), reverse=True)

        for key, value in degcent_sorted:
            dgc_key.append(str(key))
            dgc_value.append(value)

        return dgc_key, dgc_value
    

    def calculate_betweenness_centrality(self, graph):
        btc_key = []
        btc_value = []
        g = graph

        bc = nx.betweenness_centrality(g)

        betcent_sorted = sorted(bc.items(), key=itemgetter(1), reverse=True)

        for key, value in betcent_sorted:
            btc_key.append(str(key))
            btc_value.append(value)

        return btc_key, btc_value
