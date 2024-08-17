class Agent:
    def __init__(self,env): # recibe como parametro un objeto de la clase Environment
        self.performance=0
        self.battery=1000
        self.posX = 0
        self.posY = 0
        self.matrix = env.matrix        

    def get_performance(self):
        return self.performance
    
    def get_battery(self):
        return self.battery

    def suck(self): # Limpia la casilla actual
        if self.matrix[self.posX][self.posY]==1:
            self.matrix[self.posX][self.posY]=0
            self.after_clean()

    def perspective(self,env): # sensa el entorno
        pass

    def think(self):
        pass # implementa las acciones a seguir por el agente "

    def move_up(self): #mueve el agente hacia arriba
        if self.posY>0:
            self.posY+=1

    def move_down(self): #mueve el agente hacia abajo
        if  self.posY<len(self.matrix)-1:
            self.posY-=1

    def move_left(self): #mueve el agente hacia la izquierda
        if self.posX>0:
            self.posX-=1

    def move_right(self): #mueve el agente hacia la derecha
        if self.posX<len(self.matrix[0])-1:
            self.posX+=1

    def do_nothing(self): #no hace nada (idle)
        pass

    def afer_clean(self): #le quita 1 de bateria por cada casilla limpiada y retorna el perf

        if  self.battery >= 1 :
            self.battery-=1
            self.performance+=1
            return self.performance
        
        if self.battery==0:
            print("no more battery")
            return self.performance
    



