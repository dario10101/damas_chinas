from AlphaBeta import alphabeta_search
from Board import App
from tkinter import *
from Damas import Damas

class Controller:
    def __init__(self):
        self.turno=1
        self.tablero = [[1,0,1,0,1,0,1,0],
                        [0,1,0,1,0,1,0,1],
                        [1,0,1,0,1,0,1,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,3,0,3,0,3,0,3],
                        [3,0,3,0,3,0,3,0],
                        [0,3,0,3,0,3,0,3]]
        self.game = Damas(self.tablero)

    def run(self):
        root = Tk()
        vista = App(root, self.tablero)
        while True:
            if(self.turno == 1):
                vista.canvas.bind('<Button-1>', vista.handler)
                vista.player = 2
            while True:
                if vista.player == 1:
                    self.tablero = vista.getTablero()
                    break
                root.update_idletasks()
                root.update()
            self.turno = 2
            if(self.turno == 2):
                #self.tableroActual(self.tablero)
                self.tablero = self.jugadaPC(self.tablero)
                #self.tableroActual(self.tablero)
                vista.setTablero(self.tablero)
                self.turno = 1


    def tableroActual(self, tablero):
        for i in tablero:
            print(i)

    def getGame(self):
        return self.game

    def jugadaPC(self, state):
        return alphabeta_search(self.tablero, self.game)

play = Controller()
play.run()
