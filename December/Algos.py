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
#    for i in range(len(array) -1 ):
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


def ValidSub(array,sequence):
   # aIdx = 0
   sIdx = 0
   for value in array:
      if sIdx == len(sequence):
         break
      if sequence[sIdx] == value:
         sIdx += 1
   return sIdx == len(sequence)

   # while aIdx < len(array) and sIdx < len(sequence):
   #    if array[aIdx] == sequence[sIdx]:
   #       sIdx +=1
   #    aIdx += 1
   # return sIdx == len(sequence)

print(ValidSub([5, 1, 22, 25, 6, -1, 8, 10],[1, 6, -1, 10, 11, 11, 11, 11]))