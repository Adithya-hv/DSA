import time
import random

# (50 pts) Given an arbitrary array of integers, please design an algorithm,
# as efficient as possible, that constructs another array of the same size
# (i.e., B, where |B| = |A|, where B[i] is the number of elements in A on the right side of A[i])
# and smaller than \( A[i] \). Time complexity analysis is required. For example,
# A = [3, 1, 4, 2], B = [2, 0, 1, 0].


def intuitiveApproach(A):
    B = [0] * len(A)

    for i in range(0, len(A)):
        count = 0
        for j in range(i, len(A)):
            if (A[i] > A[j]):
                count += 1
        B[i] = count

    return B


def efficientApproach(A):
    B = [0] * len(A)

    def merge_sort(A):
        mid = len(A) // 2

        # Base case, single element is sorted
        if mid == 0:
            return A

        # recursive calls to sort left and right halves
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])

        merged = []
        i = j = 0  # pointers tha keep track of left and right

        while i < len(left) and j < len(right):

            # Basically checks if value of left at index i <= value of right at index j
            # j is the key pointer here, it keeps track of the number of elements that are smaller than
            # the left and on the right side of i
            if left[i][1] <= right[j][1]:
                B[left[i][0]] += j
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        for remaining in left[i:]:
            B[remaining[0]] += j
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

    merge_sort(list(enumerate(A)))

    return B


if __name__ == "__main__":
    A = [3, 1, 4, 2]

    # A = [random.randint(0, 200) for _ in range(10**4)]

    print(f"Initial List: {A}")

    # Records the time taken for each operation
    int_start = time.perf_counter()
    print(f"Intuitive Approach: B = {intuitiveApproach(A)}")
    int_stop = time.perf_counter()
    print(f"Intuitive Approach Time Taken: {int_stop-int_start}")

    msa_start = time.perf_counter()
    print(f"Merge Sort Approach: B = {efficientApproach(A)}")
    msa_stop = time.perf_counter()
    print(f"Merge Sort Approach Time Taken: {msa_stop-msa_start}")
