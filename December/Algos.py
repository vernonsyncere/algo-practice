import math
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
# BRUTE FORCE
# def getProduct(array):
   
#    # # places a 1 at every element in the product array and matches the length of 
#    # # the product array to the array passed in
#    # product = [1 for _ in range(len(array))]
#    # for i in range (len(array)):
#    #    runningProduct = 1
#    #    for j in range(len(array)):
#    #       if i != j:
#    #          runningProduct *= array[j]
#    #    product[i] = runningProduct
#    # return product



# print(getProduct([5,1,4,2]))

# O(n) time | O(n) space
# def getProduct(array):
   
#    #  places a 1 at every element in the product array and matches the length of 
#    #  the product array to the array passed in
#    product = [1 for _ in range(len(array))]
#    leftProducts = [1 for _ in range(len(array))]
#    rightProducts =[1 for _ in range(len(array))]

#    leftRunningProduct = 1
#    for i in range(len(array)):
#       leftProducts[i] = leftRunningProduct
#       leftRunningProduct *= array[i]
   
#    rightRunningProduct = 1
#    for j in reversed(range(len(array))):
#       rightProducts[j] = rightRunningProduct
#       rightRunningProduct *= array[j]

#    for i in range(len(array)):
#       product[i] = leftProducts[i] * rightProducts[i]
#    return product



# print(getProduct([5,1,4,2]))

# def getProduct(array):
   
#    #  places a 1 at every element in the product array and matches the length of 
#    #  the product array to the array passed in
#    product = [1 for _ in range(len(array))]


#    leftRunningProduct = 1
#    for i in range(len(array)):
#       product[i] = leftRunningProduct
#       leftRunningProduct *= array[i]
   
#    rightRunningProduct = 1
#    for j in reversed(range(len(array))):
#       product[j] *= rightRunningProduct
#       rightRunningProduct *= array[j]

#    return product





# print(getProduct([5,1,4,2]))

# def spiralTraverse(array):
#    spiral = []
#    sRow, eRow = 0, len(array) - 1
#    sCol, eCol = 0, len(array[0]) -1

#    while sRow <= eRow and sCol <= eCol:
#       for col in range(sCol, eCol + 1):
#          spiral.append(array[sRow][col])

#       for row in range(sRow + 1, eRow + 1):
#          spiral.append(array[row][eCol])

#       for col in reversed(range(sCol,eCol )):
#          if sRow == eRow:
#             break
#          spiral.append(array[eRow][col])

#       for row in reversed(range(sRow + 1 , eRow)):
#          if sCol == eCol:
#                 break
#          spiral.append(array[row][sCol])

#       sRow += 1
#       eRow -= 1
#       sCol += 1
#       eCol -= 1

#    return spiral

# print(spiralTraverse([[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]))

# def longestPeak(array):
#    longPeak = 0
#    i = 1
#    while i < len(array) - 1:
#       currentPeak = array[i-1] < array[i] and array[i] > array[i+1]
#       if not currentPeak:
#          i += 1
#          continue
#       lIdx = i - 2
#       while lIdx <= 0 and array[lIdx] < array[lIdx + 1]:
#          lIdx -= 1
#       rIdx = i + 2
#       while rIdx < len(array) and array[rIdx] > array[lIdx - 1]:
#          rIdx += 1

#       newPeak = rIdx - lIdx - 1
#       longPeak = max(longPeak,newPeak)
#       i = rIdx
#    return longPeak
# print(longestPeak([1,2,3,3,4,0,10,6,5,-1,-3,2,3]))

# def longestPeak(array):
#    longestPeak = 0
#    i = 1
#    while i < len(array) - 1:
#       isPeak = array[i -1] < array[i] and array[i] > array[i + 1] 
#       if not isPeak:
#          i += 1
#          continue
#       leftIndex = i - 2
#       while leftIndex >= 0 and array[leftIndex] < array[leftIndex + 1]:
#          leftIndex -= 1
#       rightIndex = i + 2
#       while rightIndex < len(array) and array[rightIndex] < array[rightIndex - 1]:
#          rightIndex += 1
      
#       currentPeak = rightIndex - leftIndex - 1
#       longestPeak = max(longestPeak, currentPeak)
#       i = rightIndex
#    return longestPeak
# print(longestPeak([1,2,3,3,4,0,10,6,5,-1,-3,2,3]))


# way to check for a peak is to see if element directly to left and right are smaller than
# current element

# lIdx = currIdx -2
# while lIdx >=0 and array[liIdx] < array[lIdx + 1]:
#    lIdx -= 1
# rIdx = currIdx + 2 
# while rIdx < len(arr) and array[rIdx] < arr[Idx -1]:
#    rIdx += 1
# currentPeak = rIdx - lIdx - 1
# peakLength = max(peakLength,currentPeak)
# i = rIdx

# def peakLong(array):
#    maxPeak = 0
#    i = 1
#    while i < len(array) -1:
#       isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
#       if not isPeak:
#          i += 1
#          continue
#       leftIdx = i - 2
#       while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
#          leftIdx -= 1
#       rightIdx = i + 2
#       while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
#          rightIdx += 1
#       currentPeak = rightIdx - leftIdx - 1
#       maxPeak = max(maxPeak, currentPeak)
#       i = rightIdx
#    return maxPeak
# print(peakLong([1,2,3,3,4,0,10,6,5,-1,-3,2,3]))


   


