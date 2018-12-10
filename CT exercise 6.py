import random

def wordcount(text):
    counter = {}
    lst = text.split(' ')
    for word in lst:
        if word in counter:
            counter[word] += 1
        else:
            counter[word]=1

    for item in counter:
        print (item + ' appeared ' + str(counter[item])+ ' time(s).')
    
def lookup(book):

    first = input('First Name: ')
    last = input('Last Name: ')

    person = (first, last)
    
    if person in book:
        return book[person]
    else:
        return False

def game(r,c):
    field = []
    for i in range (0,r):
        field.append(['_'])
        for j in range (0,c):
            field[i].append('_')

    import random
    field[random.randrange(0,r)][random.randrange(0,c)] = 'O'

    x = int(input('x coordinate of the bomb: '))
    y = int(input('y coordinate of the bomb: '))

    if field[x][y] == 'O':
        found = True
    else:
        found = False

    field[y-1][x-1]= 'X'


    for i in range(0,r):
        for j in range(0,c):
            print(field[i][j], end=' ')
        print('\n')

    if found: print('You found the bomb well done!')
    else: print ("You didn't find the bomb :(")

def reverse(book):
    return {phone:name for name, phone in book.items()}

mir = {'b':'d','d':'b','i':'i','l':'l','m':'m','n':'n','o':'o','p':'q','q':'p','t':'t','u':'u','v':'v','w':'w','x':'x'}

def mirror(s):
    string = list(s)
    for i in range (0, len(string)):
        if len(string)-(2*(i+1)) == 0:
            return ''.join(string)
        if len(string)-(2*(i+1)) == -1:
            c = string[i]
            if c in mir:
                string[i] = mir[c]
                return ''.join(string)
            else:
                return 'INVALID'
        c = string[i]
        string[i] = string[-(i+1)]
        string[-(i+1)] = c

def friends(friendships):
    'infers networks of mutual friends from a list of pairs of friends'
    network_dict = {}  # build a dictionary detailing the network a person is in
    net_name = 0       # initialize a network name
    for pair in friendships:  # check each pair of friends in the list
        found0 = False
        found1 = False
        for friend_network in network_dict:   # check if each person has already
            if friend_network == pair[0]:     #   been found
                found0 = True
            if friend_network == pair[1]:
                found1 = True
        if found0 == True and found1 == True: # if both exist, merge networks
            merged_net = network_dict[pair[0]]  # delete network deleted_net and
            deleted_net = network_dict[pair[1]] #   replace it with merged_net
            for network_person in network_dict:
                if network_dict[network_person] == deleted_net:
                    network_dict[network_person] = merged_net
        elif found0 == True and found1 == False: # if only one exists, add new person
            network_dict.update({pair[1]:network_dict[pair[0]]})
        elif found0 == False and found1 == True:
            network_dict.update({pair[0]:network_dict[pair[1]]})
        else:                                    # if both are new, create a new network
            net_name = net_name + 1              # build a new network name
            network_dict.update({pair[0]:net_name,pair[1]:net_name})
    return network_dict





def string_to_list_of_ints(string):
    string = string.replace(" ","")
    string = string.replace("[","")
    string = string.replace("]","")
    lst = string.split(",")
    out =  []
    for i in range(0, len(lst)):
        out.append(int(lst[i]))

    return out

def man_walk():
    M = []
    file = open('walk.txt', 'r')
    for i in range(0,6+1):
        lst = string_to_list_of_ints(file.readline())
        if len(lst) == 9:
            M.append(lst)
        else:
            M.append([0,0,0,0,0,0,0,0,0])
            
    file.read(17)
    i = 0
    j = 0
    x = int(file.read())+1
    while True:
        M[i][j] += 1
        moves = []

        if i - 1 >= 0:
            moves.append([i-1,j])
        if j - 1 >= 0:
            moves.append([i,j-1])
        if i + 1 <= 6:
            moves.append([i+1,j])
        if j + 1 <= 8:
            moves.append([i,j+1])
          

        move = random.choice(moves)
        i = move[0]
        j = move[1]
        
        if i == 6 and j == 8:
            M[6][8] += 1
            break

    file = open('walk.txt', 'w')
    for i in range(0,6+1):
        file.write(str(M[i]))
        file.write('\n')

    file.write('Number of walks: ' + str(x))
    file.close()
    
def big_walk():
    for i in range(0,500):
        man_walk()
        
    

def graph_walk(G,s,t):
    #G must be an adjacency matrix of G
    node = s
    x = 0
    while True:
        neighbours = []
        for i in range(0,len(G)):
            if G[s][i] >= 1:
                neighbours.append(i)

        if len(neighbours) == 0:
            break
        
        move = random.choice(neighbours)
        node = move
        x += 1

        G[s][node] += 1
        G[node][s] += 1
        if node == t:
            break

    file = open('graph.txt','w')
    for i in range(0, len(G)):
        file.write(str(G[i]))
        file.write('\n')

    file.write('Number of walks: ' +str(x))
    file.close()

    
    
        
    





    
