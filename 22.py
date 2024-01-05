d = open('22').read().splitlines()
bricks = []
for brick in d:
  tmp = brick.split("~")
  tmp0 = tmp[0].split(",")
  tmp1 = tmp[1].split(",")
  u, v, w = int(tmp0[0]), int(tmp0[1]), int(tmp0[2])
  x, y, z = int(tmp1[0]), int(tmp1[1]), int(tmp1[2])
  if u != x:
    ori = 1
  elif v != y:
    ori = 2
  elif w != z:
    ori = 3
  bricks.append([(u,v,w),(x,y,z),ori])

# My own test
#bricks = [[(1,1,3),(3,1,3),1]]

nx = max(max(u,x) for (u,v,w),(x,y,z),_ in bricks) + 1
ny = max(max(v,y) for (u,v,w),(x,y,z),_ in bricks) + 1
nz = max(max(w,z) for (u,v,w),(x,y,z),_ in bricks) + 1

def f(x):
  return x[0][2] + x[1][2]

bricks = sorted(bricks,key=f)

def symrange(a,b):
  if a<b:
    return range(a,b+1)
  else:
    return range(b,a+1)
  
def in_symrange(i,a,b):
  return i in symrange(a,b)

def get_state_from_bricks(brs):
  state = [[[-1 for k in range(nz)] for j in range(ny)] for i in range(nx)]
  for (idx, ((u,v,w), (x,y,z), ori)) in enumerate(brs):
    for i in symrange(u,x):
      for j in symrange(v,y):
        for k in symrange(w,z):
          state[i][j][k] = idx
  return state

def pr(bricks):
  st = get_state_from_bricks(bricks)
  print()
  for z in range(nz-1, -1, -1):
    v = '.ABCDEFG'
    s = ' '.join(''.join(v[st[x][y][z]+1] for x in range(nx)) for y in range(ny))
    print(s)

def fall_until_equi(br0):
  recheck = True
  while recheck:
    recheck = False
    for idx, br in enumerate(br0):
      st = get_state_from_bricks(br0)
      (u,v,w), (x,y,z), ori = br
      stp = False
      freefall = 0
      for zfall in range(1,min(w,z)+1):
        for i in symrange(u,x):
          for j in symrange(v,y):
            if st[i][j][min(w,z)-zfall] != -1:
              stp = True
              break
          if stp:
            break
        if stp:
          break
        freefall = zfall  
      if freefall > 0:
        print("Brick",idx,"fell",freefall,"spaces")
        br0[idx] = [(u,v,w-freefall), (x,y,z-freefall), ori]
        recheck = True
  return br0


#pr(bricks)
bricks = fall_until_equi(bricks)
#pr(bricks)



# removing brick 0
# Brick 8 fell 1 spaces

# removing brick 1
# Brick 8 fell 1 spaces

# removing brick 2

# removing brick 3
# Brick 9 fell 1 spaces

# removing brick 4
# Brick 22 fell 3 spaces

def falling_bricks_if_removed(bricks, removed_idxs):
  
  st = get_state_from_bricks(bricks)
    
  check = True
  while check:
    check = False
    
    
    # first, find all bricks that possibly rely on the removed brick(s)
    # that should be all bricks which have a part of them with
    # a z-value exactly one higher?
    tmp = []
    for removed_idx0 in removed_idxs:
      (u,v,w), (x,y,z), ori = bricks[removed_idx0]
      tmp += [st[i][j][max(w,z)+1] for i in symrange(u,x) for j in symrange(v,y)]
      
    possibly_falling_idxs = set(tmp) - set(removed_idxs)
    if -1 in possibly_falling_idxs:
      possibly_falling_idxs.remove(-1)
      
    # now check for each of these bricks if they have an element
    # a) outside of the bounds of the removed brick
    # b) supported by another brick
    new_removed_idxs = []
    for possible_falling_idx0 in possibly_falling_idxs:
      (a,b,c), (d,e,f), ori = bricks[possible_falling_idx0]
      elsewhere_supported = False
      for i in symrange(a,d):
        for j in symrange(b,e):
          if st[i][j][min(c,f)-1] not in removed_idxs + [-1]:
            elsewhere_supported = True
      if not elsewhere_supported:
        new_removed_idxs.append(possible_falling_idx0)
        check = True
        #print(possible_falling_idx0,"now falling")
    removed_idxs += new_removed_idxs
  return len(removed_idxs)

s = 0
for i in range(len(bricks)):
  print()
  print("removing brick",i)
  #pr(bricks2)
  val = falling_bricks_if_removed(bricks,[i])
  if val > 1:
    s += val - 1
    print(val-1,"falling")
  #pr(bricks2)
print(s)
