# from random import random
# import math
# import matplotlib.pyplot as plt
# import networkx as nx

d = open("25").read().splitlines()

nodes = list()
edges = {}
for r in d:
  n1, j = r.split(": ")
  nodes.append(n1)
  for n2 in j.split(" "):
    nodes.append(n2)
    if n1 not in edges.keys():
      edges[n1] = []
    edges[n1] += [n2]
    if n2 not in edges.keys():
      edges[n2] = []
    edges[n2] += [n1]
nodes = sorted(list(set(nodes)))
print(edges)

# Start comp and neighboorhood
comp = []
neighbors = {n:0 for n in nodes}

# Find a 3-clique to start?
cliq3 = []
for n1 in nodes:
  for n2 in edges[n1]:
    for n3 in edges[n1]:
      if n2 < n3 and n3 in edges[n2]:
        print("3 clique found",n1,n2,n3)
        cliq3 += [(n1,n2,n3)]

new_ns = ['cnh','jhz','qpg','lvj']

# Update comp and neighboorhood
comp += new_ns
for new_n in new_ns:
  neighbors.pop(new_n)
  for n in edges[new_n]:
    if n in neighbors.keys():
      neighbors[n] += 1
  
# Now "grow" this node 
limit = 6
while limit > 1:  
  new_ns = [k for (k,v) in neighbors.items() if v >= limit]
  
  # update comp and neighboorhood
  comp += new_ns
  for new_n in new_ns:
    neighbors.pop(new_n)
    for n in edges[new_n]:
      if n in neighbors.keys():
        neighbors[n] += 1
  
  #print(comp, neighbors)
  print()
  if len(new_ns) == 0:
    print("couldnt add neighbor with at least",limit,"connections to the comp")
    limit -= 1
    print("set limit to ",limit)
    continue
  limit = 6
  print("successful addition of ",len(new_ns),"new nodes to component")
  print("setting limit to",limit)
  
print(len(neighbors),len(comp))
# def plot(edges):
#   edges_w = {}
#   for i,j in edges:
#     if i < j:
#       if (i,j) not in edges_w.keys():
#         edges_w[(i,j)] = 0
#       edges_w[(i,j)] += 1
#     else:
#       if (j,i) not in edges_w.keys():
#         edges_w[(j,i)] = 0
#       edges_w[(j,i)] += 1
      
  
#   edges_w = [(i,j,k) for (i,j),k in edges_w.items()]
    
#   G = nx.Graph()
  
#   # Add edges with weights to the graph
#   G.add_weighted_edges_from(edges_w)
  
#   # Draw the graph
#   pos = nx.spring_layout(G)  # positions for all nodes
#   nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=20, font_color='black', font_weight='bold', width=2, edge_color='gray')
  
#   # Add edge weights to the plot
#   labels = nx.get_edge_attributes(G, 'weight')
#   nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
  
#   # Display the graph
#   plt.show()
  
#plot(edges)
#raise

# while True:
#   edges = [e for e in edges0]
#   n = len(edges)
#   node_map = {n:[n] for n in nodes}
  
#   # Karger algorithm
#   while len(set(edges)) > 1:
#     #while True:
#     r = math.floor(random() * n)
#     n1, n2 = edges[r]
#   #if (n1, n2) not in [('hfx','pzl'),('bvb','cmg'),('jqt','nvd')]:
#       #  break
#     node_map[n1] += node_map.pop(n2)
#     edges = [e for e in edges if e != (n1,n2)]
#     edges = [e for e in edges if e != (n2,n1)]
#     n = len(edges)
#     edges = [(n1,y) if x==n2 else (x,n1) if y==n2 else (x,y) for (x,y) in edges]
#     # re-sort?
#     edges = [(x,y) if x<y else (y,x) for (x,y) in edges]
#     edges = sorted(edges)
    
#     #print("removed edge",n1,n2,"leaving",n,"edges")
#     #print(node_map)
#   s = [len(i) for i in node_map.values()]
#   print(s,s[0]*s[1])
#   if len(edges) == 3:
#     break

  
  #plot(edges)

# print("find 3-cl") 
# # find 3-cliques
# cliq3 = set()
# for i, n1 in enumerate(nodes):
#   print(i/len(nodes))
#   for j, n2 in enumerate(nodes):
#     if i < j:
#       for k, n3 in enumerate(nodes):
#         if j < k:
#           if (n1,n2) in edges and (n1,n3) in edges and (n2,n3) in edges:
#             c1 = (n1,n2,n3)
#             cliq3.add((n1,n2,n3))

# print("find 4-cl")
# # find 4-cliques
# cliq4 = set()
# for i, c1 in enumerate(cliq3):
#   for j, c2 in enumerate(cliq3):
#     if i < j:
#       tmp = [i for i in c1 if i in c2]
#       if len(tmp) == 2:
#         n1 = [i for i in c1 if i not in c2][0]
#         n2, n3 = tmp
#         n4 = [i for i in c2 if i not in c1][0]
#         c3 = tuple(sorted([n1,n2,n4]))
#         c4 = tuple(sorted([n1,n3,n4]))
#         if c3 in cliq3 and c4 in cliq3:
#           cn = tuple(sorted([n1,n2,n3,n4]))
#           cliq4.add(cn)

# # now "grow" one of these 4-cliques
# # if a node is connected to at least four of the nodes
# # it has to be part of the same component!
# new_nodes = list(list(cliq4)[0])
# component = [] + new_nodes
# while len(new_nodes)>0:
#   new_nodes = []
#   for n in nodes:
#     if n not in component:
#       n_connecting_edges = sum(1 for i in component if (n,i) in edges)
#       if n_connecting_edges >= 3:
#         new_nodes += [n]
#   component += new_nodes
#   print("comp:",component)
  
# print(len(component)*(len(nodes)-len(component)))