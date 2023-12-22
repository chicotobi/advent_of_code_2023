d = open("14").read().splitlines()
d = [[i for i in j] for j in d]

n = len(d)
m = len(d[0])

def pr(p):
  print('\n'.join(''.join(i) for i in p))
  print()

def calc_load(d):
  load = 0
  for i in range(n):
    for j in range(m):
      if d[i][j] == 'O':
        load += n-i
  return load

def shift(d):
  for i in range(n):
    for j in range(m):
      if d[i][j] == 'O':
        k = i
        for k in range(i-1,-1,-1):
          if d[k][j] in ['O','#']:
            k += 1
            break
        d[i][j] = '.'
        d[k][j] = 'O'
  return d

# map [0][0] to [0][n-1]
# map [n-1][0] to [0][0]
# map [0][m-1] to [m-1][n-1]
# map [n-1][m-1] to [m-1][0]
def rotate(d):
  d2 = [[d[n-1-i][j] for i in range(n)] for j in range(m)]
  return d2

def cycle(d):
  for i in range(4):
    d = shift(d)
    d = rotate(d)
  return d

s = []
for i in range(1000):
  d = cycle(d)
  load = calc_load(d)
  #print(load)
  s += [load]

# find the period with the maximum value
v = s[-1]
vidx = [i for (i,j) in enumerate(s) if j == v]
periods = [i-j for (i,j) in zip(vidx[1:],vidx[:-1])]
