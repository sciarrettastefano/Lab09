import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self, e):
        input = self._view.txtIn.value
        try:
            xMin = int(input)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire una distanza minima correttamente.",
                                                          color="red"))
            self._view.update_page()
            print("Errore input")
            return
        self._model.buildGraph(xMin)
        n, e = self._model.getGraphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo con {n} nodi e {e} archi correttamente creato. Ecco l'elenco degli archi:"))
        for e in self._model._graph.edges:
            self._view.txt_result.controls.append(
                ft.Text(f"{e[0]} | {e[1]} - Distanza media: {round(self._model._graph[e[0]][e[1]]['weight'], 1)}"))
        self._view.update_page()


