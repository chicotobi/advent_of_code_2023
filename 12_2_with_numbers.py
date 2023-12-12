import time

def possible(info,test):
  tmp = [True if a==b or a=='?' else False for (a,b) in zip(info,test)]
  return all(tmp)

def split(x, n, info, blocks):

  if n == 1:
    if '#' in info:
      return 0
    else:
      return 1

  # Additional break condition
  if sum(1 for i in info if i == '#') > sum(blocks):
    #print('early return')
    return 0

  # Additional break condition
  if sum(1 for i in info if i == '.') + sum(blocks) > len(info):
    #print('early return')
    return 0

  count = 0
  #min_amount_zeros = max(1,max(info.find('?')-1,info.find('#')-1))
  #print("min_amount_zeros",min_amount_zeros)
  min_amount_zeros = 1
  for i in range(min_amount_zeros,x+1):
    # Check if zeros possible
    if not possible(info[:i],'.'*i):
      return count

    # Check if ones possible
    if not possible(info[i:(i+blocks[0])],'#'*blocks[0]):
      continue

    count += split(x-i,n-1, info[(i+blocks[0]):], blocks[1:])
  return count

def execute():
  ss = 0
  for line in infos:
    info, blocks = line.split(" ")
    blocks = [int(i) for i in blocks.split(",")]

    # unfold
    blocks = blocks * 5
    info = (info + '?')*4 + info

    info = '.' + info + '.'

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


infos = open('12_test').read().splitlines()
benchmark()
