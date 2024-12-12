# 1. (50 pts) Given a sequence of tuples, , where each tuple
# consists of a key (k) and a value (v), we define a data structure that satisfies the following two
# conditions:
# (a) It is a binary tree such that the in-order traversal on the values of the nodes gives the
# sorted sequence of values;
# (b) The tree, meanwhile, has the min-heap property on the keys.
# This data structure is particularly useful in searching.
# For example, consider . This data
# structure looks like the following:
# *Graph*
# A = [(k_1 , v_1), (k_2, v_2), … , (k_n, v_n)]
# A = [(5, 6), (1, 2), (3, 4), (9, 1), (6, 9), (2, 8), (4, 3), (8, 5)]
# Please design an algorithm, as efficient as possible, to construct this data structure for a given
# sequence of numbers, and analyze the time complexity.

class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


def sortByValue(tup):
    return sorted(tup, key=lambda x: x[1])


def generateTreesAndIsMinHeap(inorder_tuples):
    def isMinHeap(root):
        if not root:
            return True

        if root.left and root.key > root.left.key:
            return False
        if root.right and root.key > root.right.key:
            return False

        return isMinHeap(root.left) and isMinHeap(root.right)

    if not inorder_tuples:
        return [None]

    for i in range(len(inorder_tuples)):
        root_tuple = inorder_tuples[i]

        # Generate all left and right subtrees recursively
        left_subtrees = generateTreesAndIsMinHeap(inorder_tuples[:i])
        right_subtrees = generateTreesAndIsMinHeap(inorder_tuples[i + 1:])

        # Combine left and right subtrees with the root node
        for left in left_subtrees:
            for right in right_subtrees:
                root = TreeNode(root_tuple[0], root_tuple[1])
                root.left = left
                root.right = right

                # Stop immediately if a valid tree is found
                if isMinHeap(root):
                    return [root]

    return []

# Prints out the tree in a reconstructable format of (key,value,left,right)


def treeToString(root):
    if not root:
        return "null"

    left_str = treeToString(root.left)
    right_str = treeToString(root.right)

    return f"({root.key},{root.value},{left_str},{right_str})"


def inOrderTraversal(root):
    if not root:
        return []

    return inOrderTraversal(root.left) + [(root.key, root.value)] + inOrderTraversal(root.right)


inorder_input = [(5, 6), (1, 2), (3, 4), (9, 1),
                 (6, 9), (2, 8), (4, 3), (8, 5)]

answer = generateTreesAndIsMinHeap(sortByValue(inorder_input))

if answer:
    # Get the first (and only) valid tree.
    serialized_tree = treeToString(answer[0])
    print("Serialized Tree:", serialized_tree)

    inorder_output = inOrderTraversal(answer[0])
    print("In-order Traversal:", inorder_output)
else:
    print("No valid tree found.")
