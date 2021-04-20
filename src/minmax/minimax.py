#!/usr/bin/env python3

import math
import nodes


def minimax(node, depth, supported_player):
    def func(node, depth, player):
        node.visited = True
        if depth == 0 or len(node.children) == 0:
            node.val = node.h if supported_player == player else -node.h
            return node.val
        if player == 1:
            node.val = -math.inf
            for child in node.children:
                node.val = max(node.val, func(child, depth - 1, -player))
            return node.val
        node.val = math.inf
        for child in node.children:
            node.val = min(node.val, func(child, depth - 1, -player))
        return node.val

    return func(node, depth, supported_player)


def negamax(node, depth, supported_player):
    def func(node, depth, player):
        node.visited = True
        if depth == 0 or len(node.children) == 0:
            node.val = node.h
            return node.val
        node.val = -math.inf
        for child in node.children:
            node.val = max(node.val, -func(child, depth - 1, -player))
        return node.val

    return func(node, depth, supported_player)


def alfabeta(node, depth, supported_player):
    def func(node, depth, player, alfa, beta):
        node.visited = True
        if depth == 0 or len(node.children) == 0:
            node.val = node.h if supported_player == player else -node.h
            return node.val
        node.alfa = alfa
        node.beta = beta
        if player == 1:
            node.val = -math.inf
            for child in node.children:
                node.val = max(
                    node.val, func(child, depth - 1, -player, node.alfa, node.beta)
                )
                node.alfa = max(node.alfa, node.val)
                if node.beta <= node.alfa:
                    break
            return node.val
        node.val = math.inf
        for child in node.children:
            node.val = min(
                node.val, func(child, depth - 1, -player, node.alfa, node.beta)
            )
            node.beta = min(node.beta, node.val)
            if node.beta <= node.alfa:
                break
        return node.val

    return func(node, depth, supported_player, -math.inf, math.inf)


def run_minimax(internal_node_child_counts, leaf_values, depth, player):
    root = nodes.treeOf(internal_node_child_counts[:], leaf_values[:])
    val = minimax(root, depth, player)
    print("## Minmax result: {}".format(val))
    print("## Tree post minmax")
    nodes.print_minimax_tree(root)


def run_negamax(internal_node_child_counts, leaf_values, depth, player):
    root = nodes.treeOf(internal_node_child_counts[:], leaf_values[:])
    val = negamax(root, depth, player)
    print("## Negamax result: {}".format(val))
    print("## Tree post negamax")
    nodes.print_negamax_tree(root)


def run_alfabeta(internal_node_child_counts, leaf_values, depth, player):
    root = nodes.treeOf(internal_node_child_counts[:], leaf_values[:])
    val = alfabeta(root, depth, player)
    print("## Alfabeta result: {}".format(val))
    print("## Tree post alfabeta")
    nodes.print_alfabeta_tree(root)


def main():
    internal_node_child_counts = [3, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2]
    leaf_values = [1, 10, 2, 3, -2, 2, 4, 6, 6, -6, 8, 5, 7, 10, 1, 2, 4, 5, 6, 8]
    depth = 10
    supported_player = 1
    run_minimax(internal_node_child_counts, leaf_values, depth, supported_player)
    run_negamax(internal_node_child_counts, leaf_values, depth, supported_player)
    run_alfabeta(internal_node_child_counts, leaf_values, depth, supported_player)


##############################################################################

if __name__ == "__main__":
    main()
