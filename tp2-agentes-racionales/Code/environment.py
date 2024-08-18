from random import random

class Environment:
    def __init__(self,sizeX,sizeY,init_posX,init_posY,dirt_rate): #constructor

        self.sizeX=sizeX
        self.sizeY=sizeY
        self.posX=init_posX
        self.posY=init_posY
        self.dirt_rate=dirt_rate
        self.matrix=[]
        self.number_of_dirt=0
        

        for i in range(sizeX): #incializa en 0 
            self.matrix.append([])
            for j in range(sizeY):
                self.matrix[i].append(0)

        for i in range(sizeX): # llena de suciedad
            for j in range(sizeY):
                if random()<=dirt_rate:
                    self.matrix[i][j]=1
                    self.number_of_dirt+=1



    def print_environment(self): #imprime el ambiente
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                print(self.matrix[i][j],end=' ')
            print()
