import time
import random

# (50 pts) Given an arbitrary array A, design an algorithm, as efficient as possible,
# to find the length of the longest increasing subsequence. A valid increasing subsequence may not be contiguous.
# And, there can be multiple longest increasing subsequences. Time complexity analysis is required.
# For example, in A = [2, 5, 1, 9, 4, 3, 6], the longest increasing subsequences are [2, 5, 9],[2, 5, 6],[1, 4, 6])
# ,and [1, 3, 6].
# Thus, the length of the longest increasing subsequence in this example is 3.


def intuitiveApproach(A):
    max = -100
    for i in range(0, len(A)):
        count = 1
        curr = A[i]
        for j in range(i+1, len(A)):
            if (curr < A[j]):
                count += 1
                curr = A[j]
        if (max < count):
            max = count

    return max


def longestIncreasingSequence(A):
    # This will store the longest increasing subsequence
    sub = []
    for num in A:
        # We use bunary search to get where the num can be placed inside of sub
        pos = binary_search(sub, num)

        # This means num is greater than everything in sub so it gets appended to the end
        if pos == len(sub):
            sub.append(num)
        # This means that num is greater than the element in pos so replace it with num but
        # it isnt the greatest in the array
        else:
            sub[pos] = num
    return len(sub)

# standard binary search algo


def binary_search(sub, num):
    left, right = 0, len(sub)
    while left < right:
        mid = (left + right) // 2
        if sub[mid] < num:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == "__main__":
    A = [2, 5, 1, 9, 4, 3, 6]
    print(f"Initial List: {A}")
    # A = [random.randint(0, 200) for _ in range(10**5)]

    # Records the time taken for each operation
    int_start = time.perf_counter()
    print(f"Intuitive Approach: length = {intuitiveApproach(A)}")
    int_stop = time.perf_counter()
    print(f"Intuitive Approach Time Taken: {int_stop-int_start}")

    gbs_start = time.perf_counter()
    print(
        f"Greedy/BinarySearch Approach: length = {longestIncreasingSequence(A)}")
    gbs_stop = time.perf_counter()
    print(f"Greedy/BinarySearch Approach: Time Taken: {gbs_stop-gbs_start}")
