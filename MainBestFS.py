import time
from queue import PriorityQueue
import TubesDetector

class Tubes(list):
    def __init__(self, tubes, steps=None):
        super().__init__(tubes)
        self.tubes = tubes
        if steps is None:
            self.steps = []
        else:
            self.steps = steps

    def addStep(self, step):
        self.steps.append(step)

    def getSteps(self):
        return self.steps

TUBE_CAPACITY = 4
LAST = -1

def isValidMove(tubes, fromtube, totube):
    if fromtube == totube:
        return False

    if len(tubes[fromtube]) == 0 or len(tubes[totube]) >= TUBE_CAPACITY:
        return False

    # For making him less retarded
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

def isWinningTubes(tubes):
    for tube in tubes:
        if len(tube) == 0:
            continue
        if len(tube) != TUBE_CAPACITY:
            return False
        if tube.count(tube[0]) != TUBE_CAPACITY:
            return False
    return True

def move(tubes, fromtube, totube):
    t = Tubes(tubes.copy(), tubes.getSteps().copy())
    t[totube] += t[fromtube][LAST]
    t[fromtube] = t[fromtube][:-1]
    return t

def get_next_tubes(tubes):
    for fromtube in range(len(tubes)):
        for totube in range(len(tubes)):
            if fromtube == totube:
                continue
            if isValidMove(tubes, fromtube, totube):
                m = move(tubes, fromtube, totube)
                yield fromtube, totube, m

def n_same_balls(tube, n):
    return len(tube) == n and tube.count(tube[0]) == n

def static_eval(tubes):
    if isWinningTubes(tubes):
        return 1000000

    score = 0
    for tube in tubes:
        if n_same_balls(tube, 4):
            score += 10
        elif n_same_balls(tube, 3):
            score += 5
        elif n_same_balls(tube, 2):
            score += 2
        else:
            for i in range(len(tube)-1):
                for j in range(i+1, len(tube)):
                    if tube[i] == tube[j]:
                        break
                    score -= 1
    return score

def get_winning_moves(tubes):
    cache = []
    q = PriorityQueue()
    q.put((static_eval(tubes), tubes))

    while True:
        p, t = q.get()

        if isWinningTubes(t):
            print("WON", t)
            return t.getSteps()

        print(p, t)

        for *step, m in get_next_tubes(t):
            if set(m) in cache:
                continue
            m.addStep(step)
            cache.append(set(m))
            q.put((static_eval(m), m))


n = int(input("n="))
time.sleep(3)
tubes = Tubes(TubesDetector.getTubes(n))

for step in get_winning_moves(tubes):
    fromtube, totube = step
    TubesDetector.moveOnScreen(n, fromtube, totube)