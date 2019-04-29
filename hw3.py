#hw3.py v1.0
#Grant Ludwig
#5/1/19

import sys

#returns tuple of pointerList and blockList
    #pointerList is a list of tuples
        #(pointer, heapBlock)
    #blockList is a list with lists that contain the blocks that the block points to
        #the list will have as many list as there are heapBlocks
        #each index of blockList represents that helpBlock number
        #[[heapBlock, heapBlock], ...]
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
            #if ValueError occurs, that means that the line is a pointer to a block
            try:
                blockList[int(point)].append(int(pointed))
            except ValueError:
                pointerList.append((point, int(pointed)))
    return (pointerList, blockList)

def finalOutput(markedList):
    marked = 'Marked nodes: '
    swept = 'Swept nodes: '
    for block in range(len(markedList)):
        if markedList[block]:
            marked += str(block) + ' '
        else:
            swept += str(block) + ' '
    print(marked)
    print(swept)

#Recursive function that goes through all the blocks a block points to
def pointing(bList, blockNum, marked):
    for block in bList[blockNum]:
        if not marked[block]:
            marked[block] = True
            pointing(bList, block, marked)

#Runs the markSweep algorithm
def markSweep(pList, bList):
    markedNodes = []
    for _ in range(len(bList)):
        markedNodes.append(False)
    for _, blockNum in pList:
        markedNodes[blockNum] = True
        pointing(bList, blockNum, markedNodes)
    finalOutput(markedNodes)

#Driver code
fileName = sys.argv[1]
pointerList, blockList = readFile(fileName)
markSweep(pointerList, blockList)