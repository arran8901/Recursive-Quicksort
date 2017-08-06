#Func takes first 3 elements in partition
#and returns the middle element with its index
def middleElement(n1, i1, n2, n3):
  if (n2 <= n1 and n1 <= n3) or (n3 <= n1 and n1 <= n2):
    return [n1, i1]
  elif (n1 <= n2 and n2 <= n3) or (n3 <= n2 and n2 <= n1):
    return [n2, i1 + 1]
  elif (n1 <= n3 and n3 <= n2) or (n2 <= n3 and n3 <= n1):
    return [n3, i1 + 2]

def partition(x, y):
  if y - x > 0:
    if y - x > 2: #If there are 3+ elements to get a middle element;
      pivotInfo = middleElement(numList[x], x, numList[x + 1], numList[x + 2])
      # pivotInfo[pivot, pivotIndex]
    else: #Otherwise just take the first element
      pivotInfo = [numList[x], x]
    
    #If the pivot is not at the start (index 0), move it there
    if pivotInfo[1] != x:
      holder = numList[x]
      numList[x] = pivotInfo[0]
      numList[pivotInfo[1]] = holder
      pivotInfo[1] = x
    
    sorted = True #Assume sorted until proved otherwise
    
    #Iterate through all subsequent elements
    for i in range(x + 1, y):
      #If smaller than or equal to pivot, move it before the pivot 
      #and sorted is false. Otherwise just keep it after the pivot
      if numList[i] <= pivotInfo[0]:
        numList.insert(x, numList[i])
        numList.pop(i + 1)
        pivotInfo[1] += 1
        sorted = False
    
    #Return if sorted. Otherwise start another partition
    if sorted:
      return
    
    partition(x, pivotInfo[1])
    partition(pivotInfo[1], y)

#Putting numbers from file into array numList
numList = []
file = open("numbers.txt", "r")
for line in file:
  numList.append(int(line))

partition(0, len(numList))

print numList