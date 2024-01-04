# Bidirectional Search
# Pseudocode from https://webdocs.cs.ualberta.ca/%7Eholte/Publications/MM-AAAI2016.pdf
from AstarGraphProblem import AstarGraphProblem
from Node import Node


def bidirectional_search(problem):
    e = 0
    if isinstance(problem, AstarGraphProblem):
        e = problem.find_min_edge()

        """gF = cost of getting from initial state to n, gB = cost of getting from goal state to n """
    gF, gB = {Node(problem.initial): 0}, {Node(problem.goal): 0}
    frontierF, frontierB = [Node(problem.initial)], [Node(problem.goal)]
    reachedF, reachedB = [], []
    U = np.inf

    def extend(U, frontier_dir, frontier_other, g_dir, g_other, closed_dir):
        """Extend search in given direction"""
        n = find_key(C, frontier_dir, g_dir)

        frontier_dir.remove(n)
        closed_dir.append(n)

        for c in n.expand(problem):
            if c in frontier_dir or c in closed_dir:
                if g_dir[c] <= problem.path_cost(g_dir[n], n.state, None, c.state):
                    continue

                frontier_dir.remove(c)

            g_dir[c] = problem.path_cost(g_dir[n], n.state, None, c.state)
            frontier_dir.append(c)

            if c in frontier_other:
                U = min(U, g_dir[c] + g_other[c])

        return U, frontier_dir, closed_dir, g_dir

    def find_min(open_dir, g):
        """Finds minimum priority, g and f values in open_dir"""
        # pr_min_f isn't forward pr_min instead it's the f-value
        # of node with priority pr_min.
        pr_min, pr_min_f = np.inf, np.inf
        for n in open_dir:
            f = g[n] + problem.heuristic(n)
            pr = max(f, 2 * g[n])
            pr_min = min(pr_min, pr)
            pr_min_f = min(pr_min_f, f)

        return pr_min, pr_min_f, min(g.values())

    def find_key(pr_min, open_dir, g):
        """Finds key in open_dir with value equal to pr_min
        and minimum g value."""
        m = np.inf
        node = Node(-1)
        for n in open_dir:
            pr = max(g[n] + problem.heuristic(n), 2 * g[n])
            if pr == pr_min:
                if g[n] < m:
                    m = g[n]
                    node = n

        return node

    while frontierF and frontierB:
        pr_min_f, f_min_f, g_min_f = find_min(frontierF, gF)
        pr_min_b, f_min_b, g_min_b = find_min(frontierB, gB)
        C = min(pr_min_f, pr_min_b)

        if U <= max(C, f_min_f, f_min_b, g_min_f + g_min_b + e):
            return U

        if C == pr_min_f:
            # Extend forward
            U, frontierF, reachedF, gF = extend(U, frontierF, frontierB, gF, gB, reachedF)
        else:
            # Extend backward
            U, frontierB, reachedB, gB = extend(U, frontierB, frontierF, gB, gF, reachedB)

    return np.inf