
# def twoSum(nums, target) :
#    dic = {}
#    for i in range(len(nums)):
#       if target - nums[i] in dic:
#          return [dic[target-nums[i]],i]
#    return dic
# print(twoSum([1,2,3,4],7))


def reverse(x):
   if x < (-2**31) or x > (2**31)-1:
         return 0
   sx = str(x)
   if len(sx) == 1:
      sx = int(sx)
      return sx
   new = ""
   if sx[0] == "-":
      new = new + sx[0]
      for i in range(len(sx)-1,0,-1):
         new +=  sx[i]
      new = int(new)
      if new < (-2**31) or new > (2**31)-1:
         return 0
      return new
   else :
      for i in range(len(sx)-1,-1,-1):
         new +=  sx[i]
      new = int(new)
      if new < (-2**31) or new > (2**31)-1:
         return 0
      return new 
print(reverse(1534236469))


