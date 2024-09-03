from queue import PriorityQueue
import math

def get_neighbors_with_cost(position, grid):
    # Obtener vecinos válidos (arriba, abajo, izquierda, derecha)
    neighbors = []
    asociated_cost = []
    x, y = position
    if x > 0:  # izquierda
        neighbors.append((x - 1, y))
        cost=1
        asociated_cost.append(cost)
    if x < len(grid) - 1:  # derecha
        neighbors.append((x + 1, y))
        cost=3
        asociated_cost.append(cost)
    if y > 0:  # abajo
        neighbors.append((x, y - 1))
        cost=2
        asociated_cost.append(cost)
    if y < len(grid[0]) - 1:  # arriva
        neighbors.append((x, y + 1))
        cost=4
        asociated_cost.append(cost)
    return neighbors,asociated_cost


def get_neighbors(position, grid):
    # Obtener vecinos válidos (arriba, abajo, izquierda, derecha)
    neighbors = []
    x, y = position
    if x > 0:  # Arriba
        neighbors.append((x - 1, y))
    if x < len(grid) - 1:  # Abajo
        neighbors.append((x + 1, y))
    if y > 0:  # Izquierda
        neighbors.append((x, y - 1))
    if y < len(grid[0]) - 1:  # Derecha
        neighbors.append((x, y + 1))
    return neighbors


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def A_star_E1(grid,start,goal):
    frontier = PriorityQueue()
    frontier.put((0, start, []))
    explored = set()
    cost_so_far = {}
    cost_so_far[start] = 0

    while not frontier.empty():
        cost, position, path = frontier.get()

        if position in explored:
            continue

        explored.add(position)

        if grid[position[0]][position[1]] == b'G':
            return path + [position], explored, cost

        neighbors= get_neighbors(position, grid)

        for neighbor in (neighbors):
            new_cost = cost_so_far[position]+ 1 
            if neighbor not in explored or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                frontier.put((new_cost + heuristic(goal, neighbor), neighbor, path + [position]))

    return None, explored, None
    

def A_star_E2(grid, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start, []))
    explored = set()
    cost_so_far = {}
    cost_so_far[start] = 0

    while not frontier.empty():
        priority, position, path = frontier.get()

        if position in explored:
            continue

        explored.add(position)

        if grid[position[0]][position[1]] == b'G':
            return path + [position], explored, cost_so_far[position]

        neighbors, associated_cost = get_neighbors_with_cost(position, grid)

        for neighbor, action_cost in zip(neighbors, associated_cost):
            new_cost = cost_so_far[position] + action_cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                frontier.put((priority, neighbor, path + [position]))

    return None, explored, None
