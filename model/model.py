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
        for edge in edges:
            if graph.has_edge(DAO.getCountry(edge.state2no), DAO.getCountry(edge.state1no)):
                pass
            else:
                graph.add_edge(DAO.getCountry(edge.state1no), DAO.getCountry(edge.state2no))


        result1 = []
        for node in nodes:
            result1.append(f"{node.__str__()}: {graph.degree(node)}")
            print(f"{node.__str__()}: {graph.degree(node)}")
            
        return result1, nx.number_connected_components(graph)










