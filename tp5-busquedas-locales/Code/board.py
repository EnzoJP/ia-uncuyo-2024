from random import randint

class Board:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.queens = []
        self.queens_attacking = 0

    def random_board(self): #coloca n reinas en el tablero una por columna
        for i in range(self.n):
            x = randint(0, self.n - 1)
            self.board[x][i] = 1
            self.queens.append((x, i))

    def objective_function(self): 
        self.queens_attacking = 0  # reinicio cada vez que calculo los ataques
        pair_attacking_queens = self.calculate_attacking_queens()
        return pair_attacking_queens


    def calculate_attacking_queens(self):
        viseted_queens = []
        self.queens_attacking = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    self.queens_attacking += self.calculate_attacking_queens_in_row(i,j,viseted_queens)
                    self.queens_attacking += self.calculate_attacking_queens_in_diagonal(i,j,viseted_queens)
                    self.queens_attacking += self.calculate_attacking_queens_in_diagonal2(i,j,viseted_queens)
        return self.queens_attacking
                    
    def calculate_attacking_queens_in_row(self, row, column,viseted_queens):
        attacking = 0
        for i in range(0,self.n):
            if i != column and self.board[row][i] == 1:
                if (row,i) not in viseted_queens:
                    attacking += 1
                    viseted_queens.append((row,i))
        return attacking

    def calculate_attacking_queens_in_diagonal(self, row, column,viseted_queens):
        attacking = 0
        i = row
        j = column
        while i > 0 and j > 0:
            i -= 1
            j -= 1
            if self.board[i][j] == 1:
                if (i,j) not in viseted_queens:
                    attacking += 1
                    viseted_queens.append((i,j))
        i = row
        j = column
        while i < self.n - 1 and j < self.n - 1:
            i += 1
            j += 1
            if self.board[i][j] == 1:
                if (i,j) not in viseted_queens:
                    attacking += 1
                    viseted_queens.append((i,j))
        return attacking
    
    def calculate_attacking_queens_in_diagonal2(self, row, column,viseted_queens):
        attacking = 0
        i = row
        j = column
        while i > 0 and j < self.n - 1:
            i -= 1
            j += 1
            if self.board[i][j] == 1:
                if (i,j) not in viseted_queens:
                    attacking += 1
                    viseted_queens.append((i,j))
        i = row
        j = column
        while i < self.n - 1 and j > 0:
            i += 1
            j -= 1
            if self.board[i][j] == 1:
                if (i,j) not in viseted_queens:
                    attacking += 1
                    viseted_queens.append((i,j))
        return attacking
    
    def move_queen(self, row, column): #mueve la reina de la misma columna a la fila indicada
        for i in range(self.n):
            if self.board[i][column] == 1:
                self.board[i][column] = 0
                self.board[row][column] = 1
                self.queens[column] = (row, column)
                break
    
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()