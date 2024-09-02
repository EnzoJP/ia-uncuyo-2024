from queue import PriorityQueue



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

def bfs_search(grid, start, goal):
    frontier = [(start, [])]  # (posición actual, camino tomado)
    explored = set()

    while frontier:
        position, path = frontier.pop(0)

        if position in explored:
            continue

        explored.add(position)

        if grid[position[0]][position[1]] == b'G':  # Llegamos al objetivo
            return path + [position],explored

        for neighbor in get_neighbors(position, grid):
            if neighbor not in explored and grid[neighbor[0]][neighbor[1]] != b'H':  # Evitar huecos
                frontier.append((neighbor, path + [position]))

    return None,explored  # Si no se encuentra el objetivo


def dls_search(grid, start, goal, limit):
    frontier = [(start, [], 0)]  # (posición actual, camino tomado, profundidad)
    explored = set()

    while frontier:
        position, path, depth = frontier.pop()

        if position in explored:
            continue

        explored.add(position)

        if depth > limit:
            continue

        if grid[position[0]][position[1]] == b'G':  # Llegamos al objetivo
            return path + [position], explored

        if depth < limit:
            for neighbor in get_neighbors(position, grid):
                if neighbor not in explored and grid[neighbor[0]][neighbor[1]] != b'H':  # Evitar huecos
                    frontier.append((neighbor, path + [position], depth + 1))

    return None, explored  # Si no se encuentra el objetivo


def dfs_search(grid, start, goal): 
    frontier = [(start, [])]  # ( posición actual, camino tomado)
    explored = set()

    while frontier:
        position, path = frontier.pop()

        if position in explored:
            continue

        explored.add(position)

        if grid[position[0]][position[1]] == b'G':  # Llegamos al objetivo
            return path + [position], explored

        for neighbor in get_neighbors(position, grid):
            if neighbor not in explored and grid[neighbor[0]][neighbor[1]] != b'H':  # Evitar huecos
                frontier.append((neighbor, path + [position]))

    return None, explored  # Si no se encuentra el objetivo


def ucs_search_1(grid, start, goal): #las acciones tiene costo 1
    # (costo,posición actual, camino tomado)
    frontier=PriorityQueue()
    frontier.put((0,start,[]))
    explored = set()
    frontier_nodes=set()

    while frontier:
        cost,position, path = frontier.get()

        if position in explored:
            continue

        explored.add(position)

        if grid[position[0]][position[1]] == b'G':  # Llegamos al objetivo
            return path + [position],explored, len(path)+1
        
        neighbors= get_neighbors(position, grid)

        for neighbor in neighbors:
            if neighbor not in explored and grid[neighbor[0]][neighbor[1]] != b'H':  # Evitar huecos
                frontier.put((1,neighbor, path + [position]))
                frontier_nodes.add(neighbor)
            # Si el vecino ya está en la frontera con un costo mayor, lo reemplazamos
            elif neighbor in frontier_nodes == True and cost < frontier.get(neighbor)[0] and grid[neighbor[0]][neighbor[1]] != b'H':
                frontier.put((cost,neighbor,path + [position]))
                frontier_nodes.add(neighbor)
    
    return None,explored,None  # Si no se encuentra el objetivoo



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



def ucs_search_2(grid, start, goal):
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

        neighbors, associated_cost = get_neighbors_with_cost(position, grid)

        for neighbor, action_cost in zip(neighbors, associated_cost):
            new_cost = cost_so_far[position] + action_cost
            if neighbor not in explored or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                frontier.put((new_cost, neighbor, path + [position]))

    return None, explored, None


