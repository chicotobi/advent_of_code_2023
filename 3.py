def symbol_in_neighborhood(i,j):
  tmp = False
  if i > 0:
    if j > 0 and d[i-1][j-1] not in '0123456789.':
      tmp = True
    if j < jmax-1 and d[i-1][j+1] not in '0123456789.':
      tmp = True
    if d[i-1][j] not in '0123456789.':
      tmp = True
  if i < imax-1:
    if j > 0 and d[i+1][j-1] not in '0123456789.':
      tmp = True
    if j < jmax-1 and d[i+1][j+1] not in '0123456789.':
      tmp = True
    if d[i+1][j] not in '0123456789.':
      tmp = True
  if j > 0 and d[i][j-1] not in '0123456789.':
    tmp = True
  if j < jmax-1 and d[i][j+1] not in '0123456789.':
    tmp = True
  return tmp

d = []
for i in open('3'):
  d += [[j for j in i if j != "\n"]]
  
imax = len(d)
jmax = len(d[0])

ss = 0
x = 0
valid = False
f = open('3_sol','w')
for i in range(imax):
  print()
  print("row",i)
  for j in range(jmax):
    if d[i][j] in '0123456789':
      x *= 10
      x += int(d[i][j])
      if symbol_in_neighborhood(i,j):
        valid = True
    else:
      if x > 0:
        if valid:
          print(x,"valid")
          f.write(str(x)+"\n")
          ss += x
        else:
          print(x, "INVALID------")
      x = 0
      valid = False
  if x > 0:
    if valid:
      print(x,"valid")
      f.write(str(x)+"\n")
      ss += x
    else:
      print(x, "INVALID------")
  x = 0
  valid = False
print()
print("sum",ss)
