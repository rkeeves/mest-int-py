#!/usr/bin/env python3

from systematic_fixtures import unpack_graph_fixture, graph_fixture_00, graph_fixture_01


def dfs_tree(graph_fixture, max_closed_node_count):
    (start, edges_dict) = unpack_graph_fixture(graph_fixture)
    opens = [start]
    visited = []
    while len(opens) != 0 and len(visited) < max_closed_node_count:
        node = opens.pop()
        visited.append(node)
        # check
        for target in edges_dict.get(node, []):
            opens.append(target)
    return visited


def main():
    fixture = graph_fixture_01()
    visited = dfs_tree(fixture, 10)
    print(str(visited))


##############################################################################

if __name__ == "__main__":
    main()
