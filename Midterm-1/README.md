# Midterm-1
## Problem-1

### Iteration:

#### Pros:

- More memory-efficient, the program runs in O(n) time and O(1) size which is way faster that the recursive method.
- Faster avoids the overhead of multiple function calls allowing for quicker runtimes.
- Easier to debug and simpler readable code.

#### Cons:

- Less intuitive for problems that naturally fit recursion like divide and conquer problems.
- Can be harder to implement for complex recursive structures like trees and sequences.

### Recursion:

#### Pros:

- Code is cleaner and works well for naturally recursive problems.
- Fits mathematical definitions like Fibonacci pretty straight forward.
- Easier for problems as divide and conquer algorithms.

#### Cons:

- Can fail to calculate a result due to reaching max depth.
- Performance is really bad compared to the iterative, its time complexity in O(2^n).
- Harder to debug, deep recursion can make it harder to trace or debug issues.

### Sample Output

Enter the k'th number
38
Iterative Fibonacci number 39088169
Iterative Time: 0.0002199580194428563
Reccursive Fibonacci number 39088169
Reccursive Time: 3.3702377079753205

---

## Problem 2

### Time Complexity

The Time complexity of the algorithm is O(n). The key operations are:

1. traversing = O(n)
2. Reversing a group = O(n)
3. Connecting reversed group = O(1)

### Space Complexity

The Space complexity of the algorithm is O(1), because we don’t use any large data structures to store n-elements.

### Sample Output


#### Example 1
Initial List:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
Group size: 4

Result List:
4 -> 3 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5 -> 9

#### Example 2
Initial List:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
Group size: 3

Result List:
3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7
