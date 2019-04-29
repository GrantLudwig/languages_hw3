#hw3.py v1.0
#Grant Ludwig
#5/1/19

import sys

def readFile(fileName):
    firstLine = True
    pointerList = []
    blockList = []
    for line in open(fileName):
        line = line.rstrip()
        if firstLine:
            for _ in range(int(line)):
                blockList.append([])
            firstLine = False
        else:
            point, pointed = line.split(',')
            try:
                blockList[int(point)].append(int(pointed))
            except ValueError:
                pointerList.append((point, int(pointed)))
    return (pointerList, blockList)

def pointing(bList, blockNum, marked):
    for block in bList[blockNum]:
        if not marked[block]:
            marked[block] = True
            pointing(bList, block, marked)

def markSweep(pList, bList):
    markedNodes = []
    for _ in range(len(bList)):
        markedNodes.append(False)
    #from pointers
    for _, blockNum in pList:
        markedNodes[blockNum] = True
        pointing(bList, blockNum, markedNodes)
    print(markedNodes)

    


fileName = sys.argv[1]
pointerList, blockList = readFile(fileName)
print(blockList)
markSweep(pointerList, blockList)