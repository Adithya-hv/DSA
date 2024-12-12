# Final

## Problem-1

The program is designed using a brute-force approach. It takes an inorder traversal list, generates every possible binary tree, and checks each one to determine if it satisfies the conditions of a min-heap. It outputs the first valid solution it finds. This was the most straightforward approach I could think of, but there are for sure more optimized solutions.

### Time Complexity

The Time Complexity of this program is, $O(C_{n})$, this is mainly due to the fact that is creates every possible binary tree for a given inorder traversal. This also means that for a large n vaule this program will fail.

Time Complexity = $O(nLog(n))(\text{Sorting the Arr}) + O(n)(\text{Checking MinHeap}) + O(C_{n})(\text{Generating Trees})$

### Sample Output

Serialized Tree: (1,2,(9,1,null,null),(2,8,(3,4,(4,3,null,null),(5,6,(8,5,null,null),null)),(6,9,null,null)))
In-order Traversal: [(9, 1), (1, 2), (4, 3), (3, 4), (8, 5), (5, 6), (2, 8), (6, 9)]

---

## Problem 2

The program performs the deletion operation on a binary min-heap. It removes an element from the heap by replacing it with the last element, then restores the heap property using the heapify-down function. This operation ensures that the smallest element remains at the root and the tree stays balanced.

### Time Complexity

The Time COmplexity of this program is O(Log(n)) de to the heapify down function as it traveses the tree.
The height of a binary heap with n elements is O(Logn).

### Sample Output

heap before deletion [51, 202, 100, 771]
heap after deletion [100, 202, 771]
