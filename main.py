# This is a sample Python script.

from AstarGraphProblem import AstarGraphProblem
from BidirectionalSearchAstar import *
from timeit import default_timer as timer

from StringToMatrix import get_map
from UnidirectionalSearchAstar import unidirectional_search_Astar


def main():
    battleground_map = get_map('maps/battleground/battleground.map', 5, 512, 512)
    AR0011SR_map = get_map('maps/AR0011SR/AR0011SR.map', 5, 224, 216)
    plainsofsnow_map = get_map('maps/plainsofsnow/plainsofsnow.map', 5, 512, 512)

    # battleground_heap_no_heuristic_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((418, 250), (451, 277), battleground_map), "heap")
    timer_end = timer()
    print("battleground_heap_no_heuristic_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_heap_euclidean_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((418, 250), (451, 277), battleground_map, "euclidean"),
        "heap")
    timer_end = timer()
    print("battleground_heap_euclidean_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_heap_manhattan_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((418, 250), (451, 277), battleground_map, "manhattan"),
        "heap")
    timer_end = timer()
    print("battleground_heap_manhattan_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_basic_no_heuristic_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((418, 250), (451, 277), battleground_map), "basic")
    timer_end = timer()
    print("battleground_basic_no_heuristic_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_basic_euclidean_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((418, 250), (451, 277), battleground_map, "euclidean"),
        "basic")
    timer_end = timer()
    print("battleground_basic_euclidean_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_basic_manhattan_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((418, 250), (451, 277), battleground_map, "manhattan"),
        "basic")
    timer_end = timer()
    print("battleground_basic_manhattan_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # battleground_heap_no_heuristic_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((418, 250), (451, 277), battleground_map),
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

    # battleground_heap_manhattan_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((418, 250), (451, 277), battleground_map, "manhattan"),
                                              "heap")
    timer_end = timer()
    print("battleground_heap_manhattan_problem unidirectional")
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

    # battleground_basic_manhattan_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((418, 250), (451, 277), battleground_map, "manhattan"),
                                              "basic")
    timer_end = timer()
    print("battleground_basic_manhattan_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR map
    # AR0011SR_heap_no_heuristic_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((201, 122), (175, 167), AR0011SR_map), "heap")
    timer_end = timer()
    print("AR0011SR_heap_no_heuristic_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR_heap_euclidean_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((201, 122), (175, 167), AR0011SR_map, "euclidean"),
        "heap")
    timer_end = timer()
    print("A0011SR_heap_euclidean_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR_heap_manhattan_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((201, 122), (175, 167), AR0011SR_map, "manhattan"),
        "heap")
    timer_end = timer()
    print("A0011SR_heap_manhattan_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR_basic_no_heuristic_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((201, 122), (175, 167), AR0011SR_map), "basic")
    timer_end = timer()
    print("A0011SR_basic_no_heuristic_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR_basic_euclidean_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((201, 122), (175, 167), AR0011SR_map, "euclidean"),
        "basic")
    timer_end = timer()
    print("A0011SR_basic_euclidean_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # A0011SR_basic_manhattan_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((201, 122), (175, 167), AR0011SR_map, "manhattan"),
        "basic")
    timer_end = timer()
    print("A0011SR_basic_manhattan_problem")
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

    # A0011SR_heap_manhattan_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((201, 122), (175, 167), AR0011SR_map, "manhattan"),
                                              "heap")
    timer_end = timer()
    print("A0011SR_heap_manhattan_problem unidirectional")
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

    # A0011SR_basic_manhattan_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((201, 122), (175, 167), AR0011SR_map, "manhattan"),
                                              "basic")
    timer_end = timer()
    print("A0011SR_basic_manhattan_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow map
    # plainsofsnow_heap_no_heuristic_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map), "heap")
    timer_end = timer()
    print("plainsofsnow_heap_no_heuristic_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_heap_euclidean_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map, "euclidean"),
        "heap")
    timer_end = timer()
    print("plainsofsnow_heap_euclidean_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_heap_manhattan_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map, "manhattan"),
        "heap")
    timer_end = timer()
    print("plainsofsnow_heap_manhattan_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_basic_no_heuristic_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map), "basic")
    timer_end = timer()
    print("plainsofsnow_basic_no_heuristic_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_basic_euclidean_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map, "euclidean"),
        "basic")
    timer_end = timer()
    print("plainsofsnow_basic_euclidean_problem")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")

    # plainsofsnow_basic_manhattan_problem
    timer_start = timer()
    result_path = BidirectionalSearchAstar().bidirectional_search_Astar(
        AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map, "manhattan"),
        "basic")
    timer_end = timer()
    print("plainsofsnow_basic_manhattan_problem")
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

    # plainsofsnow_heap_manhattan_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map, "manhattan"),
                                              "heap")
    timer_end = timer()
    print("plainsofsnow_heap_manhattan_problem unidirectional")
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

    # plainsofsnow_basic_manhattan_problem unidirectional
    timer_start = timer()
    result_path = unidirectional_search_Astar(AstarGraphProblem((305, 96), (298, 144), plainsofsnow_map, "manhattan"),
                                              "basic")
    timer_end = timer()
    print("plainsofsnow_basic_manhattan_problem unidirectional")
    print(result_path)
    print("Time elapsed: ", timer_end - timer_start, "\n\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
