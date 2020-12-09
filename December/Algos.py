# def isValidSubsequence (sequence, array):
#    # seqIdx = 0
#    # for value in array:
#    #    if seqIdx == len(sequence):
#    #       break
#    #    if sequence[seqIdx] == value:
#    #       seqIdx += 1
#    # return seqIdx == len(sequence)

#    # OR

#    # arrIdx = 0
#    # seqIdx = 0
#    # while arrIdx < len(array) and seqIdx < len(sequence):
#    #    if sequence[seqIdx] == array[arrIdx]:
#    #       seqIdx += 1
#    #    arrIdx += 1
#    # return seqIdx == len(sequence)

# print(isValidSubsequence([-1,6,-1,10],[5,1,22,25,6,-1,8,10]))


# def threeSum(array, targetSum):
#    array.sort()
#    newArr = []
#    for i in range(len(array) -2 ):
#       left = i + 1
#       right = len(array) -1
#       while left < right:
#          totalSum = array[i] + array[left] + array[right]
#          if totalSum == targetSum:
#             newArr.append([array[i], array[left], array[right]])
#             left += 1
#             right -=1
#          elif totalSum < targetSum:
#             left += 1
#          elif totalSum > targetSum:
#             right -= 1
#    return newArr

# print(threeSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15],18))


# def ValidSub(array,sequence):
#    # aIdx = 0
#    sIdx = 0
#    for value in array:
#       if sIdx == len(sequence):
#          break
#       if sequence[sIdx] == value:
#          sIdx += 1
#    return sIdx == len(sequence)

#    # while aIdx < len(array) and sIdx < len(sequence):
#    #    if array[aIdx] == sequence[sIdx]:
#    #       sIdx +=1
#    #    aIdx += 1
#    # return sIdx == len(sequence)

# print(ValidSub([5, 1, 22, 25, 6, -1, 8, 10],[1, 6, -1, 10, 11, 11, 11, 11]))

# dic = {"1" : [3,4]}
# dic = {"s" : [1,2]}
# for key in dic:
#    print(dic[key])

# def moveToEnd (array, target):
#    l = 0
#    r = len(array) - 1
#    while l < r:
#       if array[r] == target:
#          r -= 1
#       if array[l] != target:
#          l += 1
#       if array[r] != target and array[l] ==target:
#          temp = array[r]
#          array[r] = array[l]
#          array[l] = temp
#          l += 1
#          r -= 1
#    return array
# print(moveToEnd([1, 3, 3, 4, 5, 7, 8, 4, 10, 11, 12, 5, 5, 5, 5, 5, 5],5))

# def smallestAbsoluteDifference(arrayOne, ArrayTwo):
#    arrayOne.sort()
#    ArrayTwo.sort()
#    idxOne = 0
#    idxTwo = 0
#    smallest = float("inf")
#    current = float("inf")
#    smallestPair = []
#    while idxOne < len(arrayOne) and idxTwo < len(ArrayTwo):
#       firstNum = arrayOne[idxOne]
#       secondNum = ArrayTwo[idxTwo]
#       if firstNum < secondNum:
#          current = secondNum - firstNum
#          idxOne += 1
#       elif secondNum < firstNum:
#          current = firstNum - secondNum
#          idxTwo += 1
#       else:
#          return [firstNum, secondNum]
#       if smallest > current:
#          smallest = current
#          smallestPair = [firstNum, secondNum]
#    return smallestPair
# print(smallestAbsoluteDifference([10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]))

# def isMontotonic(array):
#    goesUp = True
#    goesDown = True
#    for i in range (1, len(array)):
#       if array[i] < array[i-1]:
#          goesUp = False
#       if array[i] > array[i-1]:
#          goesDown = False
#    return goesUp or goesDown

# print(isMontotonic([1,2,3,4,5,7,8,8,8,8,9,3]))

def spiralTraverse(array):
   ending = []
   startRow, endRow = 0, len(array) - 1
   startColumn, endColumn = 0, len(array[0]) - 1

   while startRow <= endRow and startColumn <= endColumn:
      for col in range(startColumn, endColumn + 1):
         ending.append(array[startRow][col])

      for row in range(startRow + 1, endRow + 1):
         ending.append(array[row][endColumn])

      for col in reversed(range(startColumn,endColumn)):
         ending.append(array[endRow][col])
      
      for row in reversed(range(startRow + 1, endRow)):
         ending.append(array[row][startColumn])
      
      startRow +=1
      endRow -=1
      startColumn +=1
      endColumn -= 1

   return ending
print(spiralTraverse([[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]))