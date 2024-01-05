from functools import cache

d0 = open('23').read().splitlines()
d0 = [['#' if i=='#' else '.' for i in j] for j in d0]

nx = len(d0)
ny = len(d0[0])

def pr(x):
  for i in range(nx):
    r = ''
    for j in range(ny):
      if x[i][j] == 'N':
        r += str(node2idx[(i,j)])
      else:
        r += x[i][j]
    print(r)
    
# First mark all nodes:
d0[0][1] = 'N'
d0[nx-1][ny-2] = 'N'
nodes = [(0,1),(nx-1,ny-2)]
for x in range(1,nx-1):
  for y in range(1,ny-1):
    if d0[x][y] == '#':
      continue
    r = d0[x][y+1] == '.'
    l = d0[x][y-1] == '.'
    u = d0[x-1][y] == '.'
    d = d0[x+1][y] == '.'
    if r+l+d+u > 2:
      d0[x][y] = 'N'
      nodes += [(x,y)]
node2idx = {n:i for (i,n) in enumerate(nodes)}

pr(d0)

def follow_path(d0,x,y, last_dire):
  if d0[x][y] == 'N':
    return node2idx[(x,y)], 1
  d0[x][y] = '#'
  r = d0[x][y+1]
  l = d0[x][y-1]
  u = d0[x-1][y]
  d = d0[x+1][y]
  if r != '#' and last_dire != 'l':
    idx, ln = follow_path(d0,x,y+1,'r')
  if l != '#' and last_dire != 'r':
    idx, ln = follow_path(d0,x,y-1,'l')
  if u != '#' and last_dire != 'd':
    idx, ln = follow_path(d0,x-1,y,'u')
  if d != '#' and last_dire != 'u':
    idx, ln = follow_path(d0,x+1,y,'d')
  return idx, ln+1

# Now find the edges between the nodes... how?
def explore(d0,node_idx):
  x, y = nodes[node_idx]
  
  # Explore all unexplored directions from here
  r = d0[x][y+1] == '.'
  l = d0[x][y-1] == '.'
  u = d0[x-1][y] == '.'
  d = d0[x+1][y] == '.'
  
  edges = {}
  if r:
    node_idx2, ln = follow_path(d0,x,y+1,'r')
    edges[(node_idx, node_idx2)] = ln
  if l:
    node_idx2, ln = follow_path(d0,x,y-1,'l')
    edges[(node_idx, node_idx2)] = ln
  if u:
    node_idx2, ln = follow_path(d0,x-1,y,'u')
    edges[(node_idx, node_idx2)] = ln
  if d:
    node_idx2, ln = follow_path(d0,x+1,y,'d')
    edges[(node_idx, node_idx2)] = ln
    
  return edges

edges0 = {}
for i in range(2,len(nodes)):
  edges0.update(explore(d0,i))

edges = {}
for (i,j),k in edges0.items():
  if i not in edges.keys():
    edges[i] = {}
  edges[i].update({j:k})
  if j not in edges.keys():
    edges[j] = {}
  edges[j].update({i:k}) 

    
# Finally, we have a graph
# Find the longest path from 0 to 1
@cache
def longest_path(from_nd,to_nd, visited):
  if len(visited) < 5:
    print("."*len(visited)+str(from_nd))
  if from_nd == to_nd:
    return 0, [to_nd]
  
  best_length = -1
  best_path = []
  for next_nd, next_l in edges[from_nd].items():
    if next_nd in visited:
      continue
    new_visited = tuple(sorted(visited+(from_nd,)))
    length, path = longest_path(next_nd, to_nd, new_visited)

    if length > -1:
      if next_l + length > best_length:
        best_length = next_l + length
        best_path = [from_nd] + path  
  
  return best_length, best_path
  
# 6608 [0, 4, 10, 15, 18, 16, 24, 26, 25, 20, 22, 30, 35, 32, 34, 33, 31, 28, 21, 17, 14, 23, 27, 29, 19, 13, 7, 9, 12, 5, 6, 3, 2, 8]

#edges = {0:{2:10,3:5},2:{0:10,1:10,},3:{0:5,1:10},1:{2:10,3:10}}
best_length, best_path = longest_path(0,1,())
print(best_length, best_path)