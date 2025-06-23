import math as m
import random


def insertPath(a, b, c=0, d=0, e=0):
    global pathToVictory
    pathToVictory.append([a, b, c, d, e])
    global p
    p += 1


def printComb(a, b, c=0, d=0, e=0):
    print(f"settlments:{a} cities:{b} vp:{c}", end=" ")
    if d:
        print("Biggest army", end=" ")
    if e:
        print("Longest road", end=" ")
    print("\n")


def generateWins():
    for i in range(6):
        for j in range(5):
            if i + j >= 2:
                for k in range(6):
                    if i + 2 * j + k >= 6:
                        if 10 <= i + 2 * j + k <= 11:
                            insertPath(i, j, k)
                        elif i + 2 * j + k == 8 or i + 2 * j + k == 9:
                            insertPath(i, j, k, 1, 0)
                            insertPath(i, j, k, 0, 1)
                        elif i + 2 * j + k == 6 or i + 2 * j + k == 7:
                            insertPath(i, j, k, 1, 1)


def calculateScores():
    global pathToVictory
    global scores
    for i in range(len(pathToVictory)):
        scores.append(10)
        if pathToVictory[i][0] + pathToVictory[i][1] >= 5:
            scores[i] /= (pathToVictory[i][0] + pathToVictory[i][1])
        # if win[i][1]
        #     win[i][5] /= 2
        for j in range(pathToVictory[i][2]):
            scores[i] *= (5 - j) / (25 - j)
        if pathToVictory[i][3]:
            for j in range(3):
                scores[i] *= (14 - j) / (25 - j)
        if pathToVictory[i][4]:
            scores[i] /= 3
    total = sum(scores)
    scores = [x / total for x in scores]


def mergeScoresPath():
    global score
    global pathToVictory
    merged = [[scores[i], pathToVictory[i]] for i in range(len(pathToVictory))]
    merged = sorted(merged, key=lambda row: row[0], reverse=True)
    return merged


def calcNoOfDraws(n, b):
    if b:
        return 4 if n == 1 else 6 if n == 2 else 7
    if n > 0:
        return m.ceil(n * 25 / 6)
    return 0


def calculateWinCon(list):
    settlments = 0
    cities = 0
    roads = 0
    cards = 0
    for row in list:
        settlments += row[0] * row[1][0]
        cities += row[0] * row[1][1]
        roads += row[0] * row[1][4] * 2
        x = 0
        x += row[0] * (3 * row[1][1] + 2 * row[1][0])
        cards += row[0] * calcNoOfDraws(row[1][2], row[1][3])
    settlments += cities - 2
    roads += settlments * 2 - 2
    print(settlments, cities, roads, cards)
    return [settlments, cities, roads, cards]

def calculateResources(list):
    return [m.ceil(list[0]) + m.ceil(list[2]), m.ceil(list[0]) + m.ceil(list[2]), m.ceil(list[0]) + m.ceil(list[3]),
            m.ceil(list[0]) + m.ceil(list[1]) * 2 + m.ceil(list[3]), m.ceil(list[1]) * 3 + m.ceil(list[3])]
    # return [list[0]+list[2],list[0]+list[2],list[0]+list[3],list[0]+list[1]*2+list[3],list[1]*3+list[3]]


def simulate_until_x_vp_or_y_knights(x_vp=2, y_knights=3):
    deck = (
            ['K'] * 14 +  # Knights
            ['V'] * 5 +  # Victory Points
            ['O'] * 6  # Other (Monopoly, RB, YoP)
    )
    random.shuffle(deck)
    nvp = 0
    nk = 0
    for i, card in enumerate(deck, 1):
        if card == 'V':
            nvp += 1
        elif card == 'K':
            nk += 1
        if nvp >= x_vp or nk >= y_knights:
            return i
    return 25


def simulateDraws(N, a, b):
    results = [simulate_until_x_vp_or_y_knights(a, b) for _ in range(N)]
    expected_draws = sum(results) / N
    print(f"Expected draws until {a} VP or {b} Knights: {expected_draws:.2f}")


pathToVictory = []
scores = []
p = 0
generateWins()
calculateScores()
sortedPaths = mergeScoresPath()
print(p)
resources = calculateWinCon(sortedPaths)
print("lu, cl, sh, wh, ore", calculateResources(resources), sep="\n")
