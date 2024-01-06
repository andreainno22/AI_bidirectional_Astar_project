# This is a sample Python script.
from cmath import sqrt

from AstarGraphProblem import AstarGraphProblem
from queue import PriorityQueue
from BidirectionalSearchAstar import *
from timeit import default_timer as timer

from StringToMatrix import get_map


# todo: per percorsilunghi a volte l'alg termina senza che i due raggiunti si incontrino, anche se il persorso esiste

def main():
    battleground_map = get_map('maps/battleground/battleground.map', 1, 512, 512)
    AR0011SR_map = get_map('maps/AR0011SR/AR0011SR.map', 1, 224, 216)

    # battleground_heap_no_heuristic_problem
    """timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((376, 101), (193, 331), battleground_map), "heap")
    timer_end = timer()
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start)

    #battleground_heap_euclidean_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((376, 101), (193, 331), battleground_map, "euclidean"),
                                             "heap")
    timer_end = timer()
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start)

    #battleground_heap_manhattan_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((376, 101), (193, 331), battleground_map, "manhattan"),
                                             "heap")
    timer_end = timer()
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start)

    #battleground_basic_no_heuristic_problem 
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((376, 101), (193, 331), battleground_map), "basic")
    timer_end = timer()
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start)

    #battleground_basic_euclidean_problem 
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((376, 101), (193, 331), battleground_map, "euclidean"),
                                             "basic")
    timer_end = timer()
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start)

    #battleground_basic_manhattan_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((376, 101), (193, 331), battleground_map, "manhattan"),
                                             "basic")
    timer_end = timer()
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start)"""

    """AR0011SR_heap_no_heuristic_problem"""
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((100, 41), (138, 41), AR0011SR_map), "heap")
    timer_end = timer()
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start)

    """#battleground_heap_euclidean_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((131,216),(131,214), AR0011SR_map, "euclidean"),
                                             "heap")
    timer_end = timer()
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start)

    #battleground_heap_manhattan_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((131,216),(131,214), AR0011SR_map, "manhattan"),
                                             "heap")
    timer_end = timer()
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start)

    #battleground_basic_no_heuristic_problem 
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((131,216),(131,214), AR0011SR_map), "basic")
    timer_end = timer()
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start)

    #battleground_basic_euclidean_problem 
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((131,216),(131,214), AR0011SR_map, "euclidean"),
                                             "basic")
    timer_end = timer()
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start)

    #battleground_basic_manhattan_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((131,216),(131,214), AR0011SR_map, "manhattan"),
                                             "basic")
    timer_end = timer()
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start)"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
