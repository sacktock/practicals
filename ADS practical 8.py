import random

def permute(k,A):
    k=random.randint(0,k)
    
    n = len(A)
    k = k % n

    for i in range(0, n):
        temp = A[i]
        A[i] = A[(i + k) % n]
        A[(i + k) % n] = temp

    return A


def monkey_sort(A):
    while not isSorted(A):
        random.shuffle(A)

    return A

def isSorted(A):
    for i in range(0, len(A) -1):
        if A[i]>A[i+1]:
            return False

    return True
