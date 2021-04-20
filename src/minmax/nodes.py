#!/usr/bin/env python3

import math

class Node:
    def __init__(self):
        self.children = []
        self.h = None
        self.val = None
        self.alfa = -math.inf
        self.beta = math.inf
        self.visited = False

    def __str__(self):
        return "Node(v={}, children={})".format(str(self.val), "["+", ".join([str(node) for node in self.children]) + "]")

def minimax_node_stringifier(node, depth):
    return "{} [h:{}, v:{}]".format(" "*depth*3, str(node.h), str(node.val))

def negamax_node_stringifier(node, depth):
    return "{} [h:{}, v:{}]".format(" "*depth*3, str(node.h), str(node.val))

def alfabeta_node_stringifier(node, depth):
    visited_prefix = "" if node.visited else "NOT "
    return "{} [h:{}, v:{}, a:{}, b:{}, {}visited]".format(" "*depth*3,str(node.h),str(node.val),str(node.alfa),str(node.beta), visited_prefix)


def print_tree(root, stringifier):
    def print_node(node, depth):
        print(stringifier(node,depth))
        for child in node.children:
            print_node(child, depth+1)
    print_node(root,0)

def print_minimax_tree(root):
    print_tree(root, minimax_node_stringifier)

def print_negamax_tree(root):
    print_tree(root, negamax_node_stringifier)

def print_alfabeta_tree(root):
    print_tree(root, alfabeta_node_stringifier)

def treeOf(internal_node_child_counts, leaf_values):
    
    def populate_level(nodes, child_counts):
        if len(child_counts) == 0:
            return nodes
        next_level = []
        for node in nodes:
            child_count = 0 if len(child_counts) == 0 else child_counts.pop()
            for i in range(0,child_count):
                child = Node()
                node.children.append(child)
                next_level.append(child)
        populate_level(next_level,child_counts)
        return nodes

    def fill_leaves(node, leaf_values):
        if len(node.children) == 0:
            node.h = leaf_values.pop()
            return
        for node in node.children:
            fill_leaves(node, leaf_values)
        return

    internal_node_child_counts.reverse()
    leaf_values.reverse()
    root = Node()
    populate_level([root], internal_node_child_counts)
    fill_leaves(root,leaf_values)
    return root

##############################################################################

if __name__ == "__main__":
    main()
