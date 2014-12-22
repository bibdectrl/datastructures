def reverse_list(aList):
  if len(aList) == 1:
      return aList
  else:
      return [aList[-1]] + reverse_list(aList[0:-1])



print reverse_list(range(10))

