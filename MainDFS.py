import time
import mouse
from TubesDetector import getTubes, moveOnScreen, figure_out_amount_of_tubes
from time import sleep

TUBE_CAPACITY = 4
LAST = -1
next_button_pos = (980, 810)

def isWinningTubes(tubes):
    for tube in tubes:
        if len(tube) == 0:
            continue
        if len(tube) != TUBE_CAPACITY:
            return False
        if tube.count(tube[0]) != TUBE_CAPACITY:
            return False
    return True

def isValidMove(tubes, fromtube, totube):
    if fromtube == totube:
        return False

    if len(tubes[fromtube]) == 0 or len(tubes[totube]) >= TUBE_CAPACITY:
        return False

    # for making him less stupid
    if len(tubes[fromtube]) == 4 and tubes[fromtube].count(tubes[fromtube][0]) == 4:
        return False
    if len(tubes[fromtube]) == 3 and tubes[fromtube].count(tubes[fromtube][0]) == 3:
        return False
    # -----
    if len(tubes[totube]) == 0:
        return True

    if tubes[fromtube][LAST] != tubes[totube][LAST]:
        return False
    return True

def move(tubes, fromtube, totube):
    t = tubes.copy()
    t[totube] += t[fromtube][LAST]
    t[fromtube] = t[fromtube][:-1]
    return t

def get_next_tubes(tubes):
    for fromtube in range(len(tubes)):
        for totube in range(len(tubes)):
            if isValidMove(tubes, fromtube, totube):
                m = move(tubes, fromtube, totube)
                yield fromtube, totube, m

visited = []
def find_winning_moves(tubes):
    if isWinningTubes(tubes):
        return True, []
    if tubes in visited:
        return False, []

    visited.append(tubes)

    for fromtube, totube, t in get_next_tubes(tubes):
        print(t)
        iswin, mvs = find_winning_moves(t)
        if iswin:
            return True, [[fromtube, totube]] + mvs
    return False, []


class UnwinableError(Exception): pass

def win(n):
    sleep(3)
    tubes = getTubes(n)
    iswin, moves = find_winning_moves(tubes)
    if not iswin:
        raise UnwinableError("Unwinable")

    # moves = simplify_moves(moves)
    print(moves)
    for move in moves:
        fromtube, totube = move
        moveOnScreen(n, fromtube, totube)

sleep(10)
n = figure_out_amount_of_tubes()
win(n)
