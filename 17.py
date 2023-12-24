import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import shortest_path

d = open('17').read().splitlines()

n = len(d)
m = len(d[0])
d = [[int(j) for j in i] for i in d]

NN = n * m * 3 * 4

transitions = []

def hsh(st):
  i,j,ct,dire = st
  return i*m*3*4 + j*3*4 + (ct-1)*4 + dire

# N E S W 
# 0 1 2 3
hsh_map = {}
for i in range(n):
  for j in range(m):
    for ct in range(1,4):
      for dire in range(4):
        st0 = (i,j,ct,dire)
        hsh_map[hsh(st0)] = st0
        # Go up
        if i > 0:
          w = d[i-1][j]
          if dire == 0 and ct<3:
            st1 = (i-1,j,ct+1,0)
            transitions += [(st0,st1,w)]
          if dire in [1,3]:
            st1 = (i-1,j,1,0)
            transitions += [(st0,st1,w)]
        # Go right
        if j < m - 1:
          w = d[i][j+1]
          if dire==1 and ct<3:
            st1 = (i,j+1,ct+1,1)
            transitions += [(st0,st1,w)]
          if dire in [0,2]:
            st1 = (i,j+1,1,1)
            transitions += [(st0,st1,w)]
        # Go down
        if i < n - 1:
          w = d[i+1][j]
          if dire == 2 and ct<3:
            st1 = (i+1,j,ct+1,2)
            transitions += [(st0,st1,w)]
          if dire in [1,3]:
            st1 = (i+1,j,1,2)
            transitions += [(st0,st1,w)]
        # Go left
        if j > 0:
          w = d[i][j-1]
          if dire==3 and ct<3:
            st1 = (i,j-1,ct+1,3)
            transitions += [(st0,st1,w)]
          if dire in [0,2]:
            st1 = (i,j-1,1,3)
            transitions += [(st0,st1,w)]
        


# a = np.zeros((n*m*3*4,n*m*3*4))
# for (s0,s1,w) in transitions:
#   a[hsh(s0),hsh(s1)] = w

data = [w for (i,j,w) in transitions]
i0    = [hsh(i) for (i,j,w) in transitions]
j0    = [hsh(j) for (i,j,w) in transitions]

a = coo_matrix((data,(i0,j0)), shape = (NN,NN))

idx_s = [hsh((0  ,0  ,ct,dire)) for ct in range(1,4) for dire in range(4)]
idx_e = [hsh((n-1,m-1,ct,dire)) for ct in range(1,4) for dire in range(4)]

dist_matrix = shortest_path(a, indices = idx_s)
#dist_matrix, predecessors = shortest_path(a, return_predecessors = True)

#x0 something with (0,0,.,.)
#x1 something with (n-1,m-1,.,.)

m = dist_matrix[np.ix_(idx_s,idx_e)]

# path = []
# nxt = 2017
# while predecessors[1,nxt] != -9999:
#   path = [hsh_map[nxt]] + path
#   nxt = predecessors[1,nxt]

# # idx_a = [[idx(i,j) for (j,el) in enumerate(line) if el=='a'] for (i,line) in enumerate(d)]
# # idx_a = [i[0] for i in idx_a if len(i)>0]

# # for a in idx_a:
# #   m = min(m,r[a,idx_e])
# #   print(r[a,idx_e])
# # print(m)

print(np.min(m))