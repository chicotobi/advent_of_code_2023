def star_in_neighborhood(i,j):
  if i > 0:
    if j > 0 and d[i-1][j-1] == '*':
      return (i-1,j-1)
    if j < jmax-1 and d[i-1][j+1] == '*':
      return (i-1,j+1)
    if d[i-1][j] == '*':
      return (i-1,j)
  if i < imax-1:
    if j > 0 and d[i+1][j-1] == '*':
      return (i+1,j-1)
    if j < jmax-1 and d[i+1][j+1] == '*':
      return (i+1,j+1)
    if d[i+1][j] == '*':
      return (i+1,j)
  if j > 0 and d[i][j-1] == '*':
    return (i,j-1)
  if j < jmax-1 and d[i][j+1] == '*':
    return (i,j+1)
  return (-1,-1)

d = []
for i in open('3'):
  d += [[j for j in i if j != "\n"]]
  
imax = len(d)
jmax = len(d[0])

ss = {}
x = 0
valid = False
for i in range(imax):
  for j in range(jmax):
    if d[i][j] in '0123456789':
      x *= 10
      x += int(d[i][j])
      if star_in_neighborhood(i,j) != (-1,-1):
        valid = True
        star_loc = star_in_neighborhood(i,j)
        if star_loc not in ss.keys():
          ss[star_loc] = []
    else:
      if x > 0:
        if valid:
          print(x,"valid")
          ss[star_loc] += [x]
        else:
          print(x, "INVALID------")
      x = 0
      valid = False
  if x > 0:
    if valid:
      print(x,"valid")
      ss[star_loc] += [x]
    else:
      print(x, "INVALID------")
  x = 0
  valid = False
print()
print("sum",ss)
