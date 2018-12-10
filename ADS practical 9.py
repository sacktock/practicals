
def sort5(lst):
    t=0
    for j in range(1,5):
        x = lst[j]
        i = j - 1
        
        while i >= 0 and lst[i] > x:
            t += 1
            lst[i+1] = lst[i]
            i = i - 1

        lst[i+1] = x

    print(t)
    return lst
    

def sort5_network(lst):
    sort_pairs(lst,0,1)
    sort_pairs(lst,3,4)
    sort_pairs(lst,2,4)
    sort_pairs(lst,2,3)
    sort_pairs(lst,1,4)
    sort_pairs(lst,0,3)
    sort_pairs(lst,0,2)
    sort_pairs(lst,1,3)
    sort_pairs(lst,1,2)
    print(9)
    return lst  


def sort_pairs(lst, x ,y):
    if lst[x] > lst[y]:
        temp = lst[x]
        lst[x] = lst[y]
        lst[y] = temp


def algo(A):
    matrix = []
    t = []
    b = []
    C = []
    n = len(A)
    for i in range(0, n):
        t.append(0)
        b.append(0)
        C.append(0)
    C.append(0)
    for i in range(0, n):
        matrix.append(t)
        

    for i in range(0, n):
        for j in range(0,n):
            if A[i] > A[j]:
                matrix[i][j] = 1

    for i in range(0,n):
        for j in range(0,n):
            b[i] += matrix[i][j]
        
    for i in range(0,n):
        C[1+b[i]] = A[i]
    print(matrix)
    print(b)
    return C


