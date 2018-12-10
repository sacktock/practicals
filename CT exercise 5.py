import math

def arith(s):
    if len(s) >= 2:
        d  = s[1]-s[0]
    else: return True
    for i in range(2,len(s)):
        if d != s[i]-s[i-1]: return False
    return True            
        

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
def acronym(s):
    l=s.split(' ')
    o=''
    for w in l:
        o+=w[0].upper()
    return o
        
def d(n):
    l = []
    for i in range(1,n+1):
        if n%i == 0:
            l.append(i)
    return l
            
def bubblesort(lst):

    for i in range (len(lst),0,-1):
        for j in range(0,i-1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1]=temp

def negative(lst):
    x=0
    while x < len(lst):
        if lst[x] < 0: return x
        else: x+=1

    return -1


def approxE(error):
    prev=1
    current=2
    i=2
    while current-prev > error:
        prev = current
        current += 1/fact(i)
        i+=1
    return current

mimo=[1,1]
def fib(n):

    if len(mimo)>=n:
        return mimo[n-1]
    else:
        mimo.append(fib(n-1)+fib(n-2))
    return mimo[n-1]

def d2x(n,x):
    if x < 2 or x > 9:
        return False
    s=''
    while n != 0:
        s+= str(n%x)
        n = n//x

    return s[::-1]

def heron(n,error,x0):
    xprev = 0
    xcurr = x0
    i=0
    while abs(xcurr-xprev) > error or i==0:
        xprev = xcurr
        xcurr = 1/2*(xprev+n/xprev)
        i+=1
    return str(i)+' cycles for sqrt(n): '+str(xcurr)
        
def subsetsum(lst,n):
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if lst[i]==lst[j]: continue
            for k in range(j,len(lst)):
                if lst[i]==lst[k] or lst[j]==lst[k]: continue
                if lst[i]+lst[j]+lst[k]+i+j+k==n:return True
    return False

import random
def cipher():
    st=[0,1,2,3,4,5,6,7,8,9]
    cipher=''
    for i in range(0,10):
        n = random.choice(st)
        st.remove(n)
        cipher +=  str(n)

    return cipher

def encrypt(a_string, cipher):
    if len(a_string) != 10 or len(cipher) != 10: return False
    for i in range(0,10):
        if 48 < ord(a_string[i]) >57: return False
        if 48<ord(cipher[i]) >57: return False
        if cipher.count(str(i)) != 1: return False
        
    o=''
    for i in range (0,10):
        o += cipher[int(a_string[i])]
    return o

def sublist(lst1,lst2):
    for l in lst2:
        if len(lst1)==0:return True
        if l == lst1[0]:
            lst1.remove(l)
    if len(lst1)==0:
        return True
    else:
        return False  

def average_lists(lists):
    for i in range(0,len(lists)):
        total = 0
        for x in lists[i]:
            total += x
        lists[i] = total / len(lists[i])
    return lists
    
def adj_matrix_to_lists(matrix):
    n = len(matrix)

    adjlst = []
    for i in range(0,n):
        lst = []
        adjlst.append(lst)
        for j in range(0,n):
            if matrix[i][j] == 1:
                adjlst[i].append(j)
    return adjlst

def adj_lists_to_matrix(lists):
    n= len(lists)

    matrix = []
    for i in range(0, n):
        lst = []
        matrix.append(lst)
        for j in range(0, n):
            if j in lists[i]:
                matrix[i].append(1)
            else:
                matrix[i].append(0)

    return matrix


def inversions(a_string):
    char = 'a'
    x = 0
    for c in a_string:
        if c < char:
            x +=1
        char = c
    return x

def swap_inversions(a_string):
    char = 'a'
    x = 0
    i=0
    output = list(a_string)
    while i < len(output):
        if output[i] < char:
            x +=1
            temp = output[i]
            output[i] = output[i-1]
            output[i-1] = temp
            i = i - 2
        if i < 0: i =0
        char = output[i]
        i += 1
        
    return ''.join(output), x





    
        







    
        



            


        
    



    


                
