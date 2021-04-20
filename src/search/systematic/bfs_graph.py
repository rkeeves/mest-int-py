#!/usr/bin/env python3

from systematic_fixtures import unpack_graph_fixture, graph_fixture_00, graph_fixture_01


def bfs_graph(graph_fixture, max_closed_node_count):
    (start, edges_dict) = unpack_graph_fixture(graph_fixture)
    opens = [start]
    visited = []
    while len(opens) != 0 and len(visited) < max_closed_node_count:
        node = opens.pop(0)
        if not node in visited:
            visited.append(node)
            # check
            for target in edges_dict.get(node, []):
                if not target in opens:
                    opens.append(target)
    return visited


def main():
    fixture = graph_fixture_01()
    visited = bfs_graph(fixture, 10)
    print(str(visited))


##############################################################################

if __name__ == "__main__":
    main()
