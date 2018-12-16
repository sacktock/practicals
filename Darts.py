
#Finds the numeric value of a darts score (T20 would be 3x20)
def getScoreFromString(string):
    char = string[0]
    num = int(string[1:])
    if char == 'S':
        return num
    elif char == 'D':
        return num*2
    elif char == 'T':
        return num*3
    else:
        return 0

#Returns a list of all the possible scores
def getScoresList():
    scores = []
    scores.append("S0")
    for i in range (1,21):
        scores.append("S"+str(i))
        scores.append("D"+str(i))
        scores.append("T"+str(i))

    scores.append("S25")
    scores.append("D25")
    return scores

#Returns a list of all the double scores
def getDoublesList():
    scores = []
    for i in range (1,21):
        scores.append("D"+str(i))

    scores.append("D25")
    return scores

#Calculates the number of different checkouts for the input score.
def numCombinations(score):
    if score>170: return 0
    x=0
    doubles = getDoublesList()
    for double in doubles:
        tempScore = score
        tempScore = tempScore - getScoreFromString(double)
        if tempScore == 0:
            x=x+1
        else:
            x=x+combinationsVector[tempScore-1]
    return x

#Creates a vector of number of combinations of 2 darts
#that can produce each number up to 170.
def getScoreCombinationsVector():
    combinationsVector = []
    for i in range (1,171):
        combinationsVector.append(tryScoreCombinations(i))
    return combinationsVector

#Calculates how many combinations of 2 darts can produce the input score.
def tryScoreCombinations(score): 
    x=0
    scores = getScoresList()
    while len(scores) > 0:
        scoreX = scores[0]
        for scoreY in scores:
            tempScore = score
            tempScore = tempScore - getScoreFromString(scoreX) - getScoreFromString(scoreY)
            if tempScore == 0:
                x=x+1
        scores.remove(scoreX)
    return x

combinationsVector = getScoreCombinationsVector()

x=0

#Sums all the checkout combinations of scores below 100
for i in range (2,100):
    x=x+numCombinations(i)

print x

