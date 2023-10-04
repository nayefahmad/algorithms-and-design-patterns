"""
# Creating a tree structure from a list
## Overview

Let's say we want to represent the following set of bullet points as a tree structure:

1. Team members
  A. Alice
  B. Bob
     i. Bob's cat
  C. Charlie

We represent the levels of the bullet points using this list: [1, 2, 2, 3, 2]

Goal: convert to a tree structure.

Expected output: [1, [2], [2, [3]], [2]]

## References:
- [Intro to trees](https://bradfieldcs.com/algos/trees/introduction/)
- [Representing trees](https://bradfieldcs.com/algos/trees/representing-a-tree/)

"""


def create_tree_structure(lst):
    root = []  # note that root will change each time in the loop below
    current_nodes = [root]

    for idx, val in enumerate(lst):
        # For each value in the input list, create a new node
        new_node = [val]
        print(f"----new_node: {new_node}")

        # Add the new node as a child of the current node at the level one less than
        # `val`
        print(f"current nodes: {current_nodes}")

        if idx == 1:
            assert current_nodes[0][0] is current_nodes[1]
            # Possible explanation:
            # In this case, current_nodes[0][0] and current_nodes[1] are both
            # assigned the integer value 1. Python caches certain small integers
            # because they are used frequently. So when you use an integer within
            # that range, you're actually getting a reference to the same integer
            # object. Hence, current_nodes[0][0] and y are pointing to the same memory
            # location, and current_nodes[0][0] is current_nodes[1] returns True.

        current_nodes[val - 1].append(new_node)

        print(f"current nodes: {current_nodes}")

        # When we encounter a value in the input `lst`, the operation we perform
        # depends on the depth level indicated by the value. The length of current_nodes
        # represents the current depth of the tree.
        print(f"len(current_nodes): {len(current_nodes)}")
        print(f"val: {val}")
        if len(current_nodes) > val:
            # Add a node at the same level
            current_nodes[val:] = [new_node]
        else:
            # Add a node at a deeper level
            current_nodes.append(new_node)

    return root[0]


# Usage
input_list = [1, 2, 2, 3, 2]
input_list_02 = [0, 1, 2, 3, 1, 2, 3, 3, 1]
input_list_03 = [1, 1, 1]

for input_list in [input_list, input_list_02, input_list_03]:
    tree_structure = create_tree_structure(input_list)
    print(tree_structure)

# todo: explain this. Is it a feature or bug in the algorithm?
# Example 1
x = [1]
y = [[x], x]
assert y == [[[1]], [1]]
y[1].append([2])
assert y == [[[1, [2]]], [1, [2]]]

# Example 2
new_node = [1]
current_nodes = [[new_node], new_node]
new_node = [2]
assert current_nodes[0][0] is current_nodes[1]
current_nodes
current_nodes[0][0].append([9])
current_nodes
