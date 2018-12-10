def exercise1():
    lst = input("non empty list:")
    if len(lst)>=1:
        print (lst[0], lst[-1])
    else:
        print ("empty")

def ex2():
    num1 = eval(input("num1?"))
    num2 = eval(input("num2?"))
    num3 = eval(input("num3?"))
    num4 = eval(input("num4?"))
    import math
    print ((num1+num2+num3)/3==num4)
    
def ex3():
    x= eval(input("x coordinate?"))
    y= eval(input("y coordinate?"))
    print ((x**2+y**2)<8**2)

def ex4():
    x = input("4 digit number?")
    for char in x:
         print(char)
   
def pay(rate,hours):
    if hours>40:
        return rate*40 + rate*1.5*(hours-40)
    else:
        return rate*hours

def ex6():
    lst = []
    lst= [x for x in input("List of strings?").split()]
    print (lst)
    for i in range(0, len(lst)):
        if lst[i] != "secret":
            print (lst[i])

def ex7():
    lst= [x for x in input("List of strings?").split()]
    for student in lst:
        if student[0].upper()<'N':
            print (student)

def ex8():
    integer = eval(input("positive intreger?"))
    for i in range (1,5):
        print (integer*i)

            
def ex9():
    integer = eval(input("positive intreger?"))
    i=1
    while i < integer//i:
        if integer%i==0:
            print (i, integer//i)
        i+=1

def reverse_string(string):
    return string[::-1]

def coin_toss(n):
    return 0.5**n

def reverse_int(integer):
    return int(str(integer)[::-1])

def points(x1,y1,x2,y2):
    m = (y2-y1)/(x2-x1)
    c = y1-m*x1
    print ("equation of striaght line through points: y = "+ str(m)+"x + "+str(c))
    print ("distance between points: "+ str(((y2-y1)**2+(x2-x1)**2)**0.5))
    
def abbreviation(day):
    return day[:2].upper()

def collision(x1,y1,r1,x2,y2,r2):
    if r1 == 0 or r2 == 0:
        return False
    else:
        return ((x1-x2)**2 + (y1-y2)**2)**0.5 <= r1+r2

def partition(lst):
    return 0

def lastF(string):
    strings = string.split()

    return strings[1] + ", "+strings[0][0].upper()

def avg(parentLst):
    lst = []
    for childLst in parentLst:
        avg=0
        for number in childLst:
            avg+=number
        avg= avg/len(childLst)
        lst.append(avg)
    return lst
    
def hit(x,y,r,u,v):
    hit = (u-x)**2+(v-y)**2 <= r**2
    if hit:
        return "Yes"
    else:
        return "No"

def more_than_two_ts():
    
    


    
