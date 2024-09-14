from random import random, randint

class Agent:
    def __init__(self, env):  # recibe como parámetro un objeto de la clase Environment
        self.performance = 0
        self.battery = 1000
        self.posX = 0
        self.posY = 0
        self.matrix = env.matrix
        self.battery_used = 0
        self.dirt_left = env.number_of_dirt        

    def get_performance(self):
        return self.performance
    
    def get_battery(self):
        return self.battery

    def suck(self):  # Limpia la casilla actual
        
        if self.matrix[self.posX][self.posY] == 1:
            self.matrix[self.posX][self.posY] = 0
            self.after_clean()

    def perspective(self):  # Sensa el entorno (casilla)
        return self.matrix[self.posX][self.posY] == 1

    def think(self, env):  # Implementa las acciones a seguir por el agente 
        if self.perspective():
            self.suck()
        else:
            action = randint(0, 3)
            if action == 0:
                self.move_up()
            elif action == 1:
                self.move_down()
            elif action == 2:
                self.move_left()
            elif action == 3:
                self.move_right()

    def move_up(self):  # Mueve el agente hacia arriba
        if self.posX > 0:
            self.posX -= 1
            self.battery -= 1
            if self.dirt_left > 0:
                self.battery_used += 1
        else:
            self.do_nothing()

    def move_down(self):  # Mueve el agente hacia abajo
        if self.posX < len(self.matrix) - 1:
            self.posX += 1
            self.battery -= 1
            if self.dirt_left > 0:
                self.battery_used += 1
        else:  
            self.do_nothing()

    def move_left(self):  # Mueve el agente hacia la izquierda
        if self.posY > 0:
            self.posY -= 1
            self.battery -= 1
            if self.dirt_left > 0:
                self.battery_used += 1
        else:
            self.do_nothing()

    def move_right(self):  # Mueve el agente hacia la derecha
        if self.posY < len(self.matrix[0]) - 1:
            self.posY += 1
            self.battery -= 1
            if self.dirt_left > 0:
                self.battery_used += 1
        else:
            self.do_nothing()

    def do_nothing(self):  # No hace nada (idle)
        self.battery -= 1
        if self.dirt_left > 0:
                self.battery_used += 1

    def after_clean(self):  # Le quita 1 de batería por cada casilla limpiada y retorna el performance
        
        if self.battery > 0:
            self.battery -= 1
            self.performance += 1
            if self.dirt_left > 0:
                self.battery_used += 1
                self.dirt_left -= 1
            return self.performance
        
        if self.battery == 0:
            print("no more battery")
            return self.performance
        
    def get_battery_used(self):
        return self.battery_used
