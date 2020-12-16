# want to find two numers that add up to target number
# if there are no solutions return an empty array
# sort array so largest number is at the right and lowest at the left
# use to index pointers to move
# if the the sum is less than the target we move left pointers
# if sum is greater than target we move the right

# def twoSum(array, target):
#    array.sort()
#    lIdx = 0
#    rIdx = len(array) - 1

#    while lIdx < rIdx:
#       current = array[lIdx] + array[rIdx]
#       if current == target:
#          return [array[lIdx], array[rIdx]]
#       elif current < target:
#          lIdx += 1
#       elif current > target:
#          rIdx -= 1
#    return []

# print(twoSum([1,3,5,8,9,2,6,4], 18))

# find out if subset array is in the main array
# in order to be a subset of the arary the elements must appear 
# in the same order as they do in the main array.
# create to pointer variables that keep track of the index of each array
# as we go through the main array we check the current element to teh element of the subset
# if they match we add 1 to both indexes.  If they do not match we only add 1 to the main arrays index
# we'll know if the sequence array is a subset of the main array if the length of hte sequence index is == tp the length 
# of the sequence array

# def subSequence(array, sequence):
#    main = 0
#    sub = 0

#    while main < len(array) and sub < len(sequence):
#       if array[main] == sequence[sub]:
#          sub += 1
#       main +=1
#    return sub == len(sequence)
# print(subSequence([1,2,5,6,7,8,12,54,63,25],[5,8,25,63]))

# get the sum of three numbers that == the target 
# if they == the target put them in an array inside an array
# start by sorting the array
# create empty array
# for Loop you want the current index and two pointers, 
# one starting at the element directly to the right and one on the last element
# run a while Loop
# if they == the targetSum add all three into an array and append it into the empty arrayOne
# if sum is less than targertsum move left by increasing 1
# if sum greater than target sum move right by decreasing 1

# def threeNumberSum(array, targetSum):
#    array.sort()
#    newArray = []
#    for i in range(len(array)- 2):
#       l = i + 1
#       r = len(array) - 1
       
#       while l < r:
#          current = array[i] + array[l] + array[r]
#          if current == targetSum:
#             newArray.append([array[i], array[l], array[r]])
#             l += 1
#             r -= 1
#          elif current < targetSum:
#             l += 1
#          elif current > targetSum:
#             r -= 1
#    return newArray
# print(threeNumberSum([12,3,1,2,-6,5,-8,6],0))

# def moveElmenttoEnd(array, toMove):
#    lIdx = 0
#    rIdx = len(array) - 1
#    while lIdx < rIdx :
#       if array[rIdx] == toMove:
#          rIdx -= 1
#       if array[lIdx] != toMove:
#          lIdx += 1
#       if array[lIdx] == toMove and array[rIdx] != toMove:
#          temp = array[rIdx]
#          array[rIdx] = array[lIdx]
#          array[lIdx] = temp
#          lIdx += 1
#          rIdx -= 1
#    return array
# print(moveElmenttoEnd([2,1,2,4,2,2,3,4,2],4))

def smallestAbsoluteValue(arrayOne, arrayTwo):
   arrayOne.sort()
   arrayTwo.sort()
   oneIdx = 0
   twoIdx = 0
   current = float("inf")
   smallest = float("inf")
   last = []
   while oneIdx < len(arrayOne) and twoIdx < len(arrayTwo):
      numOne = arrayOne[oneIdx]
      numTwo = arrayTwo[twoIdx]
      if numOne < numTwo:
         current = numTwo - numOne
         oneIdx += 1
      elif numTwo < numOne:
         current = numOne - numTwo
         twoIdx += 1
      else:
         return [numOne, numTwo]
      if smallest > current:
         smallest = current
         last = [numOne, numTwo]
   
   return last

print(smallestAbsoluteValue([-1,5,10,3,28,20], [135,134,26,15,17]))
