from Game import Game
import math

class Damas():
    
    def __init__(self, tablero):
        self.dimension = len(tablero)
        self.tablero = tablero
        self.profundidad = 5
        
    def actions(self,lista,Jugador):
        listaHijos=[]
        print('-----')
        for y in range(len(lista)):
            for x in range(len(lista)):
                listaCopia = self.CopiarLista(lista)
                #J U G A D O R   1
                if(lista[y][x] == Jugador):
                    #INFERIOR DERECHA
                    if((y+1) < len(lista) and (x+1) < len(lista)):
                        if(lista[(y+1)][(x+1)] == 0):
                            listaCopia[y][x]=0
                            if((y+1) == len(lista)-1 and Jugador == 1):
                                listaCopia[(y+1)][(x+1)]=3
                            else:
                                listaCopia[(y+1)][(x+1)]=Jugador
                            if(listaCopia != lista):
                                    listaHijos.append(listaCopia)
                            else:
                                print("Igual!")
                        elif((y+2) < len(lista) and (x+2) < len(lista)):
                            if(lista[(y+2)][(x+2)] == 0 and lista[(y+1)][(x+1)] == 2):
                                listaCopia[y][x]=0
                                if((y+2) == len(lista)-1  and Jugador == 1):
                                    listaCopia[(y+2)][(x+2)]=3
                                else:
                                    listaCopia[(y+2)][(x+2)]=Jugador
                                listaCopia[(y+1)][(x+1)]=0
                                if(listaCopia != lista):
                                    listaHijos.append(listaCopia)
                                else:
                                    print("Igual!")
                        listaCopia = self.CopiarLista(lista)
                    #INFERIOR IZQUIERDA
                    if(((y+1) < len(lista) and (x-1) >= 0)):
                        if(lista[(y+1)][(x-1)] == 0):
                            listaCopia[y][x]=0
                            if((y+1) == len(lista)-1  and Jugador == 1):
                                listaCopia[(y+1)][(x-1)]=3
                            else:
                                listaCopia[(y+1)][(x-1)]=Jugador
                            if(listaCopia != lista):
                                listaHijos.append(listaCopia)
                            else:
                                print("Igual!")
                        elif(((y+2) < len(lista) and (x-2) >= 0)):
                            if(lista[(y+2)][(x-2)] == 0 and lista[(y+1)][(x-1)] == 2):
                                listaCopia[y][x]=0
                                listaCopia[(y+1)][(x-1)] = 0
                                if((y+2)==len(lista)-1  and Jugador == 1):
                                    listaCopia[(y+2)][(x-2)]=3
                                else:
                                    listaCopia[(y+2)][(x-2)]=Jugador
                                if(listaCopia != lista):
                                    listaHijos.append(listaCopia)
                                else:
                                    print("Igual!")
                        listaCopia = self.CopiarLista(lista)
                #J U G A D O R   2
                if(lista[y][x] ==  Jugador):
                    #SUPERIOR DERECHA
                    if(((y-1) >= 0) and (x+1) < (len(lista))):
                        if(lista[(y-1)][(x+1)] == 0):
                            listaCopia[y][x]=0
                            if((y-1) == 0  and Jugador == 2):
                                listaCopia[(y-1)][(x+1)]=4
                            else:
                                listaCopia[(y-1)][(x+1)]=Jugador
                            if(listaCopia != lista):
                                listaHijos.append(listaCopia)
                            else:
                                print("Igual!")
                        elif(((y-2) >= 0) and (x+2) < (len(lista))):
                            if(lista[(y-2)][(x+2)] == 0 and lista[(y-1)][(x+1)] == 1):
                                listaCopia[y][x]=0
                                listaCopia[(y-1)][(x+1)] = 0
                                if((y-2) == 0 and Jugador == 2):
                                    listaCopia[(y-2)][(x+2)]=4
                                else:
                                    listaCopia[(y-2)][(x+2)]=Jugador
                                if(listaCopia != lista):
                                    listaHijos.append(listaCopia)
                                else:
                                    print("Igual!")
                        listaCopia = self.CopiarLista(lista)
                    #SUPERIOR IZQUIERDA
                    if(((y-1) >= 0) and (x-1) >= 0):
                        if(lista[(y-1)][(x-1)] == 0):
                            listaCopia[y][x]=0
                            if((y-1) == 0 and Jugador == 2):
                                listaCopia[(y-1)][(x-1)]=4
                            else:
                                listaCopia[(y-1)][(x-1)]=Jugador
                            if(listaCopia != lista):
                                listaHijos.append(listaCopia)
                            else:
                                print("Igual!")
                        elif(((y-2) >= 0) and (x-2) >= 0):
                            if(lista[(y-2)][(x-2)] == 0 and (lista[(y-1)][(x-1)] == 1)):
                                listaCopia[y][x]=0
                                listaCopia[(y-1)][(x-1)] = 0
                                if((y-2) == 0 and Jugador == 2):
                                    listaCopia[(y-2)][(x-2)]=4
                                else:
                                    listaCopia[(y-2)][(x-2)]=Jugador
                                if(listaCopia != lista):
                                    listaHijos.append(listaCopia)
                                else:
                                    print("Igual!")
                        listaCopia = self.CopiarLista(lista)
        return listaHijos
        
    

    def display(self):
        #Print or otherwise display the state.
        print(self.tablero)
        
            
    def terminal_test(self, tablero, profundidad):
        TerminaJuego=False
        FichasRestantesPC=0
        FichasRestantesHumano = 0
        if FichasRestantesPC ==0 or FichasRestantesHumano ==0:
            TerminaJuego = True
        if profundidad == self.profundidad:
            TerminaJuego = True
        return TerminaJuego



    def utility(self, tablero):
        incremento=20
        pesoFichasPc = 0
        pesoFichasHumano = 0
        tamTablero = len(tablero)
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                if (tablero[i][j]==1):
                    pesoFichasPc = pesoFichasPc + ((i+1)*incremento)
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                if (tablero[i][j]==2):
                        pesoFichasHumano=pesoFichasHumano+(tamTablero*incremento)
            tamTablero=tamTablero-1
        return pesoFichasPc - pesoFichasHumano
            
    
    def CopiarLista(self,lista):
        ListaCopia = []
        ListaCopia=[x[:] for x in lista]
        return ListaCopia
