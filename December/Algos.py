def isValidSubsequence (sequence, array):
   # seqIdx = 0
   # for value in array:
   #    if seqIdx == len(sequence):
   #       break
   #    if sequence[seqIdx] == value:
   #       seqIdx += 1
   # return seqIdx == len(sequence)

   # OR

   # arrIdx = 0
   # seqIdx = 0
   # while arrIdx < len(array) and seqIdx < len(sequence):
   #    if sequence[seqIdx] == array[arrIdx]:
   #       seqIdx += 1
   #    arrIdx += 1
   # return seqIdx == len(sequence)

print(isValidSubsequence([-1,6,-1,10],[5,1,22,25,6,-1,8,10]))
