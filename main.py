# This is a sample Python script.
from AstarGraphProblem import AstarGraphProblem
from BidirectionalSearchAstar import *

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    graph = [['@', '.', '.', '.', '.'],
             ['@', '.', '.', 'T', '.'],
             ['.', '.', '.', '.', '.'],
             ['.', 'b', '.', '.', '.'],
             ['c', '.', '.', '.', 'd']]
    problem = AstarGraphProblem((0, 1), (4, 3), graph)
    print(bidirectional_search(problem))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
