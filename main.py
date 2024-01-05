# This is a sample Python script.
from cmath import sqrt

from AstarGraphProblem import AstarGraphProblem
from queue import PriorityQueue
from BidirectionalSearchAstar import *
from timeit import default_timer as timer


# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    graph = [['@', '.', '.', '.', '.'],
             ['@', '.', '.', 'T', '.'],
             ['.', '.', 'T', 't', '.'],
             ['.', 'b', 't', '.', '.'],
             ['c', 'y', '.', '.', 'd']]
    problem = AstarGraphProblem((0, 1), (4, 3), graph)
    timer_start = timer()
    result_path = bidirectional_search(problem)
    timer_end = timer()
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start)

    problem1 = AstarGraphProblem((0, 1), (4, 3), graph, 'manhattan')
    timer_start1 = timer()
    result_path1 = bidirectional_search(problem1)
    timer_end1 = timer()
    print(result_path1)
    print("Time elapsed: ", timer_end1 - timer_start1)
    # print(2**0.5)

    """queue = PriorityQueue()
    queue.put((1, Node((0, 1), None, None, 0, 0)))
    queue.put((2, Node((0, 1), None, None, 0, 0)))
    c, d = queue.queue[0]

    print(d)"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
