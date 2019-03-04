#adspractical18.py
#algorithms and data structures practical week 17
#matthew johnson 28 february 2013, last revised 20 february 2018

#####################################################

"""
in this practical, we look at depth-first search: there are two tasks

(i) to write a function that given an undirected graph performs a depth-first
search and returns the arrays d, f and pi

(ii) to write a function that given an undirected graph, finds all the
articulation points (using the approach described in the second lecture) 

the second of these might prove fairly challenging so you might prefer to
complete the rest of the questions and then see if you have any time left to
have a go at it (or to look at adspractical17extra.py instead)

i will represent graphs using adjacency lists as last week: the example
graph is

V = "ABCDEFGHIJKLM"
E = {'J': 'E', 'K': 'ELM', 'H': 'CG', 'I': 'EG', 'L': 'EFK', 'M': 'GK', 'B': 'ACFG', 'C': 'ABGH', 'A': 'BCDE', 'F': 'BL', 'G': 'BCHIM', 'D': 'A', 'E': 'AIJKL'}
G = (V, E)

note that as we will not consider directed graphs at all we do not bother to
write G = (V, E, False) as we did last week

you might prefer to use the NetworkX package that you will be using in
Computational Thinking (CT); if you do this then you can use the following code
for DFS (which you might be provided with in one of the CT practicals -- it
does not quite do what we want, but perhaps you can adapt it)

def dfs(G,u):
    n = len(G.nodes())
    global visited_counter
    G.node[u]['visited'] = 'yes'
    visited_counter = visited_counter + 1
    print(u)
    if visited_counter < n:
        for v in G.neighbors(u):
            if G.node[v]['visited'] == 'no':
                dfs(G,v)
"""

###################################################

#we define the example graph that might be useful while you experiment
#can also use the graphs defined for the test functions; see below

V = "ABCDEFGHIJKLM"
E = {'A': 'BCDE',
     'B': 'ACFG',
     'C': 'ABGH',
     'D': 'A',
     'E': 'AIJKL',
     'F': 'BL',
     'G': 'BCHIM',
     'H': 'CG',
     'I': 'EG',
     'J': 'E',
     'K': 'ELM',
     'L': 'EFK',
     'M': 'GK',}
G = (V, E)

###################################################


def dfs(G, source):
    """given an undirected graph G and source vertex, performs a DFS from the
    source and returns the arrays d, f and pi with pi[source)=-1

    G should be given as a pair: vertex string and dictionary of adjacency lists

    use test1() to check"""
    V, E = G
    #initialize arrays as dictionaries and time as 2
    global d, f, pi, col, time
    d, f, pi, col = {}, {}, {}, {}
    for u in V:
        pi[u] = 0
        col[u] = 'white'
    pi[source], d[source] = -1, 1
    time = 0
    
    #insert code here
    dfs_visit(G,source)
    
    return d, f, pi

def dfs_visit(G, u):
    V, E = G
    global d, f, pi, col, time
    col[u] = 'grey'
    time += 1
    d[u] = time
    for v in E[u]:
        if col[v] == 'white':
            pi[v] = u
            dfs_visit(G,v)

    col[u] = 'black'
    time +=1
    f[u] = time
    

"""to see how your function is working in the shell do

>>>a = dfs(G, "A")
>>>print_dfs_output(G, *a)

you should get

      d    f    pi
 A    1    26   -1   
 B    2    23   A    
 C    3    22   B    
 D    24   25   A    
 E    8    19   I    
 F    13   14   L    
 G    4    21   C    
 H    5    6    G    
 I    7    20   G    
 J    9    10   E    
 K    11   18   E    
 L    12   15   K    
 M    16   17   K
"""

###################################################

def print_dfs_output(G, d, f, pi):
    """given a graph and output d, f, pi from dfs, prints arrays in columns"""
    V = G[0]
    print ("      d    f    pi")
    for v in V:
        print (" {: <5}{: <5}{: <5}{: <5}".format(v, d[v], f[v], pi[v]))
        
###################################################

def articulation_points(G):
    """finds the articulation points of an undirected graph; returns a list
    in alphabetical order
    
    G should be given as a pair: vertex point and dictionary of adjacency lists

    use test2() to check"""
    V, E = G
    source = V[0]
    #initialize arrays as dictionaries and time as 1
    global d, pi, time, artic
    d, pi, N =  {}, {}, {}
    artic = []
    for v in V: N[v] = v
    d[source], pi[source] = 1, -1
    time = 2

    #code here

    artic.sort()
    return artic




###################################################

#second test graph (graph used in second lecture)
V1 = "ABCDEFGHIJKL"
E1 = {'A': 'BGHI', 'C': 'BD', 'B': 'ACI', 'E': 'DFJ', 'D': 'CEIJ', 'G': 'AH', 'F': 'EKL', 'I': 'ABD', 'H': 'AG', 'K': 'FJL', 'J': 'DEK', 'L': 'FK'}
G1 = (V1, E1)

#more test graphs
V2 = "ABCDEFGHIJKL"
E2 = {'A': 'B', 'C': 'BD', 'B': 'AC', 'E': 'DF', 'D': 'CE', 'G': 'FH', 'F': 'EG', 'I': 'HJ', 'H': 'GI', 'K': 'JL', 'J': 'IK', 'L': 'K'}
G2 = (V2, E2)

V3 = "ABCDEFGHIJKL"
E3 = {'A': 'BL', 'C': 'BD', 'B': 'AC', 'E': 'DF', 'D': 'CE', 'G': 'FH', 'F': 'EG', 'I': 'HJ', 'H': 'GI', 'K': 'JL', 'J': 'IK', 'L': 'AK'}
G3 = (V3, E3)


###################################################

#tests
def test1():
    """test for dfs()"""
    assert dfs(G, "A") == ({'A': 1, 'C': 3, 'B': 2, 'E': 8, 'D': 24, 'G': 4, 'F': 13, 'I': 7, 'H': 5, 'K': 11, 'J': 9, 'M': 16, 'L': 12}, {'A': 26, 'C': 22, 'B': 23, 'E': 19, 'D': 25, 'G': 21, 'F': 14, 'I': 20, 'H': 6, 'K': 18, 'J': 10, 'M': 17, 'L': 15}, {'A': -1, 'C': 'B', 'B': 'A', 'E': 'I', 'D': 'A', 'G': 'C', 'F': 'L', 'I': 'G', 'H': 'G', 'K': 'E', 'J': 'E', 'M': 'K', 'L': 'K'})
    assert dfs(G, "I") == ({'A': 3, 'C': 5, 'B': 4, 'E': 2, 'D': 20, 'G': 6, 'F': 12, 'I': 1, 'H': 7, 'K': 10, 'J': 23, 'M': 9, 'L': 11}, {'A': 22, 'C': 18, 'B': 19, 'E': 25, 'D': 21, 'G': 17, 'F': 13, 'I': 26, 'H': 8, 'K': 15, 'J': 24, 'M': 16, 'L': 14}, {'A': 'E', 'C': 'B', 'B': 'A', 'E': 'I', 'D': 'A', 'G': 'C', 'F': 'L', 'I': -1, 'H': 'G', 'K': 'M', 'J': 'E', 'M': 'G', 'L': 'K'})
    assert dfs(G1, "A") == ({'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 20, 'F': 6, 'I': 15, 'H': 21, 'K': 7, 'J': 8, 'L': 10}, {'A': 24, 'C': 18, 'B': 19, 'E': 14, 'D': 17, 'G': 23, 'F': 13, 'I': 16, 'H': 22, 'K': 12, 'J': 9, 'L': 11}, {'A': -1, 'C': 'B', 'B': 'A', 'E': 'D', 'D': 'C', 'G': 'A', 'F': 'E', 'I': 'D', 'H': 'G', 'K': 'F', 'J': 'K', 'L': 'K'})
    assert dfs(G1, "J") == ({'A': 5, 'C': 3, 'B': 4, 'E': 15, 'D': 2, 'G': 6, 'F': 16, 'I': 10, 'H': 7, 'K': 17, 'J': 1, 'L': 18}, {'A': 12, 'C': 14, 'B': 13, 'E': 22, 'D': 23, 'G': 9, 'F': 21, 'I': 11, 'H': 8, 'K': 20, 'J': 24, 'L': 19}, {'A': 'B', 'C': 'D', 'B': 'C', 'E': 'D', 'D': 'J', 'G': 'A', 'F': 'E', 'I': 'A', 'H': 'G', 'K': 'F', 'J': -1, 'L': 'K'})
    print ("all tests passed")
    
def test2():
    """test for articulation_points()"""
    assert articulation_points(G) == ['A', 'E']
    assert articulation_points(G1) == ['A', 'D']
    assert articulation_points(G2) == ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    assert articulation_points(G3) == []
    print ("all tests passed")
    
