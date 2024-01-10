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


# è stata usata l'euristica di chebyshev al posto di manhattan perchè l'agente può muoversi anche in diagonale
# todo: unidir è più veloce di bidir, perchè??

def main():
    battleground_map = get_map('maps/battleground/battleground.map', 1, 512, 512)
    AR0011SR_map = get_map('maps/AR0011SR/AR0011SR.map', 1, 224, 216)
    plainsofsnow_map = get_map('maps/plainsofsnow/plainsofsnow.map', 1, 512, 512)

    # battleground_heap_no_heuristic_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((339, 67), (133, 399), battleground_map), "heap")
    timer_end = timer()
    print("battleground_heap_no_heuristic_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_heap_euclidean_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((418, 250), (451, 277), battleground_map, "euclidean"),
                                             "heap")
    timer_end = timer()
    print("battleground_heap_euclidean_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_heap_chebyshev_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((418, 250), (451, 277), battleground_map, "chebyshev"),
                                             "heap")
    timer_end = timer()
    print("battleground_heap_chebyshev_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_basic_no_heuristic_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((418, 250), (451, 277), battleground_map), "basic")
    timer_end = timer()
    print("battleground_basic_no_heuristic_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_basic_euclidean_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((418, 250), (451, 277), battleground_map, "euclidean"),
                                             "basic")
    timer_end = timer()
    print("battleground_basic_euclidean_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_basic_chebyshev_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((418, 250), (451, 277), battleground_map, "chebyshev"),
                                             "basic")
    timer_end = timer()
    print("battleground_basic_chebyshev_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_heap_no_heuristic_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((339, 67), (133, 399), battleground_map),
                                              "heap")
    timer_end = timer()
    print("battleground_heap_no_heuristic_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_heap_euclidean_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((418, 250), (451, 277), battleground_map, "euclidean"),
                                              "heap")
    timer_end = timer()
    print("battleground_heap_euclidean_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_heap_chebyshev_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((418, 250), (451, 277), battleground_map, "chebyshev"),
                                              "heap")
    timer_end = timer()
    print("battleground_heap_chebyshev_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_basic_no_heuristic_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((418, 250), (451, 277), battleground_map), "basic")
    timer_end = timer()
    print("battleground_basic_no_heuristic_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_basic_euclidean_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((418, 250), (451, 277), battleground_map, "euclidean"),
                                              "basic")
    timer_end = timer()
    print("battleground_basic_euclidean_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_basic_chebyshev_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((418, 250), (451, 277), battleground_map, "chebyshev"),
                                              "basic")
    timer_end = timer()
    print("battleground_basic_chebyshev_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    """A0011SR map"""
    # AR0011SR_heap_no_heuristic_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((201, 122), (175, 167), AR0011SR_map), "heap")
    timer_end = timer()
    print("AR0011SR_heap_no_heuristic_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR_heap_euclidean_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((201, 122), (175, 167), AR0011SR_map, "euclidean"),
                                             "heap")
    timer_end = timer()
    print("A0011SR_heap_euclidean_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR_heap_chebyshev_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((201, 122), (175, 167), AR0011SR_map, "chebyshev"),
                                             "heap")
    timer_end = timer()
    print("A0011SR_heap_chebyshev_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR_basic_no_heuristic_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((201, 122), (175, 167), AR0011SR_map), "basic")
    timer_end = timer()
    print("A0011SR_basic_no_heuristic_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR_basic_euclidean_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((201, 122), (175, 167), AR0011SR_map, "euclidean"),
                                             "basic")
    timer_end = timer()
    print("A0011SR_basic_euclidean_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR_basic_chebyshev_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((201, 122), (175, 167), AR0011SR_map, "chebyshev"),
                                             "basic")
    timer_end = timer()
    print("A0011SR_basic_chebyshev_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # AR0011SR_heap_no_heuristic_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((201, 122), (175, 167), AR0011SR_map), "heap")
    timer_end = timer()
    print("AR0011SR_heap_no_heuristic_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR_heap_euclidean_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((201, 122), (175, 167), AR0011SR_map, "euclidean"),
                                              "heap")
    timer_end = timer()
    print("A0011SR_heap_euclidean_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR_heap_chebyshev_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((201, 122), (175, 167), AR0011SR_map, "chebyshev"),
                                              "heap")
    timer_end = timer()
    print("A0011SR_heap_chebyshev_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR_basic_no_heuristic_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((201, 122), (175, 167), AR0011SR_map), "basic")
    timer_end = timer()
    print("A0011SR_basic_no_heuristic_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR_basic_euclidean_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((201, 122), (175, 167), AR0011SR_map, "euclidean"),
                                              "basic")
    timer_end = timer()
    print("A0011SR_basic_euclidean_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR_basic_chebyshev_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((201, 122), (175, 167), AR0011SR_map, "chebyshev"),
                                              "basic")
    timer_end = timer()
    print("A0011SR_basic_chebyshev_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    """plainsofsnow map"""
    # plainsofsnow_heap_no_heuristic_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map), "heap")
    timer_end = timer()
    print("plainsofsnow_heap_no_heuristic_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_heap_euclidean_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map, "euclidean"),
                                             "heap")
    timer_end = timer()
    print("plainsofsnow_heap_euclidean_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_heap_chebyshev_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map, "chebyshev"),
                                             "heap")
    timer_end = timer()
    print("plainsofsnow_heap_chebyshev_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_basic_no_heuristic_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map), "basic")
    timer_end = timer()
    print("plainsofsnow_basic_no_heuristic_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_basic_euclidean_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map, "euclidean"),
                                             "basic")
    timer_end = timer()
    print("plainsofsnow_basic_euclidean_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_basic_chebyshev_problem
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map, "chebyshev"),
                                             "basic")
    timer_end = timer()
    print("plainsofsnow_basic_chebyshev_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_heap_no_heuristic_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map), "heap")
    timer_end = timer()
    print("plainsofsnow_heap_no_heuristic_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_heap_euclidean_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map, "euclidean"),
                                              "heap")
    timer_end = timer()
    print("plainsofsnow_heap_euclidean_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_heap_chebyshev_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map, "chebyshev"),
                                              "heap")
    timer_end = timer()
    print("plainsofsnow_heap_chebyshev_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_basic_no_heuristic_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map), "basic")
    timer_end = timer()
    print("plainsofsnow_basic_no_heuristic_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_basic_euclidean_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map, "euclidean"),
                                              "basic")
    timer_end = timer()
    print("plainsofsnow_basic_euclidean_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_basic_chebyshev_problem unidirectional
    timer_start = timer()
    result_path = bidirectional_search_Astar(AstarGraphProblem((339, 67), (133, 399), battleground_map),
                                             "heap")
    timer_end = timer()
    print("plainsofsnow_basic_chebyshev_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # Supponiamo che il tuo percorso sia qualcosa del genere
    path = result_path[0]
    # Dividiamo le tuple in due liste separate per le coordinate x e y
    x = [coord[0] for coord in path]
    y = [coord[1] for coord in path]

    # Creiamo il grafico
    plt.plot(x, y)

    # Mostriamo il grafico
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
