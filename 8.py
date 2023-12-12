d = open('8').read().splitlines()
cmd = d[0]
d = d[2:]
dct = {}
for r in d:
  a = r[0:3]
  b = r[7:10]
  c = r[12:15]
  dct[a] = {}
  dct[a]['L'] = b
  dct[a]['R'] = c
  
# n = 0
# x = 'AAA'
# while x != 'ZZZ':
#   cmd0 = cmd[n%len(cmd)]
#   print(cmd0)
#   x = dct[x][cmd0]
#   n += 1
  
# print(n)

x = [i for i in dct.keys() if i[2] == 'A']
goals = [i for i in dct.keys() if i[2] == 'Z']

n = 0
while True:
  cmd0 = cmd[n%len(cmd)]
  x = [dct[i][cmd0] for i in x]
  tmp = [1 if i in goals else 0 for i in x]
  if sum(tmp) > 0:
    tmp2 = [i if i in goals else '...' for i in x]
    print(n,n%len(cmd),tmp2)
  n += 1
print(n)