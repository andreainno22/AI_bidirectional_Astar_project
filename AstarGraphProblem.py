import enum
from cmath import sqrt

from Node import Node
from enum import Enum


class Action(enum.Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    UP_LEFT = 5
    UP_RIGHT = 6
    DOWN_LEFT = 7
    DOWN_RIGHT = 8



    """def neighbors(self, node1, node2):
        # Questa è una semplice euristica che considera vicini i nodi adiacenti orizzontalmente o verticalmente.
        # Potrebbe essere necessario adattarla in base alle regole di movimento del tuo gioco.
        return abs(node1.state(0) - node2.state(1)) + abs(node1.state(0) - node2.state(1)) == 1 or (
                (node1.state(0) - node2.state(0)) ** 2 + (
                node1.state(1) - node2.state(1)) ** 2) ** 0.5 == 2 ** 0.5"""


class AstarGraphProblem:
    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal, graph, heuristic=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal
        self.heuristic = heuristic
        self.nodes = [[0 for i in range(len(graph))] for j in range(len(graph[0]))]
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] == '.':
                    self.nodes[i][j] = 1
                    # self.nodes.append(Node([i, j]))

        """potrei salvare la mappa in una matrice di tuple, dove ogni tupla è composta da (x,y)"""

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        actions = []
        if state(0) > 0 and self.nodes[state(0) - 1][state(1)] == 1:
            actions.append(Action.UP)
        if state(0) < len(self.nodes) - 1 and self.nodes[state(0) + 1][state(1)] == 1:
            actions.append(Action.DOWN)
        if state(1) > 0 and self.nodes[state(0)][state(1) - 1] == 1:
            actions.append(Action.LEFT)
        if state(1) < len(self.nodes[0]) - 1 and self.nodes[state(0)][state(1) + 1] == 1:
            actions.append(Action.RIGHT)
        if state(0) > 0 and state(1) > 0 and self.nodes[state(0) - 1][state(1) - 1] == 1:
            actions.append(Action.UP_LEFT)
        if state(0) > 0 and state(1) < len(self.nodes[0]) - 1 and self.nodes[state(0) - 1][state(1) + 1] == 1:
            actions.append(Action.UP_RIGHT)
        if state(0) < len(self.nodes) - 1 and state(1) > 0 and self.nodes[state(0) + 1][state(1) - 1] == 1:
            actions.append(Action.DOWN_LEFT)
        if state(0) < len(self.nodes) - 1 and state(1) < len(self.nodes[0]) - 1 and self.nodes[state(0) + 1][
            state(1) + 1] == 1:
            actions.append(Action.DOWN_RIGHT)
        return actions

    def result(self, node, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        if action == Action.UP:
            return (node.state(0) - 1, node.state(1))
        elif action == Action.DOWN:
            return [node.state(0) + 1, node.state(1)]
        elif action == Action.LEFT:
            return [node.state(0), node.state(1) - 1]
        elif action == Action.RIGHT:
            return [node.state(0), node.state(1) + 1]
        elif action == Action.UP_LEFT:
            return [node.state(0) - 1, node.state(1) - 1]
        elif action == Action.UP_RIGHT:
            return [node.state(0) - 1, node.state(1) + 1]
        elif action == Action.DOWN_LEFT:
            return [node.state(0) + 1, node.state(1) - 1]
        elif action == Action.DOWN_RIGHT:
            return [node.state(0) + 1, node.state(1) + 1]

    def get_neighbors(self, node):
        """Return the neighbors of the given state"""
        actions = self.actions(node.state)
        neighbors = []
        for action in actions:
            neighbor = Node(self.result(node, action), node, action)
            neighbor.set_path_cost(self.path_cost(node.path_cost, node, action, neighbor))
            neighbors.append(neighbor)
        """ rende una lista di stati adiacenti a quello di partenza"""
        return neighbors

    def path_cost(self, c, node1, action, node2):
        """Vogliamo il percorso di costo minore!!!
        Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2. If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        if action == Action.UP or action == Action.DOWN or action == Action.LEFT or action == Action.RIGHT:
            return c + 1 + 0.5 * (
                    self.h(node1, self.initial) - self.h(node1, self.goal) + self.h(node2, self.goal) - self.h(
                node2, self.initial))
        else:
            return c + sqrt(2) + 0.5 * (
                    self.h(node1, self.initial) - self.h(node1, self.goal) + self.h(node2, self.goal) - self.h(
                node2, self.initial))

    def h(self, currentNode, goalNode):
        if self.heuristic is None:
            return 0
        elif self.heuristic == "manhattan":
            return abs(currentNode.state(0) - goalNode.state(0)) + abs(currentNode.state(1) - goalNode.state(1))
        elif self.heuristic == "euclidean":
            return ((currentNode.state(0) - goalNode.state(0)) ** 2 + (
                    currentNode.state(1) - goalNode.state(1)) ** 2) ** 0.5
        return

