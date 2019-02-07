A = [2,4,6,4,3,5,78,9,6,5,43,436,7]

def Heapify(A,v,n):
    largest = v
    if 2*v <= n and A[2*v]>A[v]:
        largest = 2*v

    if 2*v+1 <= n and A[2*v+1]>A[largest]:
        largest = 2*v+1

    if largest != v:
        temp = A[v]
        A[v] = A[largest]
        A[largest] = temp
        Heapify(A,largest,n)

    

def BuildHeap(A,n):
    for i in range(n,-1,-1):
        Heapify(A,i,n)

def HeapSort(A):
    n = len(A)-1
    HeapSize = n
    BuildHeap(A,n)
    for i in range(n,0,-1):
        temp = A[i]
        A[i] = A[0]
        A[0] = temp
        HeapSize = HeapSize -1
        Heapify(A,0,HeapSize)

