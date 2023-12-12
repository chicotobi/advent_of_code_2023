def possible(info,test):
  tmp = [True if a==b or a=='?' else False for (a,b) in zip(info,test)]
  return all(tmp)

def split(x, n, info, blocks):
  if n == 1:
    if '#' in info:
      return 0
    else:
      return 1
  count = 0
  for i in range(1,x+1):
    # Check if zeros possible
    if not possible(info[:i],'.'*i):
      break

    # Check if ones possible
    if not possible(info[i:(i+blocks[0])],'#'*blocks[0]):
      continue

    count += split(x-i,n-1, info[(i+blocks[0]):], blocks[1:])
  return count

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

  ss += split(nwhites, len(blocks)+1, info, blocks)

print('ss:',ss)
