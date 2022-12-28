import fileinput
from itertools import chain, count, islice

import networkx as nx
import numpy as np

OFFSETS = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]


def main():
    blizzards: list[str] = list(map(str.rstrip, fileinput.input()))

    print(*part_1_and_2(blizzards), sep='\n')


def part_1_and_2(blizzards: list[str]) -> tuple[int, int]:
    blizzards_ = np.zeros((len(blizzards) - 2, len(blizzards[0]) - 2), np.ubyte)
    aux_n_1 = np.empty_like(blizzards_)
    aux_n_2 = np.empty_like(blizzards_)
    aux_b = np.empty_like(blizzards_, np.bool_)
    height = blizzards_.shape[0]
    width = blizzards_.shape[1]
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
    graph.add_node((0, height, width - 1))
    graph.add_nodes_from((0, y, x) for y, x in zip(*np.where(np.equal(blizzards_, 0, out=aux_b))))

    first = blizzards_.copy()

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

        for y, x in chain(zip(*np.where(np.equal(blizzards_, 0, out=aux_b))), [(-1, 0), (height, width - 1)]):
            curr_node = i, y, x

            for y_offset, x_offset in OFFSETS:
                if graph.has_node(prev_node := (prev_i, y + y_offset, x + x_offset)):
                    graph.add_edge(prev_node, curr_node)

        if i == 0:
            break

    a = min((time_, node) for node, time_ in nx.single_source_shortest_path_length(graph, (0, -1, 0)).items()
            if node[1] == height)
    b = min((time_, node) for node, time_ in nx.single_source_shortest_path_length(graph, a[1]).items()
            if node[1] == -1)
    c = min((time_, node) for node, time_ in nx.single_source_shortest_path_length(graph, b[1]).items()
            if node[1] == height)

    return a[0], a[0] + b[0] + c[0]


if __name__ == '__main__':
    main()
