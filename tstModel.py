from model.model import Model

mymodel = Model()
mymodel.buildGraph(2200)
n, e = mymodel.getGraphDetails()
print(f"Nodi: {n}")
print(f"Archi: {e}")
