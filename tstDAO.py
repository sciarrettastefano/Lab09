from database.DAO import DAO

mydao = DAO()
allNodes = mydao.getAllAirports()
for n in allNodes:
    print(f"Nodi: {n}")
"""allEdges = mydao.getAllEdges(2200)
for e in allEdges:
    print(e)"""
