# Bidirectional Search
# Pseudocode from https://webdocs.cs.ualberta.ca/%7Eholte/Publications/MM-AAAI2016.pdf
from AstarGraphProblem import AstarGraphProblem
from Node import Node
from queue import PriorityQueue

finish = False


def bidirectional_search(problem):
    """si guarda solo il costo, non la funzione. il costo per passare da un nodo all'altro è cvw = cvw + 1/2(htv - hsv) + 1/2(hsw - htv)"""
    nodeF = Node(problem.initial)
    nodeB = Node(problem.goal)
    frontierF = PriorityQueue()
    frontierB = PriorityQueue()

    """i nodi di inizio e fine sono aggiunti alle rispettive code con priorità h(n) (hanno costo 0)"""
    frontierF.put((problem.h(nodeF, nodeB), nodeF))
    frontierB.put((problem.h(nodeB, nodeF), nodeB))

    """i nodi di inizio e fine sono aggiunti ai rispettivi dizionari di nodi raggiunti"""
    reachedF, reachedB = {nodeF.state: nodeF}, {nodeB.state: nodeB}
    solution = None

    while not frontierF.empty() and not frontierB.empty() or finish is False:
        """ The algorithm terminates as soon as one of the searches is about to scan a node v with dv + hv ≥ C(P) or when Qs = Qt = ∅."""
        # Estrai il nodo con il costo f minore da ciascuna coda
        hStartNode, startNode = frontierF.queue[0]
        hEndNode, endNode = frontierB.queue[0]
        if hStartNode < hEndNode:
            solution = expand("F", problem, reachedF, reachedB, frontierF, solution)
        else:
            solution = expand("B", problem, reachedB, reachedF, frontierB, solution)

    return solution


def expand(direction, problem, reached1, reached2, frontier, solution):
    node = frontier.get()
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
            frontier.put(neighbor)
            if s in reached2:
                solution2 = merge_nodes(direction, neighbor, reached2[s])
                if solution is None or solution2.path_cost < solution.path_cost:
                    solution = solution2
    return solution


def merge_nodes(direction, node1, node2):
    if direction == "F":
        """per ricostruire il cammino si parte dal nodo soluzione """
        return Node(node1.state, node1.path_cost + node2.path_cost, node1.parent, node2.parent)
    else:
        return Node(node1.state, node1.path_cost + node2.path_cost, node2.parent, node1.parent)
