import sys
import math

#turns input file into a list
def parseFile(filename):
    inputList = [ ]
    infile = open(filename, 'r')
    for line in infile:
        inputList.append(int(line))

    print('List: ', inputList)
    return inputList

#merging and counting the inversions
def MergeCount(B, C):
    i = j = count = 0
    D = [] #output

    print('B is ', B)
    print('C is ', C)
    while i < len(B) and j < len(C):
        print("i = ", i)
        print("j = ", j)
        if B[i] < C[j] :
            D.append(B[i])
            count += (len(B)-i)
            i += 1
            
        else:   #B[i] <= C[j]
            D.append(C[j])
            j += 1
            

    rem = B[i:] + C[j:]
    print('rem  ', rem)
    D.extend(rem)
    print(D)
    print('count is ', count)
            
    return [count, D]

#recursive function to split the list
def splitSort(myList):
    n = len(myList)
    if n == 1:
        return [0,myList]
    
    x = splitSort(list(myList[:math.ceil(n/2)]))    #list B
    y = splitSort(list(myList[math.ceil(n/2):]))  #list C
    z = MergeCount(x[1], y[1])
    return [x[0]+y[0]+z[0], z[1]]




numInversions = 0
    
filename = sys.argv[1]

myList = parseFile(filename)

answer = splitSort(myList)
inversions = answer[0]
finalList = answer[1]

print('Number of inversions: ', inversions)

print('Sorted list: ', finalList)


