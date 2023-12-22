# Right-winding curve
d = open('18_test').read().splitlines()
# Right-winding curve
d = open('18').read().splitlines()

d2 = [i.split() for i in d]

x0 = 0
y0 = 0
s = [(x0,y0,0)]
inner = []
ct = 0
for (dire,n,_) in d2:
  if dire == 'U':
    inner += [(x0,y0+1)]
  elif dire == 'R':
    inner += [(x0+1,y0)]
  elif dire == 'D':
    inner += [(x0,y0-1)]
  elif dire == 'L':
    inner += [(x0-1,y0)]
  else:
    raise
  for i in range(int(n)):
    if dire == 'U':
      x0 -= 1
      inner += [(x0,y0+1)]
    elif dire == 'R':
      y0 += 1
      inner += [(x0+1,y0)]
    elif dire == 'D':
      x0 += 1
      inner += [(x0,y0-1)]
    elif dire == 'L':
      y0 -= 1
      inner += [(x0-1,y0)]
    else:
      raise
    ct += 1
    s += [(x0,y0,ct%5)]


minx = min(x for (x,y,_) in s)
miny = min(y for (x,y,_) in s)

s = [(x-minx,y-miny,c) for (x,y,c) in s]
inner = [(x-minx,y-miny) for (x,y) in inner]

n = max(x for (x,y,_) in s) + 1
m = max(y for (x,y,_) in s) + 1

s2 = [['.']*m for i in range(n)]
for (x,y) in inner:
  s2[x][y] = 'o'
for (x,y,c) in s:
  s2[x][y] = str(c)


def pr(x):
  print('\n'.join(''.join(i) for i in x))

pr(s2)

# Little view
ss = [[el for (i,el) in enumerate(r) if i < 60] for (j,r) in enumerate(s2)]
pr(ss)

s3 = set((x,y) for (x,y,c) in s)
inner = set(inner)
true_inner = set(i for i in inner if i not in s3)

# iterate over inner points:
candidates = true_inner
next_candidates = set()
while len(candidates) > 0:
  for (x,y) in candidates:
    c = (x+1,y)
    if c not in s3 and c not in true_inner:
      next_candidates.add(c)
    c = (x-1,y)
    if c not in s3 and c not in true_inner:
      next_candidates.add(c)
    c = (x,y+1)
    if c not in s3 and c not in true_inner:
      next_candidates.add(c)
    c = (x,y-1)
    if c not in s3 and c not in true_inner:
      next_candidates.add(c)
  print(next_candidates)
  true_inner = true_inner.union(next_candidates)
  candidates = next_candidates
  next_candidates = set()

print(len(s3) + len(true_inner))


# debug other solution
sol1_row_sums = {i:0 for i in range(-352,12)}
for (x,y) in true_inner:
  sol1_row_sums[x-352] += 1
