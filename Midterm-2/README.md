# Midterm-2

## Problem-1

### Intuitive Approach

The intuitive approach is just to loop through A for every element of B and count the number of values lesser than A[i]
Time Complexity = O(n^2)

#### Time Complexity Analysis

The approach has a nested for loop so in the worst case its time complexity is:

Total time Complexity = O(n^2)

### Effective Approach

To achieve better time complexity, we use merge sort to count the smaller elements instead of the nested loop.

Merge sort works by recursively dividing the array into left and right halves until each subarray contains a single element. During the merging step, we compare elements from the left and right subarrays to rebuild the sorted array. At this point, whenever we choose an element from the right subarray over an element from the left subarray, we know that the chosen element is smaller than the current element in the left subarray. This count of smaller elements is then added to the respective index in B, adding up recursively for each index in A. At the end of the merge B contains the answer values, which is the number of elements smaller than A[i] to the right of A[i] for each index i.

#### Time Complexity Analysis

At each recursive step, the array is split into two halves. There are O(logn) levels of recursion and at each level, merging takes O(n) time because all elements are processed once per level.

Total time complexity = O(nlogn).

### Sample Output

#### Example - 1

Initial List: [3, 1, 4, 2]
Intuitive Approach: B = [2, 0, 1, 0]
Intuitive Approach Time Taken: 7.374677807092667e-06
Merge Sort Approach: B = [2, 0, 1, 0]
Merge Sort Approach Time Taken: 1.1499971151351929e-05

#### Example - 2

for A = [random.randint(0, 200) for _ in range(10**4)]

Intuitive Approach Time Taken: 1.443775207735598
Merge Sort Approach Time Taken: 0.014811540953814983

---

## Problem 2

### Intuitive Approach

The intuitive approach is similar to the last question, just loop through the list for every element and keep track of the current ellemet and update it if the element is < A[i] and at the same time increment the count. Finally use a variable to keep the max count and report it as the answer. This Algorithim is the most intuitive approach and is slow due the the repeated checking of each element.

#### Time Complexity Analysis

The approach has a nested for loop so in the worst case its time complexity is:

Total time Complexity = O(n^2)

### Effective Approach

This approach uses a greedy Algorithim with binary search. Sub holds the longest increasing subsequence whichs starts of as empty but is updated with each element with every iteration. We use binary search to get the postion that num needs to go into sub. if the pos is == the length of sub then its the greatest element and its appended. else it finds the pos of an element num can replace. This gives us an array with all the most increasing nums in A.

#### Time Complexity Analysis

Each iteration of binary search takes O(Log(n)) and its performed once per element in A (O(n)).

Total time Complexity = O(nLog(n))

### Sample Output

#### Example - 1

Initial List: [2, 5, 1, 9, 4, 3, 6]
Intuitive Approach: length = 3
Intuitive Approach Time Taken: 6.00004568696022e-06
Greedy/BinarySearch Approach: length = 3
Greedy/BinarySearch Approach: Time Taken: 6.167218089103699e-06

#### Example - 2

for A = [random.randint(0, 200) for _ in range(10**4)]

Intuitive Approach Time Taken: 0.8655251660384238
Greedy/BinarySearch Approach: Time Taken: 0.0031792917288839817
