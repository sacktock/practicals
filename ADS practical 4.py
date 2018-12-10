#adspractical5.py
#algorithms and data structures practical week 5
#matthew johnson 2 november 2012
#revised 31 october 2018

#####################################################


############
#Question 3#
############

def hash(d):
    """given a list d of integers returns a list of length 13
    describing the hash table obtained when the hash function
    h(k)=k mod 13 is applied to each integer k in d"""
    n=13
    #initialize table
    table = ["-"]*n
    #
    #now you do the rest
    for i in range(0,len(d)):
        k=d[i]
        k=k%n
        for j in range(0,n+1):
            if j==n+1:
                print ("hash table is full "+str(d[i])+" couldn't be added")
                break
            if table[(k+j)%n]=="-":
                table[(k+j)%n]=d[i]
                break
    return table
        



def testq3():
    assert hash([25,6,39,17,12,15,53]) == [39, 12, 15, 53, 17, '-', 6, '-', '-', '-', '-', '-', 25]
    assert hash([0,1,2,3,4,5,6,7,8,9,10,11,12]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert hash([10,11,12,0,1,2,3,4,5,6,7,8,9]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert hash([-1,-2,-3]) == ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', -3, -2, -1]
    assert hash([53,25,6,39,17,12,15]) == [39, 53, 12, 15, 17, '-', 6, '-', '-', '-', '-', '-', 25]
    print ("all basic tests passed")
    assert hash([25,6,39,17,12,15,53,53]) == [39, 12, 15, 53, 17, '-', 6, '-', '-', '-', '-', '-', 25]
    assert hash([1,1,1,1,2,2,2,3,3,3]) == ['-', 1, 2, 3, '-', '-', '-', '-', '-', '-', '-', '-', '-']    
    print ("all tests involving duplicates passed")
    print ("now  we test inputs containing more integers than the size of the table")
    print ("you will wait forever if you have not considered this case")
    assert hash([0,1,2,3,4,5,6,7,8,9,10,11,12,13]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert hash([0,1,1,1,7,1,2,3,4,0,5,6,7,8,9,9,9,10,11,12,13]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print ("all tests passed")



############
#Question 4#
############

def modulus(m ,n):
    """returns value of m mod n"""
    if m<n:
        return m
    else:
        return modulus(m-n, n)

############
#Question 5#
############

def DigitSum(n):
    """returns sum of the digits of a positive integer"""
    if len(str(n))==1:
        return n
    else:
        return int(str(n)[0])+DigitSum(int(str(n)[1:]))

#####################################################


mimo=[2,1]
def lucas(n):

    if len(mimo)>=n:
        return mimo[n-1]
    else:
        mimo.append(lucas(n-1) + lucas(n-2))
    return mimo[n-1]

def c(m,n):
    if n == 0: return 1
    if n == m: return 1
    if n == 1: return m
    if n == m-1: return m
    return c(m-1,n-1)+c(m-1,n)

    
