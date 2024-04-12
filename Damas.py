from Game import Game
import math

class Damas():
    
    def __init__(self, tablero):
        self.dimension = len(tablero)
        self.tablero = tablero
        self.profundidad = 7
        
    def actions(self,lista,Jugador):
        listaHijos3=[]#movimientos sin captura
        listaHijos2=[]#movimientos capturando peon
        listaHijos1=[]#movimientos capturando dama
        for y in range(len(lista)):
            for x in range(len(lista)):
                listaCopia = self.CopiarLista(lista)
                pieza = lista[y][x]
                #Turno 1
                if(pieza <= 2 and pieza > 0 and Jugador == 1):
                    #INFERIOR DERECHA
                    if((y+1) < len(lista) and (x+1) < len(lista)):
                        if(lista[(y+1)][(x+1)] == 0):
                            listaCopia[y][x]=0
                            if((y+1) == len(lista)-1 and Jugador == 1):
                                listaCopia[(y+1)][(x+1)]=2
                            else:
                                listaCopia[(y+1)][(x+1)]=pieza
                            if(listaCopia != lista):
                                    listaHijos3.append(listaCopia)
                        elif((y+2) < len(lista) and (x+2) < len(lista)):
                            #puede capturar?
                            capturado = lista[(y+1)][(x+1)]
                            if(lista[(y+2)][(x+2)] == 0 and capturado > 2):
                                listaCopia[y][x]=0
                                if((y+2) == len(lista)-1  and Jugador == 1):
                                    listaCopia[(y+2)][(x+2)] = 2  #si llego a la ultima jugada, se vielve reina
                                else:
                                    listaCopia[(y+2)][(x+2)] = pieza
                                listaCopia[(y+1)][(x+1)]=0
                                if(listaCopia != lista):
                                    if capturado == 3:
                                        listaHijos2.append(listaCopia)
                                    elif capturado == 4:
                                        listaHijos1.append(listaCopia)                                        
                        listaCopia = self.CopiarLista(lista)
                    #INFERIOR IZQUIERDA
                    if(((y+1) < len(lista) and (x-1) >= 0)):
                        if(lista[(y+1)][(x-1)] == 0):
                            listaCopia[y][x]=0
                            if((y+1) == len(lista)-1  and Jugador == 1):
                                listaCopia[(y+1)][(x-1)]=2
                            else:
                                listaCopia[(y+1)][(x-1)]=pieza
                            if(listaCopia != lista):
                                listaHijos3.append(listaCopia)
                        elif(((y+2) < len(lista) and (x-2) >= 0)):
                            capturado = lista[(y+1)][(x-1)]
                            if(lista[(y+2)][(x-2)] == 0 and capturado > 2):
                                listaCopia[y][x]=0
                                listaCopia[(y+1)][(x-1)] = 0
                                if((y+2)==len(lista)-1  and Jugador == 1):
                                    listaCopia[(y+2)][(x-2)]=2
                                else:
                                    listaCopia[(y+2)][(x-2)]=pieza
                                if(listaCopia != lista):
                                    if capturado == 3:
                                        listaHijos2.append(listaCopia)
                                    elif capturado == 4:
                                        listaHijos1.append(listaCopia)
                        listaCopia = self.CopiarLista(lista)
                
                #Turno 2
                if(pieza >= 3 and Jugador == 2):
                    #SUPERIOR DERECHA
                    if(((y-1) >= 0) and (x+1) < (len(lista))):
                        if(lista[(y-1)][(x+1)] == 0):
                            listaCopia[y][x]=0
                            if((y-1) == 0  and Jugador == 2):
                                listaCopia[(y-1)][(x+1)]=4
                            else:
                                listaCopia[(y-1)][(x+1)]=pieza
                            if(listaCopia != lista):
                                listaHijos3.append(listaCopia)
                        elif(((y-2) >= 0) and (x+2) < (len(lista))):
                            capturado = lista[(y-1)][(x+1)]
                            if(lista[(y-2)][(x+2)] == 0 and capturado >= 1 and capturado <= 2):
                                listaCopia[y][x]=0
                                listaCopia[(y-1)][(x+1)] = 0
                                if((y-2) == 0 and Jugador == 2):
                                    listaCopia[(y-2)][(x+2)]=4
                                else:
                                    listaCopia[(y-2)][(x+2)]=pieza
                                if(listaCopia != lista):
                                    if capturado == 1:
                                        listaHijos2.append(listaCopia)
                                    elif capturado == 2:
                                        listaHijos1.append(listaCopia)
                        listaCopia = self.CopiarLista(lista)
                    #SUPERIOR IZQUIERDA
                    if(((y-1) >= 0) and (x-1) >= 0):
                        if(lista[(y-1)][(x-1)] == 0):
                            listaCopia[y][x]=0
                            if((y-1) == 0 and Jugador == 2):
                                listaCopia[(y-1)][(x-1)]=4
                            else:
                                listaCopia[(y-1)][(x-1)]=pieza
                            if(listaCopia != lista):
                                listaHijos3.append(listaCopia)
                        elif(((y-2) >= 0) and (x-2) >= 0):
                            capturado = lista[(y-1)][(x-1)]
                            if(lista[(y-2)][(x-2)] == 0 and capturado >= 1 and capturado <= 2):
                                listaCopia[y][x]=0
                                listaCopia[(y-1)][(x-1)] = 0
                                if((y-2) == 0 and Jugador == 2):
                                    listaCopia[(y-2)][(x-2)]=2
                                else:
                                    listaCopia[(y-2)][(x-2)]=pieza
                                if(listaCopia != lista):
                                    if capturado == 1:
                                        listaHijos2.append(listaCopia)
                                    elif capturado == 2:
                                        listaHijos1.append(listaCopia)
                        listaCopia = self.CopiarLista(lista)


        if len(listaHijos1) > 0:
            return listaHijos1
        if len(listaHijos2) > 0:
            return listaHijos2
        return listaHijos3
        
    

    def display(self):
        #Print or otherwise display the state.
        print(self.tablero)
        
            
    def terminal_test(self, tablero, prof):
        TerminaJuego=False
        cont_teams = self.cont_equipos(tablero)
        FichasRestantesPC= cont_teams[0]#calcular el numero de fichas del pc (1 o 2)
        FichasRestantesHumano = cont_teams[1]#calcular numero de fichas del humano (3 o 4)
        if FichasRestantesPC ==0 or FichasRestantesHumano ==0:
            TerminaJuego = True
        if prof == self.profundidad:
            TerminaJuego = True
        return TerminaJuego



    def utility(self, tablero):
        incremento = 20
        pesoFichasPc = 0
        pesoFichasHumano = 0
        tamTablero = len(tablero)
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                if (tablero[i][j] > 0 and tablero[i][j] <= 2):
                    pesoFichasPc = pesoFichasPc + ((i+1)*incremento)
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                if (tablero[i][j] >= 3):
                        pesoFichasHumano=pesoFichasHumano+(tamTablero*incremento)
            tamTablero=tamTablero-1
        return pesoFichasPc - pesoFichasHumano
            
    
    def CopiarLista(self,lista):
        ListaCopia = []
        ListaCopia=[x[:] for x in lista]
        return ListaCopia

    def cont_equipos(self,tablero):
        cont1 = 0
        cont2 = 0
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                dato = tablero[i][j]
                if dato > 0 and dato <= 2:
                    cont1 = cont1 + 1
                elif dato >= 3:
                    cont2 = cont2 + 1

        return (cont1,cont2)
                    
        

    
"""
tab = [[1,0,1,0,1,0,2,0],
       [0,1,0,1,0,1,0,1],
       [1,0,1,0,1,0,1,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,3,0,3,0,3,0,3],
       [3,0,3,0,3,0,3,0],
       [0,3,0,3,0,3,0,4]]

"""



