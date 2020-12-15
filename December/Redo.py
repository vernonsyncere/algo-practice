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

def subSequence(array, sequence):
   main = 0
   sub = 0

   while main < len(array) and sub < len(sequence):
      if array[main] == sequence[sub]:
         sub += 1
      main +=1
   return sub == len(sequence)
print(subSequence([1,2,5,6,7,8,12,54,63,25],[5,8,25,63]))