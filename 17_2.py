import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import shortest_path

d = open('17').read().splitlines()

n = len(d)
m = len(d[0])
d = [[int(j) for j in i] for i in d]

transitions = []

min_ct = 4
max_ct = 10

NN = n * m * (max_ct + 1) * 4

def hsh(st):
  i,j,ct,dire = st
  return i*m*(max_ct+1)*4 + j*(max_ct+1)*4 + ct*4 + dire

# N E S W 
# 0 1 2 3
hsh_map = {}
for i in range(n):
  for j in range(m):
    for ct in range(max_ct+1):
      for dire in range(4):
        st0 = (i,j,ct,dire)
        hsh_map[hsh(st0)] = st0
        # Go up
        if i > 0:
          w = d[i-1][j]
          if dire == 0 and ct < max_ct:
            st1 = (i-1,j,ct+1,0)
            transitions += [(st0,st1,w)]
          if dire in [1,3] and ct >= min_ct:
            st1 = (i-1,j,1,0)
            transitions += [(st0,st1,w)]
        # Go right
        if j < m - 1:
          w = d[i][j+1]
          if dire==1 and ct < max_ct:
            st1 = (i,j+1,ct+1,1)
            transitions += [(st0,st1,w)]
          if dire in [0,2] and ct >= min_ct:
            st1 = (i,j+1,1,1)
            transitions += [(st0,st1,w)]
        # Go down
        if i < n - 1:
          w = d[i+1][j]
          if dire == 2 and ct < max_ct:
            st1 = (i+1,j,ct+1,2)
            transitions += [(st0,st1,w)]
          if dire in [1,3] and ct >= min_ct:
            st1 = (i+1,j,1,2)
            transitions += [(st0,st1,w)]
        # Go left
        if j > 0:
          w = d[i][j-1]
          if dire==3 and ct < max_ct:
            st1 = (i,j-1,ct+1,3)
            transitions += [(st0,st1,w)]
          if dire in [0,2] and ct >= min_ct:
            st1 = (i,j-1,1,3)
            transitions += [(st0,st1,w)]


data = [w for (i,j,w) in transitions]
i0    = [hsh(i) for (i,j,w) in transitions]
j0    = [hsh(j) for (i,j,w) in transitions]

a = coo_matrix((data,(i0,j0)), shape = (NN,NN))

idx_s = [hsh((0  ,0  ,0, dire)) for dire in range(4)]
idx_e = [hsh((n-1,m-1,ct,dire)) for ct in range(min_ct, max_ct + 1) for dire in range(4)]

#dist_matrix = shortest_path(a, indices = idx_s)
dist_matrix, predecessors = shortest_path(a, return_predecessors = True, indices = idx_s)

m = dist_matrix[np.ix_(idx_s,idx_e)]

tmp = np.where(m == np.min(m))

start = idx_s[tmp[0][0]]
end = idx_e[tmp[1][0]]

path = []
nxt = end
while predecessors[start,nxt] != -9999:
  path = [hsh_map[nxt]] + path
  nxt = predecessors[start,nxt]

print(np.min(m))
print(path)