import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        pass

    def handleCalcola(self, year: int):

        graph = nx.Graph()

        #PRENDI I NODI E INSERISCILI
        nodes = DAO.getCountries()
        graph.add_nodes_from(nodes)


        #PRENDI GLI ARCHI RELATIVI ALL'INPUT
        edges = DAO.getBorders(year)
        graph.add_edges_from(edges)


        result1 = []
        for node in nodes:
            result1.append(f"{DAO.getCountry(node).__str__()}: {graph.degree(node)}")
            
        return result1, nx.number_connected_components(graph)










