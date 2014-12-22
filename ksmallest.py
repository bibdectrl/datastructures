def ksmall(k, alist):
  alist.sort()
  return alist[k - 1]

print ksmall(3, [4, 3, 2, 1, 6, 7, 8])
