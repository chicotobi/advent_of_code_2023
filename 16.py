d = open('16').read().splitlines()

n = len(d)
m = len(d[0])

# x, y, dir (N E S W = 0 1 2 3)

def pr(f):
  f2 = set((i,j) for (i,j,k) in f)
  f3 = [['.' for j in range(m)] for i in range(n)]
  for i in range(n):
    for j in range(m):
      if (i,j) in f2:
        f3[i][j] = '#'
  print('\n'.join(''.join(i) for i in f3))


def fill(d,f,x,y,dire):
  # advance
  if dire == 0:
    x -= 1
  elif dire == 1:
    y += 1
  elif dire == 2:
    x += 1
  elif dire == 3:
    y -= 1
  else:
    raise
  #print()
  #print('check',x,y,dire)
  #pr(f)
  if x < 0 or x > n-1 or y < 0 or y > m-1:
    #print('out')
    return f
  if (x,y,dire) in f:
    return f
  f.add((x,y,dire))
  if d[x][y] == '.' or (d[x][y]=='|' and dire in [0,2]) or (d[x][y]=='-' and dire in [1,3]):
    if dire == 0:
      f = fill(d,f,x,y,dire)
    if dire == 1:
      f = fill(d,f,x,y,dire)
    if dire == 2:
      f = fill(d,f,x,y,dire)
    if dire == 3:
      f = fill(d,f,x,y,dire)
  elif d[x][y] == '|' and dire in [1,3]:
    f = fill(d,f,x,y,0)
    f = fill(d,f,x,y,2)
  elif d[x][y] == '-' and dire in [0,2]:
    f = fill(d,f,x,y,1)
    f = fill(d,f,x,y,3)
  elif d[x][y] == '\\':
    if dire == 0:
      f = fill(d,f,x,y,3)
    elif dire == 1:
      f = fill(d,f,x,y,2)
    elif dire == 2:
      f = fill(d,f,x,y,1)
    elif dire == 3:
      f = fill(d,f,x,y,0)
    else:
      raise
  elif d[x][y] == '/':
    if dire == 0:
      f = fill(d,f,x,y,1)
    elif dire == 1:
      f = fill(d,f,x,y,0)
    elif dire == 2:
      f = fill(d,f,x,y,3)
    elif dire == 3:
      f = fill(d,f,x,y,2)
    else:
      raise
  else:
    raise
  # (N E S W = 0 1 2 3)
  return f


def process(x,y,dire):  
  f = set()  
  f = fill(d,f,x,y,dire)  
  ss = 0
  for i in range(n):
    for j in range(m):
      if (i,j,0) in f or (i,j,1) in f or (i,j,2) in f or (i,j,3) in f:
        ss += 1
  return ss

best_score = 0
for i in range(n):
  ss = process(i,-1,1)
  print(ss)
  best_score = max(best_score,ss)
  ss = process(i,m,3)
  print(ss)
  best_score = max(best_score,ss)
for j in range(m):
  ss = process(-1,j,2)
  print(ss)
  best_score = max(best_score,ss)
  ss = process(n,j,0)
  print(ss)
  best_score = max(best_score,ss)
  
print("best_score",best_score)