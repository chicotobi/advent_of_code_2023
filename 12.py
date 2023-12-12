def split(x,n):
  if n == 1:
    return [[x]]
  ls = []
  for i in range(x+1):
    t = split(x-i,n-1)
    t2 = [[i] + j for j in t]
    ls += t2
  return ls

infos = open('12').read().splitlines()

ss = 0
for line in infos:
  info, blocks = line.split(" ")
  blocks = [int(i) for i in blocks.split(",")]
  
  l = len(info)
  nwhites = l - sum(blocks)
      
  S = []
  
  print("into split",nwhites, len(blocks)+1)
  combs = split(nwhites, len(blocks)+1)
  
  print("out of split")
  for i in combs:
    mid = i[1:-1]
    vals = [j==0 for j in mid]
    if any(vals):
      continue
    t = [[] for j in range(2*len(blocks)+1)]
    t[::2] = ['.'*j for j in i]
    t[1::2] = ['#'*j for j in blocks]
    t = ''.join(t)
    
     # check
    possible = [True if a==b or a=='?' else False for (a,b) in zip(info,t) ]
    
    if all(possible):
      S.append(t)
  
  print(info,blocks)
  print(S)
  print(len(S))
  ss += len(S)
  print()

print(ss)