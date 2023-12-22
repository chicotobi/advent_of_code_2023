data = open('21').read().splitlines()
data = [[i for i in j] for j in data]

n = len(data)
m = len(data[0])
data = {(i,j):el for (i,r) in enumerate(data) for (j,el) in enumerate(r)}

active = [k for (k,v) in data.items() if v == 'S']
data[active[0]] = '.'
x0, y0 = active[0]

steps = []

def dmod(inp):
  x, y = inp
  x = x%n
  y = y%m
  return data[(x,y)]

for i in range(1000):
  print(i,",",len(active),",")
  new_active = set()
  for x0, y0 in active:
    u  = (x0-1,y0)
    d  = (x0+1,y0)
    r  = (x0,y0+1)
    l  = (x0,y0-1)

    if dmod(u) == '.':
      new_active.add(u)
    if dmod(d) == '.':
      new_active.add(d)
    if dmod(r) == '.':
      new_active.add(r)
    if dmod(l) == '.':
      new_active.add(l)

  active = new_active
