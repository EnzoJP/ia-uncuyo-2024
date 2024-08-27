from node import Node

class Searches:
    
    def breadth_first_search(env, start_state, goal_state):

        root = Node(state=start_state)
        frontier = [root]
        explored = set()  

        while frontier:
            node = frontier.pop(0)

            if node.state == goal_state:
                return node,explored  

            explored.add(node.state)  # Marcamos este estado como explorado

            # Expandimos los nodos hijos
            for action in range(env.action_space.n):
                next_state, _, done, truncated, _ = env.step(action)  # Aplicamos la acción

                # Evitar repetir estados y añadir a la frontera
                if next_state not in explored and not done and not truncated:
                    child_node = Node(state=next_state, parent=node, action=action)
                    node.add_child(child_node)
                    frontier.append(child_node)
                    
                    # Verificar si alcanzamos el objetivo
                    if next_state == goal_state:
                        return child_node,explored

        return None,explored  # Si la frontera se vacía y no encontramos el objetivo

    def depth_first_search(env, start_state, goal_state):
        root = Node(state=start_state)
        frontier = [root]  # (LIFO)
        explored = set()   

        while frontier:
            node = frontier.pop()  # Sacamos el último nodo de la frontera

            if node.state == goal_state:
                return node, explored 

            explored.add(node.state) 

            # Expandimos los nodos hijos aplicando las acciones disponibles
            for action in range(env.action_space.n):
                next_state, _, done, truncated, _ = env.step(action)  # Aplicamos la acción

                if next_state not in explored and not done and not truncated:
                    child_node = Node(state=next_state, parent=node, action=action)
                    node.add_child(child_node)
                    frontier.append(child_node)  
                    
                    if next_state == goal_state:
                        return child_node, explored 

        return None, explored  # Si la frontera se vacía y no encontramos el objetivo

    def limited_dfs (env, start_state, goal_state, limit):
        root = Node(state=start_state)
        frontier = [(root, 0)]  # Pila con nodos y su nivel de profundidad
        explored = set() 

        while frontier:
            node, depth = frontier.pop()  # Sacamos el último nodo de la pila

            if node.state == goal_state:
                return node, explored  # Retornamos el nodo objetivo

            if depth < limit:
                explored.add(node.state)  # Marcamos este estado como explorado

                # Expandimos los nodos hijos aplicando las acciones disponibles
                for action in range(env.action_space.n):
                    next_state, _, done, truncated, _ = env.step(action)

                    if next_state not in explored and not done and not truncated:
                        child_node = Node(state=next_state, parent=node, action=action)
                        node.add_child(child_node)
                        frontier.append((child_node, depth + 1))  # Añadimos el hijo a la pila con su nueva profundidad

        return None, explored  # Si la frontera se vacía y no encontramos el objetivo



    def uniform_cost_search (env, start_state, goal_state):
            pass
    

    

