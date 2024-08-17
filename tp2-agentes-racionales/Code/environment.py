from random import random

class Environment:
    def __init__(self,sizeX,sizeY,init_posX,init_posY,dirt_rate): #constructor

        self.sizeX=sizeX
        self.sizeY=sizeY
        self.posX=init_posX
        self.posY=init_posY
        self.dirt_rate=dirt_rate
        self.matrix=[]
        

        for i in range(sizeX): #incializa en 0 
            self.matrix.append([])
            for j in range(sizeY):
                self.matrix[i].append(0)

        for i in range(sizeX): # llena de suciedad
            for j in range(sizeY):
                if random.random()<=dirt_rate:
                    self.matrix[i][j]=1

    def accept_action(self,action): #realiza la accion que se le pasa como parametro

        if action==0:
            self.move_up()
        elif action==1:
            self.move_down()
        elif action==2:
            self.move_left()
        elif action==3:
            self.move_right()
        elif action==4:
            self.clean()
        elif action==5:
            self.do_nothing()

    def is_dirty(self): #retorna True si la casilla actual esta sucia

        if self.matrix[self.posX][self.posY]==1:
            return True
        else:
            return False
        

    def print_environment(self): #imprime el ambiente
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                print(self.matrix[i][j],end=' ')
            print()
