import sympy
from math import *

def ignoreableMultiplicator(x, start, finish, ignore, xCoords):
    result = 1
    for i in range(start, finish):
        if i == ignore:
            continue
        result *= (x - xCoords[i])
    return result

def main():
    x = sympy.Symbol('x')
    coordDict = dict()

    print('Input your coordinates like this: "x y" (Input nothing to stop inputting.)')
    while True:
        inp = input('>>>')
        if not inp:
            break
        xCoord, yCoord = inp.split()
        xCoord, yCoord = eval(xCoord), eval(yCoord)
        coordDict[xCoord] = yCoord

    xCoords = tuple(coordDict.keys())
    N = len(xCoords)
    output = 0

    for k in range(N):
        xk = xCoords[k]
        output += coordDict[xk] * (x - xk + 1) * ignoreableMultiplicator(x, 0, N, k, xCoords) / ignoreableMultiplicator(xk, 0, N, k, xCoords)

    print('Unsimplified: ' + str(output).replace('**', '^'))
    output = sympy.simplify(output)
    output = str(output)
    print("Simplified: " + output.replace('**', '^'))


if __name__ == '__main__':
    main()