from PIL import ImageGrab, Image
from string import printable
import time
import mouse

d = 0.3

tubesAmount2pos = {
    11:
        [
            (756, 485), # 0

            (797, 760), # 1

            82,  # Horizontal distance between 2 tubes
            45,  # Vertical distance between 2 tubes
            6    # Amount of tubes in the upper row
        ],
    9:
        [
            (756, 471), # 0
            (807, 808), # 1

            100,
            55,
            5
        ],

    14:
        [
            (746, 484), # 0
            (746, 754), # 1

            70,
            45,
            7
        ],

    7:
        [
            (755, 470),
            (825, 810),

            135,
            60,
            4
        ]
}

def getPixel():
    im = ImageGrab.grab()
    def f(x, y):
        r, g, b = im.getpixel((x, y))
        return '%02x%02x%02x' % (r, g, b)
    return f

def getTubes(n):
    p = iter(printable)
    color2letter = {

    }
    # Assume 4 balls in each tube
    [tube1x, tube1y], [tube2x, tube2y], hd, vd, ntubesup = tubesAmount2pos[n]

    getpixel = getPixel()
    # Get the color of the first row
    tubes = []
    for i in range(ntubesup):
        tube = []
        for j in range(4):
            x = tube1x + i * hd
            y = tube1y - j * vd
            print("Getting pixel at:", x, y, end="    ")
            pixval = getpixel(x, y)
            pixval = pixval[:4]
            if pixval[0:2] == pixval[2:4]:# == pixval[4:6]:
                break
            # mouse.move(x, y)
            # time.sleep(0.7)
            if pixval not in color2letter:
                color2letter[pixval] = next(p)
            print(pixval, color2letter[pixval])
            tube.append(color2letter[pixval])
        print("--------")
        tubes.append(''.join(tube))

    # Get the color of the second row
    print("Getting second row")
    for i in range(n-ntubesup):
        tube = []
        for j in range(4):
            x = tube2x + i * hd
            y = tube2y - j * vd
            print("Getting pixel at:", x, y, end="  ")
            pixval = getpixel(x, y)
            pixval = pixval[:4]
            if pixval[0:2] == pixval[2:4]:# == pixval[4:6]:
                break

            if pixval not in color2letter:
                color2letter[pixval] = next(p)
            print(pixval, color2letter[pixval])

            tube.append(color2letter[pixval])
        print("--------")
        tubes.append(''.join(tube))
    return tubes

def moveOnScreen(n, fromtube, totube):
    [tube1x, tube1y], [tube2x, tube2y], hd, vd, ntubesup = tubesAmount2pos[n]
    if fromtube < ntubesup:
        x1 = tube1x + fromtube * hd
        y1 = tube1y
    else:
        x1 = tube2x + (fromtube - ntubesup) * hd
        y1 = tube2y

    if totube < ntubesup:
        x2 = tube1x + totube * hd
        y2 = tube1y
    else:
        x2 = tube2x + (totube - ntubesup) * hd
        y2 = tube2y

    mouse.move(x1, y1)
    time.sleep(d)
    mouse.click()
    time.sleep(d)
    mouse.move(x2, y2)
    time.sleep(d)
    mouse.click()
    time.sleep(d)

def figure_out_amount_of_tubes():
    import numpy as np
    n = 0

    for k in range(2):
        if k == 0:
            im = ImageGrab.grab(bbox=(715, 400, 1210, 410))
        else:
            im = ImageGrab.grab(bbox=(715, 730, 1210, 740))
        imarr = np.array(im)

        j = 0
        while j < len(imarr[0]):
            if tuple(imarr[0][j]) == (0xbb, 0xbb, 0xbb):
                j += 10
                n += 1
            j += 1

    return n/2
