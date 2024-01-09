# Bidirectional Search
from cmath import inf

from Node import Node
from queue import PriorityQueue

from PriorityList import PriorityList

finish = False


def unidirectional_search_Astar(problem, frontier_type="basic"):
    """si guarda solo il costo, non la funzione. il costo per passare da un nodo all'altro è cvw = cvw + 1/2(htv - hsv) + 1/2(hsw - htv)"""
    nodeF = Node(problem.initial)
    nodeB = Node(problem.goal)
    if frontier_type == "heap":
        frontierF = PriorityQueue()
    else:
        frontierF = PriorityList()

    """i nodi di inizio e fine sono aggiunti alle rispettive code con priorità h(n) (hanno costo 0)"""
    hInitialNode = problem.h(nodeF, nodeB.state)
    frontierF.put((hInitialNode, nodeF))

    """i nodi di inizio e fine sono aggiunti ai rispettivi dizionari di nodi raggiunti"""
    reachedF = {nodeF.state: nodeF}
    n_iter = 0

    """ The algorithm terminates as soon as one of the searches is about to scan a node v with dv + hv ≥ C(P) or when Qs = Qt = ∅."""
    while not frontierF.empty() and finish is False:
        """ salva senza estrarre il nodo a più alta priorità da ciascuna frontiera """
        n_iter = n_iter + 1
        _, node = frontierF.get()
        if node.state == problem.goal:
            path = Node.path(node)
            return path, n_iter, node.path_cost

        # Aggiorna i nodi vicini per il nodo di inizio
        for neighbor in problem.get_neighbors_bi(node):
            s = neighbor.state
            if s not in reachedF or neighbor.path_cost < reachedF[s].path_cost:
                reachedF[s] = neighbor
            """aggiunge il nodo espanso alla frontiera"""
            frontierF.put((problem.path_cost_bi(node.path_cost, node, neighbor.action, neighbor), neighbor))
    return
