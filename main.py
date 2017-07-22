
from queue import PriorityQueue

def isGoalState(state):
    # goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    return state == goal

def getSuccessor(state):
    blank = state.index(0)

    top = blank - 3
    bottom = blank + 3
    left = blank - 1
    right = blank + 1

    legalMoves = []

    if blank not in [0, 3, 6]:
        legalMoves.append(left)
    if blank not in [0, 1, 2]:
        legalMoves.append(top)
    if blank not in [2, 5, 8]:
        legalMoves.append(right)
    if blank not in [6, 7, 8]:
        legalMoves.append(bottom)

    successor = []
    for move in legalMoves:
        copyState = state[:]
        copyState[blank], copyState[move] = copyState[move], copyState[blank]
        successor.append((copyState, move))

    return successor

def tostr(li):
    return ''.join([str(x) for x in li])


def heuristic (state):
    goalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    for position, number in enumerate(goalState):
        positionInState = state.index(number)
        rowOfGoalNumber = position // 3
        rowOfStateNumber = positionInState // 3

        colTraversal = abs(rowOfStateNumber - rowOfGoalNumber)

        lowerNumber = min(position, positionInState)
        highNumber = max(position, positionInState)

        rowTraversal = abs((lowerNumber + (3 * colTraversal) - highNumber))

        return rowTraversal + colTraversal

def aStarSearch (root):
    visited = set()
    fringe = PriorityQueue()
    fringe.put((0, (root, [], 0)))

    while fringe:
        node, path, cost = fringe.get()[1]
        if isGoalState(node):
            return path
        for successor, move in getSuccessor(node):
            if tostr(successor) not in visited:
                gx = cost + 1
                hx = heuristic(successor)
                fx = hx + gx
                fringe.put((fx, (successor, path + [move], gx)))

        visited.add(tostr(node))
    return []  

def PerformActions(state, moves):
    blank = state.index(0)

    for i, move in enumerate(moves):
        state[blank], state[move] = state[move], state[blank]
        blank = move
        
        print ("Move {}: {}".format(i, state))

def main():
    print ('Finding game region .... ')

    print ('Game region found, getting board configuration ....')
    root = [3,0,8,1,7,2,6,4,5]
    print ('The board configuration is ....')
    print (root)

    print ('Finding Solution for the current configuration ....')
    moves = aStarSearch(root)

    print ('The Solution is')
    print (moves)

    PerformActions(root, moves)
    
if __name__ == '__main__':
    main()