import numpy as np
data = np.loadtxt("inputs/input1.txt",dtype=int)
dataSize = len(data)

def part1():
     isBiggerCounter = 0
     currentValue = np.inf
     for i in range(dataSize):
          if currentValue < data[i]:
               isBiggerCounter += 1
          currentValue = data[i]
     print(isBiggerCounter)

def oneliner():
     data = np.loadtxt("inputs/input1.txt",dtype=int); print(sum([data[i]>data[i-1] for i in range(1,len(data))]))
     #print(sum([np.loadtxt("inputs/input1.txt",dtype=int)[i]>np.loadtxt("inputs/input1.txt",dtype=int)[i-1] for i in range(1,len(np.loadtxt("inputs/input1.txt",dtype=int)))]))
def part2():
     isBiggerCounter = 0
     lastSum = np.inf
     currentSum = 0

     for i in range(1,dataSize-1):
          currentSum = data[i-1]+data[i]+data[i+1]
          if currentSum > lastSum:
               isBiggerCounter += 1
          lastSum = currentSum
     print(isBiggerCounter)

oneliner()