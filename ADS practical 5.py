#adspractical6kochcurve.py
#algorithms and data structures practical week 6
#matthew johnson 9 november 2012
#last revised 10 november 2013

#####################################################

import tkinter
import math


def koch(start, finish, depth):
    """draw a koch curve between start and finish of stated recursion depth"""
    [start, t1, t2, t3, finish] = calculate_points(start, finish) 
    if depth == 0:
        connect_points([start, t1, t2, t3, finish])
    else:
        koch(start, t1, depth - 1)
        koch(t1, t2, depth - 1)
        koch(t2, t3, depth - 1)
        koch(t3, finish, depth - 1)

#runs when start button is pressed
def start():
    depth=int(recursiondepth.get())
    koch(*initial_conditions())
    koch(coordinate(325.0,569.7),coordinate(100.0,180.0),depth)
    koch(coordinate(550.0,180.0), coordinate(325.0,569.7),depth)


def starth():
    depth=int(recursiondepth.get())
    h_tree(coordinate(320.0,300.0),200,depth)
   
def h_tree(m, l, depth):
    l = l/2
    u= coordinate(m.x+l,m.y)
    v= coordinate(m.x-l,m.y)
    draw_line(u,v)
    x= coordinate(m.x+l,m.y+l)
    y= coordinate(m.x+l,m.y-l)
    draw_line(x,y)
    u= coordinate(m.x-l,m.y+l)
    v= coordinate(m.x-l,m.y-l)
    draw_line(u,v)
    if depth != 0:
        depth -=1
        h_tree(u,l,depth)
        h_tree(v,l,depth)
        h_tree(x,l,depth)
        h_tree(y,l,depth)

    

def initial_conditions():
    return coordinate(100.0,180.0), coordinate(550.0,180.0), int(recursiondepth.get())


def calculate_points(start, finish):
    delta = finish - start
    perp = delta.perpendicular()
    t1 = start + delta * (1/3)
    t2 = start + delta * (1/2) + perp * (math.sqrt(3)/6)
    t3 = start + delta * (2/3)
    return [start, t1, t2, t3, finish]

def connect_points(points):
    """draws lines to connect a list of points together"""
    for i in range(len(points) - 1):
        draw_line(points[i], points[i+1])

def draw_line(u, v):
    """draws a straight line between two coordinates u and v"""
    canvas.create_line(u.x, u.y, v.x, v.y)

def draw_triangle(left, right, bottom, colour="#f62817"):
    """draw triangle given coordinates of corners and colour for fill"""
    canvas.create_polygon(left.x, left.y, right.x, right.y, bottom.x, bottom.y, fill=colour)



def square(midpoint, length, colour):
    """draws a square of given midpoint length and colour"""
    offset = coordinate(length/2, length/2)
    bottomleft = midpoint - offset
    topright = midpoint + offset
    canvas.create_rectangle(bottomleft.x, bottomleft.y, topright.x, topright.y, fill=colour)


class coordinate(object):
    """creates a class for coordinates in the x-y plane
    that can be added and multiplied by constants"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return coordinate(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return coordinate(self.x - other.x, self.y - other.y)
    def __mul__(self, const):
        return coordinate(const * self.x, const * self.y)
    def perpendicular(self):
        """rotate 90 degrees anticlockwise"""
        return coordinate(self.y, self.x * (-1))

def midpoint(c1, c2):
    """finds the midpoint of two coordinates"""
    return(coordinate((c1.x+c2.x)/2, (c1.y+c2.y)/2))


   
#####################################################

#clears the canvas when clear button is pressed
def clear():
    canvas.delete("all")
    
#set up window with buttons, labels etc
window = tkinter.Tk()
window.title("ADS Practical 6: Koch curve")
clear_button = tkinter.Button(window, text = "Clear", command = clear)
start = tkinter.Button(window, text="Start", command=starth)
recursiondepth=tkinter.StringVar()
defaultrecursion = 0 #default depth of recursion
recursiondepth.set(defaultrecursion)
recLabel=tkinter.Label(window, width="17")
recLabel.configure(text="    Depth of recursion =   ")
recentry=tkinter.Entry(window, width="2", textvariable=recursiondepth)
canvas = tkinter.Canvas(window, width=620, height=600)
canvas.pack(side="top")
start.pack(side="right")
clear_button.pack(side = "right")
recLabel.pack(side="left")
recentry.pack(side="left")

# start event loop
window.mainloop()

