# This is a sample Python script.
from cmath import sqrt
from turtledemo.chaos import plot

from AstarGraphProblem import AstarGraphProblem
from queue import PriorityQueue
from BidirectionalSearchAstar import *
from timeit import default_timer as timer
import matplotlib.pyplot as plt

from StringToMatrix import get_map
from UnidirectionalSearchAstar import unidirectional_search_Astar


# todo: viene data una soluzione con costo subottimo a volte....perchè?

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
    result_path = bidirectional_search_Astar(AstarGraphProblem((76, 93), (162, 54), AR0011SR_map), "heap")
    timer_end = timer()
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start)

    # Supponiamo che il tuo percorso sia qualcosa del genere
    path = result_path[0]
    # Dividiamo le tuple in due liste separate per le coordinate x e y
    x = [coord[0] for coord in path]
    y = [coord[1] for coord in path]

    # Creiamo il grafico
    plt.plot(x, y)

    # Mostriamo il grafico
    plt.show()

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
