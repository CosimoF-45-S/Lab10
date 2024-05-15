import flet as ft
from UI import view
import networkx as nx
import time

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._year = 0

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        self.readYear()
        try:
            year = int(self._year)
            if year > 2016 or year < 1816:
                self._view.create_alert("Inserire un anno compreso tra 1816 e 2016")
            else:
                start = time.time()
                output = self._model.handleCalcola(year)
                self._view._txt_result.controls.append(ft.Text("Stati e Confini:\n"))
                for i in output[0]:
                    self._view._txt_result.controls.append(ft.Text(i))
                self._view._txt_result.controls.append(ft.Text("\nComponenti connesse: "))
                self._view._txt_result.controls.append(ft.Text(f"{output[1]}"))
                self._view.update_page()
                end = time.time()
                print(end - start)



        except ValueError:
            self._view.create_alert("Per favore inserire un intero")

    def readYear(self):
        self._year = self._view._txtAnno.value

