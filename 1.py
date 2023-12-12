x = [i for i in '0123456789']

ss = 0
for i in open('1'):
  first = -1
  last = -1
  for j in i:
    if j in x:
      last = int(j)
      if first == -1:
        first = int(j)
  ss += first * 10 + last