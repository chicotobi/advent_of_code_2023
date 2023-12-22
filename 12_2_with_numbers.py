import time
from functools import cache

def possible(info,test):
  tmp = [True if a==b or a==9 else False for (a,b) in zip(info,test)]
  return all(tmp)

@cache
def split(x, n, info, blocks):
  if n == 1:
    if 1 in info:
      return 0
    else:
      return 1

  # Additional break condition
  if sum(1 for i in info if i == 1) > sum(blocks):
    return 0

  # Additional break condition
  if sum(1 for i in info if i == 0) + sum(blocks) > len(info):
    return 0

  count = 0
  min_amount_zeros = 1
  for i in range(min_amount_zeros,x+1):
    # Check if zeros possible
    if not possible(info[:i],[0]*i):
      return count

    # Check if ones possible
    if not possible(info[i:(i+blocks[0])],[1]*blocks[0]):
      continue

    count += split(x-i,n-1, info[(i+blocks[0]):], blocks[1:])
  return count

def execute():
  ss = 0
  for line in infos:
    info, blocks = line.split(" ")
    blocks = tuple(int(i) for i in blocks.split(","))

    # unfold
    blocks = blocks * 5
    info = (info + '?') * 4 + info

    info = '.' + info + '.'
    info = [i for i in info]
    info = tuple(1 if i == '#' else 0 if i == '.' else 9 for i in info)

    l = len(info)
    nwhites = l - sum(blocks)

    s = split(nwhites, len(blocks)+1, info, blocks)
    ss += s
  return ss

def benchmark():
  for i in range(5):
    t = time.time()
    ss = execute()
    t2 = time.time()
    print('ss:',ss)
    print('t2-t:',t2-t)

infos = open('12').read().splitlines()
benchmark()
