d = open('22_test').read().splitlines()
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
  else:
    raise
  bricks.append([(u,v,w),(x,y,z),ori])

# My own test
bricks = [[(1,1,3),(3,1,3),1]]

nx = max(max(u,x) for (u,v,w),(x,y,z),_ in bricks) + 1
ny = max(max(v,y) for (u,v,w),(x,y,z),_ in bricks) + 1
nz = max(max(w,z) for (u,v,w),(x,y,z),_ in bricks) + 1

def get_state_from_bricks(brs):
  state = [[[-1 for k in range(nz)] for j in range(ny)] for i in range(nx)]
  for (idx, ((u,v,w), (x,y,z), ori)) in enumerate(brs):
    for i in range(u,x+1):
      for j in range(v,y+1):
        for k in range(w,z+1):
          state[i][j][k] = idx
  return state

st = get_state_from_bricks(bricks)

def print_state():
  for

def fall_until_equi(brs):
  something_moved = True
  while something_moved:
    something_moved = False
    st = get_state_from_bricks(brs)
    for (idx, ((u,v,w), (x,y,z), ori)) in enumerate(brs):
      for free_space_under_brick in range(z):
        for i in range(u,x+1):
          for j in range(v,y+1):
              if st[i][j][z-free_space_under_brick-1] != -1:
                break
          else:
            continue
          break
      else:
        continue
      break
      if free_space_under_brick > 0:
        brs[idx] = [(u,v,w-free_space_under_brick), (x,y,z-free_space_under_brick), ori]
        something_moved = True
        print("Brick",idx,"fell",free_space_under_brick,"spaces")


fall_until_equi(bricks)
