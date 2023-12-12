f = '10'
d = open(f).read().splitlines()

dct = {}
typ = {}
cts = {
  "S": 0,
  "F": 0,
  "7": 0,
  "L": 0,
  "J": 0,
  "-": 0,
  "|": 0
  }
for (i,row) in enumerate(d):
  for (j,el) in enumerate(row):
    if el == 'S':
      idx_s = (i,j)
      # get start direction to make it a clockwise curve
      if f == '10_test2':
        dct[(i,j)] = [(i,j+1)]
      elif f == '10_test3':
        dct[(i,j)] = [(i,j+1)]
      elif f == '10_test4':
        dct[(i,j)] = [(i+1,j)]
      elif f == '10_test5':
        dct[(i,j)] = [(i+1,j)]
      else:
        dct[(i,j)] = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    if el == 'F':
      dct[(i,j)] = [(i+1,j),(i,j+1)]
    if el == '7':
      dct[(i,j)] = [(i+1,j),(i,j-1)]
    if el == 'L':
      dct[(i,j)] = [(i-1,j),(i,j+1)]
    if el == 'J':
      dct[(i,j)] = [(i-1,j),(i,j-1)]
    if el == '-':
      dct[(i,j)] = [(i,j+1),(i,j-1)]
    if el == '|':
      dct[(i,j)] = [(i+1,j),(i-1,j)]
    typ[(i,j)] = el

i_max = len(d)
j_max = len(d[0])

def pipe_step(last,curr):
  if curr not in dct.keys():
    return []
  if 0 <= i and i < i_max and 0 <= j and j < j_max:
    nx = [i for i in dct[curr] if i != last]
    return nx
  else:
    return []

# derived direction of curve by looking at mod count in the image
# my curve is clockwise
# now i know which fields to mark as inner

for curr in dct[idx_s]:
  print("Start",idx_s)
  print("Goto",curr)
  counts = {}
  mark_inner = set()
  last = idx_s
  ll = 1
  path = [curr]
  counts[curr] = ll
  while curr != idx_s:
    cts[typ[curr]] +=1
    counts[curr] = ll
    ll += 1
    i, j = curr
    if typ[curr] == 'F':
      if last == (i, j+1):
        mark_inner.add((i-1,j))
        mark_inner.add((i-1,j-1))
        mark_inner.add((i,j-1))
      elif last == (i+1, j):
        mark_inner.add((i+1,j+1))
      else:
        raise
    if typ[curr] == '7':
      if last == (i+1, j):
        mark_inner.add((i,j+1))
        mark_inner.add((i-1,j+1))
        mark_inner.add((i-1,j))
      elif last == (i, j-1):
        mark_inner.add((i+1,j-1))
      else:
        raise
    if typ[curr] == 'L':
      if last == (i-1, j):
        mark_inner.add((i,j-1))
        mark_inner.add((i+1,j-1))
        mark_inner.add((i+1,j))
      elif last == (i, j+1):
        mark_inner.add((i-1,j+1))
      else:
        raise
    if typ[curr] == 'J':
      if last == (i, j-1):
        mark_inner.add((i,j+1))
        mark_inner.add((i+1,j))
        mark_inner.add((i+1,j+1))
      elif last == (i-1, j):
        mark_inner.add((i-1,j-1))
      else:
        raise
    if typ[curr] == '-':
      if last == (i, j-1):
        mark_inner.add((i+1,j))
      elif last == (i, j+1):
        mark_inner.add((i-1,j))
      else:
        raise
    if typ[curr] == '|':
      if last == (i+1, j):
        mark_inner.add((i,j+1))
      elif last == (i-1, j):
        mark_inner.add((i,j-1))
      else:
        raise
    #if (0,37) in mark_inner:
    #  raise
    nx = pipe_step(last,curr)
    if len(nx) == 0:
      break
    if len(nx) > 1:
      raise
    last = curr
    curr = nx[0]
    path += [curr]
    print("Goto",curr,"ll",ll)
  if curr == idx_s:
    print("Great success",ll)
    print("Furthest away",ll//2)
    break

# remove path members from mark_inner:
for i in path:
  if i in mark_inner:
    mark_inner.discard(i)

  
# print result?
# and transform to new representation
def pprint():
  new_way = [[0]*j_max for i in range(i_max)]
  for i in range(i_max):
    line = []
    for j in range(j_max):
      if (i,j) in mark_inner and (i,j) in path:
        new_way[i][j] = 9
        c = '#'
      elif (i,j) in path:
        new_way[i][j] = 9
        c = 'P'
      elif (i,j) in mark_inner:
        new_way[i][j] = 1
        c = 'I'
      else:
        c = '.'
      line.append(c)
    print(''.join(line))

check = mark_inner.copy()
while len(check) > 0:
  #pprint()
  print(len(check))
  new_check = set()
  for (idx,(i,j)) in enumerate(check):
    if idx%500 == 0:
      print(idx)
    neighbours = [(i+1,j-1),(i+1,j),(i+1,j+1),(i-1,j-1),(i-1,j),(i-1,j+1),(i,j+1),(i,j-1)]
    for neigh in neighbours:
      if neigh not in path:
        if neigh not in mark_inner:
          new_check.add(neigh)
          mark_inner.add(neigh)
  check = new_check.copy()
  
    