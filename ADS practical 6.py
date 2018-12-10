
lst = [4,3,2,1,6,5,8,7]

#def insertion_sort(lst):
#    for j in range(0,len(lst)):
#        x = lst[j]
#        for i in range(j+1, len(lst)):
#            if lst[i] < x:
#                temp = x
#                x = lst[i]
#                lst[i] = temp
#        lst[j] = x
        
        
def insertion_sort(a):
    for j in range(1,len(a)):
        x = a[j]
        i = j - 1
        while i >= 0 and a[i] > x:
            a[i+1] = a[i]
            i = i -1
        a[i+1] = x
