#adspractical17extra.py
#algorithms and data structures practical week 17
#matthew johnson 22 february 2013, last revised 15 february 2018

#####################################################

"""an extra question that has nothing to do with the algorithms from the
lectures, but gives some practice on thinking about graph algorithms"""

#define an example tree using adjacency lists 
V = "ABCDEFGHIJKLM"
E = {'A': 'BCD', 'C': 'AGH', 'B': 'AEF', 'E': 'BIJK', 'D': 'A',
    'G': 'C', 'F': 'BL', 'I': 'E', 'H': 'C', 'K': 'EM', 'J': 'E',
    'M': 'K', 'L': 'F'}
T = (V, E)

"""
in a tree, there is a unique path between each pair of vertices; the diameter
of a tree is the longest such path (the diameter of the example tree above is
6); write a function that takes a tree and returns its diameter

the function should be recursive; first, what is the diameter of a tree on 1
vertex? what if the tree has more vertices and you remove one of them
and split the tree into many smaller trees; what do you need to know about the
smaller trees to find the diameter of the larger tree? 
"""

def tree_diameter(tree):
    """given a tree as a pair, the vertex set and adjacency lists, return
    the diameter of the tree"""
    V, E = tree
    #complete the function here
    return #diameter

###################################################

#the following function might prove useful
def print_lists(G):
    """takes a graph with adjacency list representation and prints the lists"""
    V, E = G
    for vertex in V:
        n = ""
        for neighbour in E[vertex]:
            n += neighbour + ", " 
        print (vertex[0] + ": " + n[:-2])

###################################################

#tests        
V1 = "A"
E1 = {'A': ''}
T1 = (V1, E1)
V2 = "AB"
E2 = {'A': 'B', 'B': 'A'}
T2 = (V2, E2)
V3 = "ABC"
E3 = {'A': 'B', 'C': 'B', 'B': 'AC'}
T3 = (V3, E3)
V4 = "ABCD"
E4 = {'A': 'B', 'C': 'BD', 'B': 'AC', 'D': 'C'}
T4 = (V4, E4)
E4a = {'A': 'B', 'C': 'B', 'B': 'ACD', 'D': 'B'}
T4a = (V4, E4a)
V5 = "ABCDEFGHIJKLMNOPQR"
E5 = {'A': 'B', 'C': 'BD', 'B': 'AC', 'E': 'DF', 'D': 'CE', 'G': 'FH', 'F': 'EG', 'I': 'HJ', 'H': 'GI', 'K': 'JL', 'J': 'IK', 'M': 'LN', 'L': 'KM', 'O': 'NP', 'N': 'MO', 'Q': 'PR', 'P': 'OQ', 'R': 'Q'}
T5 = (V5, E5)
E5a = {'A': 'B', 'C': 'BD', 'B': 'ACG', 'E': 'DF', 'D': 'CE', 'G': 'BH', 'F': 'E', 'I': 'HJ', 'H': 'GI', 'K': 'JL', 'J': 'IK', 'M': 'LN', 'L': 'KM', 'O': 'NP', 'N': 'MO', 'Q': 'PR', 'P': 'OQ', 'R': 'Q'}
T5a = (V5, E5a)
def test():
    assert tree_diameter(T) == 6
    assert tree_diameter(T1) == 0
    assert tree_diameter(T2) == 1
    assert tree_diameter(T3) == 2
    assert tree_diameter(T4) == 3
    assert tree_diameter(T4a) == 2
    assert tree_diameter(T5) == 17
    assert tree_diameter(T5a) == 16
    print ("all tests passed")
