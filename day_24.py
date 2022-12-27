import fileinput
from itertools import count, islice

import networkx as nx
import numpy as np


def main():
    blizzards: list[str] = list(map(str.rstrip, fileinput.input()))

    print(*part_1_and_2(blizzards), sep='\n')


def part_1_and_2(blizzards: list[str]) -> tuple[int, int]:
    blizzards_ = np.zeros((len(blizzards) - 2, len(blizzards[0]) - 2), np.ubyte)
    aux_n_1 = np.empty_like(blizzards_)
    aux_n_2 = np.empty_like(blizzards_)
    aux_b = np.empty_like(blizzards_, np.bool_)
    graph = nx.DiGraph()

    for y, row in enumerate(islice(blizzards, 1, len(blizzards) - 1)):
        for x, tile in enumerate(islice(row, 1, len(row) - 1)):
            match tile:
                case '<':
                    blizzards_[y, x] = 0b0001
                case 'v':
                    blizzards_[y, x] = 0b0010
                case '>':
                    blizzards_[y, x] = 0b0100
                case '^':
                    blizzards_[y, x] = 0b1000

    graph.add_node((0, -1, 0))
    graph.add_nodes_from((0, y, x) for y, x in zip(*np.where(np.equal(blizzards_, 0, out=aux_b))))
    graph.add_node((0, blizzards_.shape[0], blizzards_.shape[1] - 1))

    first = blizzards_.copy()
    enters = []
    exits = []

    for i in count(1):
        # <
        np.bitwise_and(blizzards_[:, 1:], 0b0001, out=aux_n_1[:, :-1])
        np.bitwise_and(blizzards_[:, 0], 0b0001, out=aux_n_1[:, -1])

        # v
        np.bitwise_and(blizzards_[:-1, 1:-1], 0b0010, out=aux_n_2[1:, 1:-1])
        np.bitwise_and(blizzards_[-1, 1:-1], 0b0010, out=aux_n_2[0, 1:-1])
        aux_n_1[:, 1:-1] |= aux_n_2[:, 1:-1]

        # >
        np.bitwise_and(blizzards_[:, :-1], 0b0100, out=aux_n_2[:, 1:])
        np.bitwise_and(blizzards_[:, -1], 0b0100, out=aux_n_2[:, 0])
        aux_n_1 |= aux_n_2

        # ^
        np.bitwise_and(blizzards_[1:, 1:-1], 0b1000, out=aux_n_2[:-1, 1:-1])
        np.bitwise_and(blizzards_[0, 1:-1], 0b1000, out=aux_n_2[-1, 1:-1])
        aux_n_1[:, 1:-1] |= aux_n_2[:, 1:-1]

        aux_n_1, blizzards_ = blizzards_, aux_n_1

        prev_i = i - 1
        if np.array_equal(blizzards_, first):
            i = 0

        graph.add_edge((prev_i, -1, 0), (i, -1, 0))
        graph.add_edge((prev_i, blizzards_.shape[0], blizzards_.shape[1] - 1),
                       (i, blizzards_.shape[0], blizzards_.shape[1] - 1))
        for y, x in zip(*np.where(np.equal(blizzards_, 0, out=aux_b))):
            curr_point = i, y, x

            if graph.has_node(prev_point := (prev_i, y, x)):
                graph.add_edge(prev_point, curr_point)
            if x > 0 and graph.has_node(prev_point := (prev_i, y, x - 1)):
                graph.add_edge(prev_point, curr_point)
            if ((y < blizzards_.shape[0] - 1 or x == blizzards_.shape[1] - 1) and
                    graph.has_node(prev_point := (prev_i, y + 1, x))):
                graph.add_edge(prev_point, curr_point)
            if x < blizzards_.shape[1] - 1 and graph.has_node(prev_point := (prev_i, y, x + 1)):
                graph.add_edge(prev_point, curr_point)
            if (y > 0 or x == 0) and graph.has_node(prev_point := (prev_i, y - 1, x)):
                graph.add_edge(prev_point, curr_point)
        if graph.has_node(prev_point := (prev_i, 0, 0)):
            graph.add_edge(prev_point, enter := (i, -1, 0))
            enters.append(enter)
        if graph.has_node(prev_point := (prev_i, blizzards_.shape[0] - 1, blizzards_.shape[1] - 1)):
            graph.add_edge(prev_point, exit_ := (i, blizzards_.shape[0], blizzards_.shape[1] - 1))
            exits.append(exit_)

        if i == 0:
            break

    while nodes_to_remove := [node for node, degree in graph.degree() if degree == 1]:
        graph.remove_nodes_from(nodes_to_remove)

    a = min((time_, node) for node, time_ in nx.single_source_shortest_path_length(graph, (0, -1, 0)).items()
            if node[1] == blizzards_.shape[0])
    b = min((time_, node) for node, time_ in nx.single_source_shortest_path_length(graph, a[1]).items()
            if node[1] == -1)
    c = min((time_, node) for node, time_ in nx.single_source_shortest_path_length(graph, b[1]).items()
            if node[1] == blizzards_.shape[0])

    return a[0], a[0] + b[0] + c[0]


if __name__ == '__main__':
    main()
