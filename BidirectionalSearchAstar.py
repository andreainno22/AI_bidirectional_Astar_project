# Bidirectional Search
from cmath import inf

from Node import Node
from queue import PriorityQueue

from PriorityList import PriorityList

finish = False


def bidirectional_search_Astar(problem, frontier_type="basic"):
    """si guarda solo il costo, non la funzione. il costo per passare da un nodo all'altro è cvw = cvw + 1/2(htv - hsv) + 1/2(hsw - htv)"""
    global finish
    finish = False
    nodeF = Node(problem.initial)
    nodeB = Node(problem.goal)
    if frontier_type == "heap":
        frontierF = PriorityQueue()
        frontierB = PriorityQueue()
    else:
        frontierF = PriorityList()
        frontierB = PriorityList()

    """i nodi di inizio e fine sono aggiunti alle rispettive code con priorità h(n) (hanno costo 0)"""
    hInitialNode = problem.h(nodeF, nodeB.state)
    hGoalNode = problem.h(nodeB, nodeF.state)
    frontierF.put((hInitialNode, nodeF))
    frontierB.put((hGoalNode, nodeB))

    """i nodi di inizio e fine sono aggiunti ai rispettivi dizionari di nodi raggiunti"""
    reachedF, reachedB = {nodeF.state: nodeF}, {nodeB.state: nodeB}
    solution = Node((None, None), None, None, 0, inf)
    n_iter = 0

    """ The algorithm terminates as soon as one of the searches is about to scan a node v with dv + hv ≥ C(P) or when Qs = Qt = ∅."""
    while not frontierF.empty() and not frontierB.empty() and finish is False:
        """ salva senza estrarre il nodo a più alta priorità da ciascuna frontiera """
        n_iter = n_iter + 1
        fStartNode, fEndNode = inf, inf
        if frontier_type == "heap":
            if not frontierF.empty():
                fStartNode, startNode = frontierF.queue[0]
            if not frontierB.empty():
                fEndNode, endNode = frontierB.queue[0]
        else:
            if not frontierF.is_empty():
                fStartNode, startNode = frontierF.first_element()
            if not frontierB.is_empty():
                fEndNode, endNode = frontierB.first_element()

        """sceglie quale nodo espandere in base alla priorità"""
        if fStartNode < fEndNode:
            solution = expand("F", problem, reachedF, reachedB, frontierF, solution)
        else:
            solution = expand("B", problem, reachedB, reachedF, frontierB, solution)
    if solution.state is None:
        return None

    path1 = Node.path(solution)
    solution.parent = solution.parent2
    path2 = Node.path(solution)
    path = path1 + path2[::-1]
    """il nodo solution è duplicato, viene rimosso"""
    path.remove(solution.state)
    return path, n_iter, solution.path_cost


def expand(direction, problem, reached1, reached2, frontier, solution):
    _, node = frontier.get()
    global finish
    if direction == "F":
        if node.depth + problem.h(node, problem.goal) >= solution.path_cost:
            finish = True
            return solution
    else:
        if node.depth + problem.h(node, problem.initial) >= solution.path_cost:
            finish = True
            return solution
    # Aggiorna i nodi vicini per il nodo di inizio
    for neighbor in problem.get_neighbors_bi(node):
        s = neighbor.state
        if s not in reached1 or neighbor.path_cost < reached1[s].path_cost:
            reached1[s] = neighbor
            """aggiunge il nodo espanso alla frontiera"""
            frontier.put((neighbor.path_cost, neighbor))
            if s in reached2:
                solution2: Node = merge_nodes(direction, neighbor, reached2[s])
                if solution is None or solution2.path_cost < solution.path_cost:
                    solution = solution2
    return solution


def merge_nodes(direction, node1, node2):
    if direction == "F":
        """per ricostruire il cammino si parte dal nodo soluzione"""
        return Node(node1.state, node1.parent, node2.parent, node1.action, node1.path_cost + node2.path_cost)
    else:
        return Node(node1.state, node2.parent, node1.parent, node2.action, node1.path_cost + node2.path_cost)
