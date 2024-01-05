d0 = open('23').read().splitlines()
d0 = [[i for i in j] for j in d0]

nx = len(d0)
ny = len(d0[0])

def walk(d1,x,y):
  d = [[i for i in j] for j in d1]
  lengths = []
  d[x][y] = '#'
  if x == nx - 1 and y == ny - 2:
    return 1
  
  r = d[x][y+1]
  if r == '.':
    check = walk(d,x,y+1)
    if check > 0:
      lengths += [check+1]
  elif r == '>':
    check = walk(d,x,y+2)
    if check > 0:
      lengths += [check+2]
    
  l = d[x][y-1]
  if l == '.':
    check = walk(d,x,y-1)
    if check > 0:
      lengths += [check+1]
  elif l == '<':
    check = walk(d,x,y-2)
    if check > 0:
      lengths += [check+2]

  u = d[x-1][y]
  if u == '.':
    check = walk(d,x-1,y)
    if check > 0:
      lengths += [check+1]
  elif u == '^':
    check = walk(d,x-2,y)
    if check > 0:
      lengths += [check+2]
    
  do = d[x+1][y]
  if do == '.':
    check = walk(d,x+1,y)
    if check > 0:
      lengths += [check+1]
  elif do == 'v':
    check = walk(d,x+2,y)
    if check > 0:
      lengths += [check+2]
  
  if len(lengths) == 0:
    return -1
  return max(lengths)

res = walk(d0,1,1)
print("max path",res)

def pr(x):
  print('\n'.join(''.join(i) for i in x))