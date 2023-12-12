def possible(info,test):
  tmp = [True if a==b or a=='?' else False for (a,b) in zip(info,test)]
  return all(tmp)

def split(x, n, info, blocks):
  if n == 1:
    if '#' in info:
      return []
    else:
      return [[x]]
  ls = []
  for i in range(1,x+1):
    # Check if zeros possible
    if not possible(info[:i],'.'*i):
      break

    # Check if ones possible
    if not possible(info[i:(i+blocks[0])],'#'*blocks[0]):
      continue

    t = split(x-i,n-1, info[(i+blocks[0]):], blocks[1:])
    t2 = [[i] + j for j in t]
    ls += t2
  return ls

def transform(x, blocks):
  t = [[] for j in range(2*len(blocks)+1)]
  t[::2] = ['.'*j for j in x]
  t[1::2] = ['#'*j for j in blocks]
  return ''.join(t)


infos = open('12_test').read().splitlines()

ss = 0
for line in infos:
  info, blocks = line.split(" ")
  blocks = [int(i) for i in blocks.split(",")]

  # unfold
  blocks = blocks + blocks + blocks + blocks + blocks
  info = info + '?' + info + '?' + info + '?' + info + '?' + info

  info = '.' + info + '.'

  l = len(info)
  nwhites = l - sum(blocks)

  combs = split(nwhites, len(blocks)+1, info, blocks)

  #S = [transform(i,blocks) for i in combs]

  print(len(combs))
  ss += len(combs)

print('ss:',ss)
