# Bidirectional Search
from cmath import inf

from Node import Node
from queue import PriorityQueue

from PriorityList import PriorityList


class BidirectionalSearchAstar:
    def __init__(self):
        self.finish = False
        self.first_solution = None
        self.n_iter_first_solution = 0
        self.no_solution = True
        self.n_iter = 0

    def bidirectional_search_Astar(self, problem, frontier_type="basic"):
        """si guarda solo il costo, non la funzione. il costo per passare da un nodo all'altro è cvw = cvw + 1/2(htv - hsv) + 1/2(hsw - htv)"""
        nodeF = Node(problem.initial)
        nodeB = Node(problem.goal)
        if frontier_type == "heap":
            frontierF = PriorityQueue()
            frontierB = PriorityQueue()
        else:
            frontierF = PriorityList()
            frontierB = PriorityList()

        """i nodi di inizio e fine sono aggiunti alle rispettive code con priorità h(n) (hanno costo 0)"""
        frontierF.put((problem.h(nodeF, nodeB.state), nodeF))
        frontierB.put((problem.h(nodeB, nodeF.state), nodeB))

        """i nodi di inizio e fine sono aggiunti ai rispettivi dizionari di nodi raggiunti"""
        reachedF, reachedB = {nodeF.state: nodeF}, {nodeB.state: nodeB}
        solution = Node((None, None), None, None, 0, inf, inf)
        self.first_solution = solution

        """ The algorithm terminates as soon as one of the searches is about to scan a node v with dv + hv ≥ C(P) or when Qs = Qt = ∅."""
        while not frontierF.empty() or not frontierB.empty() and self.finish is False:
            """ salva senza estrarre il nodo a più alta priorità da ciascuna frontiera """
            self.n_iter = self.n_iter + 1
            fStartNode, fEndNode = inf, inf
            if frontier_type == "heap":
                if not frontierF.empty():
                    fStartNode, startNode = frontierF.queue[0]
                if not frontierB.empty():
                    fEndNode, endNode = frontierB.queue[0]
            else:
                if not frontierF.empty():
                    fStartNode, startNode = frontierF.first_element()
                if not frontierB.empty():
                    fEndNode, endNode = frontierB.first_element()

            """sceglie quale nodo espandere in base alla priorità"""
            if fStartNode < fEndNode:
                solution = self.expand("F", problem, reachedF, reachedB, frontierF, solution)
            else:
                solution = self.expand("B", problem, reachedB, reachedF, frontierB, solution)
        if solution.state is None:
            return None

        path1 = Node.path(solution)
        solution.parent = solution.parent2
        path2 = Node.path(solution)
        path = path1 + path2[::-1]
        """il nodo solution è duplicato, viene rimosso"""
        path.remove(solution.state)

        path_first_solution1 = Node.path(self.first_solution)
        self.first_solution.parent = self.first_solution.parent2
        path_first_solution2 = Node.path(self.first_solution)
        path_first_solution = path_first_solution1 + path_first_solution2[::-1]
        path_first_solution.remove(self.first_solution.state)
        return (path, self.n_iter, solution.effective_path_cost), (
            path_first_solution, self.n_iter_first_solution, self.first_solution.effective_path_cost)

    def expand(self, direction, problem, reached1, reached2, frontier, solution):
        _, node = frontier.get()
        if direction == "F":
            if node.depth + problem.h(node, problem.goal) >= solution.path_cost:
                self.finish = True
                return solution
        else:
            if node.depth + problem.h(node, problem.initial) >= solution.path_cost:
                self.finish = True
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
                    if self.no_solution is True:
                        self.first_solution = solution2
                        self.no_solution = not self.no_solution
                        self.n_iter_first_solution = self.n_iter
                    if solution2.effective_path_cost < solution.effective_path_cost:
                        solution = solution2

        return solution


def merge_nodes(direction, node1, node2):
    if direction == "F":
        """per ricostruire il cammino si parte dal nodo soluzione"""
        return Node(node1.state, node1.parent, node2.parent, node1.action, node1.path_cost + node2.path_cost,
                    node1.effective_path_cost + node2.effective_path_cost)
    else:
        return Node(node1.state, node2.parent, node1.parent, node2.action, node1.path_cost + node2.path_cost,
                    node1.effective_path_cost + node2.effective_path_cost)
