# Bidirectional Search
# Pseudocode from https://webdocs.cs.ualberta.ca/%7Eholte/Publications/MM-AAAI2016.pdf
from cmath import inf

from Node import Node
from queue import PriorityQueue

finish = False
no_solution = False

def bidirectional_search(problem):
    """si guarda solo il costo, non la funzione. il costo per passare da un nodo all'altro è cvw = cvw + 1/2(htv - hsv) + 1/2(hsw - htv)"""
    global finish
    global no_solution
    finish = False
    no_solution = False
    nodeF = Node(problem.initial)
    nodeB = Node(problem.goal)
    frontierF = PriorityQueue()
    frontierB = PriorityQueue()

    """i nodi di inizio e fine sono aggiunti alle rispettive code con priorità h(n) (hanno costo 0)"""
    hInitialNode = problem.h(nodeF, nodeB.state)
    hGoalNode = problem.h(nodeB, nodeF.state)
    frontierF.put((hInitialNode, nodeF))
    frontierB.put((hGoalNode, nodeB))

    """i nodi di inizio e fine sono aggiunti ai rispettivi dizionari di nodi raggiunti"""
    reachedF, reachedB = {nodeF.state: nodeF}, {nodeB.state: nodeB}
    solution = Node((None, None), None, None, 0, inf)

    while not frontierF.empty() and not frontierB.empty() and finish is False and no_solution is False:
        """ The algorithm terminates as soon as one of the searches is about to scan a node v with dv + hv ≥ C(P) or when Qs = Qt = ∅."""
        # Estrai il nodo con il costo f minore da ciascuna coda
        hStartNode, startNode = frontierF.queue[0]
        hEndNode, endNode = frontierB.queue[0]
        if hStartNode < hEndNode:
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
    path.remove(solution)
    return path


def expand(direction, problem, reached1, reached2, frontier, solution):
    _, node = frontier.get()
    global finish
    if direction == "F":
        if node.path_cost + problem.h(node, problem.goal) >= solution.path_cost:
            finish = True
            return solution
    else:
        if node.path_cost + problem.h(node, problem.initial) >= solution.path_cost:
            finish = True
            return solution
    # Aggiorna i nodi vicini per il nodo di inizio
    for neighbor in problem.get_neighbors(node):
        s = neighbor.state
        if s not in reached1 or neighbor.path_cost < reached1[s].path_cost:
            reached1[s] = neighbor
            """aggiunge il nodo espanso alla frontiera"""
            frontier.put((problem.path_cost(node.path_cost, node, neighbor.action, neighbor), neighbor))
            if s in reached2:
                solution2: Node = merge_nodes(direction, neighbor, reached2[s])
                if solution is None or solution2.path_cost < solution.path_cost:
                    solution = solution2
    if solution.state is None:
        global no_solution
        no_solution = True
        return
    return solution


def merge_nodes(direction, node1, node2):
    if direction == "F":
        """per ricostruire il cammino si parte dal nodo soluzione """
        return Node(node1.state, node1.parent, node2.parent, node1.action, node1.path_cost + node2.path_cost)
    else:
        return Node(node1.state, node2.parent, node1.parent, node2.action, node1.path_cost + node2.path_cost)
