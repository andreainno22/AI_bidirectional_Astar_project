import enum

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


class AstarGraphProblem:

    def __init__(self, initial, goal, graph, heuristic=None):
        """The constructor specifies the initial state, the goal
        state, the heuristic type and the graph."""
        self.initial = initial
        self.goal = goal
        self.heuristic = heuristic
        self.nodes = graph

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        actions = []
        if state[0] > 0 and self.nodes[state[0] - 1][state[1]] == 1:
            actions.append(Action.UP)
        if state[0] < len(self.nodes) - 1 and self.nodes[state[0] + 1][state[1]] == 1:
            actions.append(Action.DOWN)
        if state[1] > 0 and self.nodes[state[0]][state[1] - 1] == 1:
            actions.append(Action.LEFT)
        if state[1] < len(self.nodes[0]) - 1 and self.nodes[state[0]][state[1] + 1] == 1:
            actions.append(Action.RIGHT)
        if state[0] > 0 and state[1] > 0 and self.nodes[state[0] - 1][state[1] - 1] == 1:
            actions.append(Action.UP_LEFT)
        if state[0] > 0 and state[1] < len(self.nodes[0]) - 1 and self.nodes[state[0] - 1][state[1] + 1] == 1:
            actions.append(Action.UP_RIGHT)
        if state[0] < len(self.nodes) - 1 and state[1] > 0 and self.nodes[state[0] + 1][state[1] - 1] == 1:
            actions.append(Action.DOWN_LEFT)
        if state[0] < len(self.nodes) - 1 and state[1] < len(self.nodes[0]) - 1 and self.nodes[state[0] + 1][
            state[1] + 1] == 1:
            actions.append(Action.DOWN_RIGHT)
        return actions

    def result(self, node, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        if action == Action.UP:
            return node.state[0] - 1, node.state[1]
        elif action == Action.DOWN:
            return node.state[0] + 1, node.state[1]
        elif action == Action.LEFT:
            return node.state[0], node.state[1] - 1
        elif action == Action.RIGHT:
            return node.state[0], node.state[1] + 1
        elif action == Action.UP_LEFT:
            return node.state[0] - 1, node.state[1] - 1
        elif action == Action.UP_RIGHT:
            return node.state[0] - 1, node.state[1] + 1
        elif action == Action.DOWN_LEFT:
            return node.state[0] + 1, node.state[1] - 1
        elif action == Action.DOWN_RIGHT:
            return node.state[0] + 1, node.state[1] + 1

    def get_neighbors_bi(self, node):
        """Return the neighbors of the given state"""
        actions = self.actions(node.state)
        neighbors = []
        for action in actions:
            neighbor = Node(self.result(node, action), node, None, action)
            neighbor.set_path_cost(self.path_cost_bi(node.path_cost, node, action, neighbor))
            neighbor.set_effective_path_cost(self.effective_path_cost(node.effective_path_cost, action))
            neighbors.append(neighbor)
        return neighbors

    def get_neighbors_un(self, node):
        """Return the neighbors of the given state"""
        actions = self.actions(node.state)
        neighbors = []
        for action in actions:
            neighbor = Node(self.result(node, action), node, None, action)
            neighbor.set_path_cost(self.path_cost_un(node.path_cost, node, action, neighbor))
            neighbor.set_effective_path_cost(self.effective_path_cost(node.effective_path_cost, action))
            neighbors.append(neighbor)
        return neighbors

    def path_cost_bi(self, c, node1, action, node2):
        if action == Action.UP or action == Action.DOWN or action == Action.LEFT or action == Action.RIGHT:
            return c + 1 + 0.5 * (
                    self.h(node1, self.initial) - self.h(node1, self.goal) + self.h(node2, self.goal) - self.h(
                node2, self.initial))
        else:
            return c + 2 ** 0.5 + 0.5 * (
                    self.h(node1, self.initial) - self.h(node1, self.goal) + self.h(node2, self.goal) - self.h(
                node2, self.initial))

    def path_cost_un(self, c, node1, action, node2):
        if action == Action.UP or action == Action.DOWN or action == Action.LEFT or action == Action.RIGHT:
            return c + 1 + self.h(node2, self.goal) - self.h(node1, self.goal)
        else:
            return c + 2 ** 0.5 + self.h(node2, self.goal) - self.h(node1, self.goal)

    def effective_path_cost(self, c, action):
        """ Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1."""
        if action == Action.UP or action == Action.DOWN or action == Action.LEFT or action == Action.RIGHT:
            return c + 1
        else:
            return c + 2 ** 0.5

    def h(self, currentNode, goalNodeState):
        """ Calculate the function h"""
        if self.heuristic is None:
            return 0
        elif self.heuristic == "manhattan":
            return abs(currentNode.state[0] - goalNodeState[0]) + abs(currentNode.state[1] - goalNodeState[1])
        elif self.heuristic == "euclidean":
            return ((currentNode.state[0] - goalNodeState[0]) ** 2 + (
                    currentNode.state[1] - goalNodeState[1]) ** 2) ** 0.5
        return
