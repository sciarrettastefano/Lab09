from database.DAO import DAO
import networkx as nx

class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._allAirports = []
        self._idMapAirports = {}
        self.getAllAirports()


    def buildGraph(self, xMin):
        self._graph.clear()
        if len(self._allAirports) == 0:
            print("Lista vuota.")
            return
        allEdges = self.getAllEdges(xMin)
        #self._graph.add_nodes_from(self._allAirports)
        for e in allEdges:
            self._graph.add_edge(e[0], e[1], weight=e[2])


    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()


    def getAllAirports(self):
        self._allAirports = DAO.getAllAirports()
        for airport in self._allAirports:
            self._idMapAirports[airport.ID] = airport
        return self._allAirports


    def getAllEdges(self, xMin):
        return DAO.getAllEdges(xMin, self._idMapAirports)



