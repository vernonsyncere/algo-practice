# want to find two numers that add up to target number
# if there are no solutions return an empty array
# sort array so largest number is at the right and lowest at the left
# use to index pointers to move
# if the the sum is less than the target we move left pointers
# if sum is greater than target we move the right

def twoSum(array, target):
   array.sort()
   lIdx = 0
   rIdx = len(array) - 1

   while lIdx < rIdx:
      current = array[lIdx] + array[rIdx]
      if current == target:
         return [array[lIdx], array[rIdx]]
      elif current < target:
         lIdx += 1
      elif current > target:
         rIdx -= 1
   return []

print(twoSum([1,3,5,8,9,2,6,4], 18))