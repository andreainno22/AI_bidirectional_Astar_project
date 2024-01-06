# This is a sample Python script.
from cmath import sqrt

from AstarGraphProblem import AstarGraphProblem
from queue import PriorityQueue
from BidirectionalSearchAstar import *
from timeit import default_timer as timer

from StringToMatrix import get_map


# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# todo: implementare coda con priorità non con heap binario
# todo: aggiungere terzo grafo

def main():
    battleground_map = get_map('maps/plainsofsnow/plainsofsnow.map', 1, 512, 512)

    # game_map2 = get_map('arena.map', 5, 49, 49)
    problem = AstarGraphProblem((290, 359), (261, 351), battleground_map)
    timer_start = timer()
    result_path = bidirectional_search_Astar(problem, "")
    timer_end = timer()
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start)

    problem1 = AstarGraphProblem((290, 359), (261, 351), battleground_map)
    timer_start1 = timer()
    result_path1 = bidirectional_search_Astar(problem1, "heap")
    timer_end1 = timer()
    print(result_path1)
    print("Time elapsed: ", timer_end1 - timer_start1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
