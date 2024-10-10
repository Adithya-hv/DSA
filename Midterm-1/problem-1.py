import time

# Many functions can be implemented using either iterations or recursion, such as
# computing the Fibonacci number. Please argue the pros and cons of both iteration-based and
# recursion-based implementations.

# Iterative definition of the Fib sequence keeps track of the last two numbers and adds them 
# to make the next in the seqeunce and loops till the required number
def iterative(k):
    result, fib1, fib2= 0, 0, 1
    if k == 1: return(fib1)
    elif k == 2: return(fib2)
    for i in range(k-1):
        result = fib1+fib2
        fib1 = fib2
        fib2 = result
    return(result)

# The recursive definition of the Fib sequence, makes a tree of functions eventually going up 
# returning the required numbers till it reaches the answer at the root.  
def recursive(k):
    if k <= 1:
        return k
    return recursive(k - 1) + recursive(k - 2)
        

if __name__ == "__main__":
    k = int(input("Enter the k'th number \n"))
    
    # Records the time taken for each operation
    itr_start = time.perf_counter() 
    print(f"Iterative Fibonacci number {iterative(k)}")
    itr_stop = time.perf_counter() 
    print(f"Iterative Time Taken: {itr_stop-itr_start}")

    
    rec_start = time.perf_counter() 
    print(f"Reccursive Fibonacci number {recursive(k)}")
    rec_stop = time.perf_counter()
    print(f"Reccursive Time Taken: {rec_stop-rec_start}")