#hw3.py v1.0
#Grant Ludwig
#5/1/19

import sys

def readFile(fileName):
    firstLine = True
    numBlocks = 0
    namedList = []
    heapList = []
    for line in open(fileName):
        line = line.rstrip()
        if firstLine:
            numBlocks = int(line)
            firstLine = False
        else:
            point, pointed = line.split(',')
            try:
                #int(point)
                heapList.append((int(point), int(pointed)))
            except ValueError:
                namedList.append((point, int(pointed)))
    return (numBlocks, namedList, heapList)

fileName = sys.argv[1]
numBlocks, namedList, heapList = readFile(fileName)
print(numBlocks, namedList, heapList)