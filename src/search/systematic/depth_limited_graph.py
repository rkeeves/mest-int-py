#!/usr/bin/env python3

from systematic_fixtures import unpack_graph_fixture, graph_fixture_00, graph_fixture_01


def depth_limited_graph(graph_fixture, max_closed_node_count, depth_limit):
    (start, edges_dict) = unpack_graph_fixture(graph_fixture)
    opens = [(start, 0)]
    visited = []
    while len(opens) != 0 and len(visited) < max_closed_node_count:
        node = opens.pop()
        (symbol, depth) = node
        if symbol not in [node[0] for node in visited]:
            visited.append(node)
            if depth < depth_limit:
                # check
                for target in edges_dict.get(symbol, []):
                    if target not in [open_node[0] for open_node in opens]:
                        opens.append((target, depth + 1))
    return visited


def main():
    fixture = graph_fixture_01()
    visited = depth_limited_graph(fixture, 10, 3)
    print(str(visited))


##############################################################################

if __name__ == "__main__":
    main()
