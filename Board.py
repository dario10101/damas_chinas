# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:31:26 2018

@author: eumartinez

"""
from tkinter import *

class App:
       
    def __init__(self, master, model):
        self.varClick = 1
        self.frame = Frame(master)
        self.frame.pack()
        self.height=600
        self.width=600
        self.grid_column=len(model)
        self.grid_row=len(model)
        self.canvas = Canvas(self.frame, height=self.height, width=self.width)
        self.cellwidth = int(self.canvas["width"])/self.grid_column
        self.cellheight = int(self.canvas["height"])/self.grid_row
        self.draw_grid()
        self.canvas.pack()
        self.model=model
        self.player = 2
        self.pos=(0,0)
        self.hi_there = Button(self.frame, text="Jugar", command=self.start_Game)
        self.hi_there.pack(side=LEFT)
        
    def handler(self,event):
        return self.__onClick(event)

    def getTablero(self):
        return self.model
    def setTablero(self, tablero):
        self.model = tablero
        self.drawChips()
      
    def draw_grid(self):
        for i in range(self.grid_row):
            for j in range(self.grid_column):
                self.draw_rectangle(i,j)
                

    def draw_rectangle(self,i,j):
        x1 = i * self.cellwidth
        y1 = j * self.cellheight
        x2 = x1 + self.cellwidth
        y2 = y1 + self.cellheight
        color1 = "red"
        if (i%2 == 0 and j%2 > 0) or (i%2 > 0 and j%2 == 0):            
            color = "khaki"
        else:
            color = "DarkOrange4"
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        
    
    def drawChips(self):
        for i in range(len(self.model)):
            row=self.model[i]
            for j in range(len(row)):
                val=self.model[i][j]
                x=j*self.cellwidth
                y=i*self.cellheight                
                if(val == 1):
                    self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='yellow')
                elif(val == 2):
                    self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='gold3')
                elif (val == 3):
                    self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='gray1')
                elif(val == 4):
                    self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='gray15')
                elif(val == 0):
                    self.draw_rectangle(j,i)
        
    def __onClick(self, event):
        if self.varClick == 1:
            i=int(event.y/self.cellheight)
            j=int(event.x/self.cellwidth)
            self.pos =(i,j)
            if(self.model[i][j] > 2):
                self.varClick = 2
        
        elif self.varClick == 2:
            varI=int(event.y/self.cellheight)
            varJ=int(event.x/self.cellwidth)
            movimiento = [varI,varJ]
            if(self.ComprobarLibre(movimiento) == True):
                nodoAComer = self.PuedeComer(movimiento)
                if(nodoAComer[0] != -1):
                    if varI == 7:
                        self.model[varI][varJ] = 4
                    else:
                        #print("no ha coronado")
                        self.model[varI][varJ] = 3
                    self.model[self.pos[0]][self.pos[1]] = 0
                    self.model[nodoAComer[0]][nodoAComer[1]] = 0
                    self.player = 1
                elif(self.PuedeMoverse(movimiento) == True):
                    if varI == 0:
                        #print("coronado")
                        self.model[varI][varJ] = 4
                    else:
                        #print("no ha coronado")
                        self.model[varI][varJ] = 3
                    self.model[self.pos[0]][self.pos[1]] = 0
                    self.player = 1

                        
            self.drawChips()
            self.varClick = 1
        #print('click: ' + str(self.varClick))
        return True

    def  start_Game(self):
        #print('start game')
        self.draw_grid()        
        self.drawChips()
        

    def ComprobarLibre(self,movimiento):
        resultado = False
        i=movimiento[0]
        j=movimiento[1]
        if self.model[i][j]==0:
            resultado = True
        return resultado

    def PuedeMoverse(self, movimiento):
        resultado = False
        diferenciaI = abs(movimiento[0] - self.pos[0])
        diferenciaJ = abs(movimiento[1] - self.pos[1])
        if diferenciaI == 1 and diferenciaJ == 1:
            if self.pos[0] > movimiento[0]:
                resultado = True
        return resultado

    def PuedeComer(self, movimiento):
        resultado = [-1,-1]
        i=movimiento[0]
        j=movimiento[1]
        diferenciaI = movimiento[0] - self.pos[0]
        diferenciaJ = movimiento[1] - self.pos[1]
        if(abs(diferenciaI) == 2 and abs(diferenciaJ) == 2):   
            if(self.pos[0] > movimiento[0]):
                posicionINodoAComer = self.pos[0] - 1
                posicionJNodoAComer = 0
                if(diferenciaJ < 0):
                    posicionJNodoAComer = self.pos[1] - 1
                elif(diferenciaJ > 0):
                    posicionJNodoAComer = self.pos[1] + 1
                if(self.model[posicionINodoAComer][posicionJNodoAComer] <= 2):
                    resultado = [posicionINodoAComer,posicionJNodoAComer] 
        return resultado
