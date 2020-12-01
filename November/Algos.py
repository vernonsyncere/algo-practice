
# def twoSum(nums, target) :
#    dic = {}
#    for i in range(len(nums)):
#       if target - nums[i] in dic:
#          return [dic[target-nums[i]],i]
#    return dic
# print(twoSum([1,2,3,4],7))


# def reverse(x):
#    sx = str(x)
#    if len(sx) == 1:
#       sx = int(sx)
#       return sx
#    new = ""
#    if sx[0] == "-":
#       new = new + sx[0]
#       for i in range(len(sx)-1,0,-1):
#          new +=  sx[i]
#    else :
#       new = "".join(reversed(sx))
#    new = int(new)
#    if new < (-2**31) or new > (2**31)-1:
#       return 0
#    return new 
# print(reverse(308))

def reverseStringII(s,k):
   count = len(s)
   odd = True
   res = []
   start = 0
   tracker = 1

   while start < count:
      end = min(start + k,count )
      if odd:
         res.append(s[start:end][::-1])
         print(tracker, end, tracker, res)
      else :
         res.append(s[start:end])
         print(tracker, end, tracker, res)
      start = end
      odd = not odd   
      tracker += 1
   return "".join(res)

print(reverseStringII("abcdefg", 4))

