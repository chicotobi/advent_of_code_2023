data = open('21').read().splitlines()
data = [[i for i in j] for j in data]

n = len(data)
m = len(data[0])
data = {(i,j):el for (i,r) in enumerate(data) for (j,el) in enumerate(r)}

new_plots = [k for (k,v) in data.items() if v == 'S']
data[new_plots[0]] = '.'

for i in range(32):
  tmp = []
  for x0, y0 in new_plots:
    u  = (x0-1,y0)
    d  = (x0+1,y0)
    r  = (x0,y0+1)
    l  = (x0,y0-1)
    uu = (x0-2,y0)
    dd = (x0+2,y0)
    rr = (x0,y0+2)
    ll = (x0,y0-2)
    ul = (x0-1,y0-1)
    ur = (x0-1,y0+1)
    dl = (x0+1,y0-1)
    dr = (x0+1,y0+1)

    if uu in data.keys() and data[u] == '.' and data[uu] == '.':
      data[uu] = 'O'
      tmp.append(uu)
    if dd in data.keys() and data[d] == '.' and data[dd] == '.':
      data[dd] = 'O'
      tmp.append(dd)
    if rr in data.keys() and data[r] == '.' and data[rr] == '.':
      data[rr] = 'O'
      tmp.append(rr)
    if ll in data.keys() and data[l] == '.' and data[ll] == '.':
      data[ll] = 'O'
      tmp.append(ll)

    if ur in data.keys() and data[ur] == '.' and (data[u] == '.' or data[r] == '.'):
      data[ur] = 'O'
      tmp.append(ur)

    if ul in data.keys() and data[ul] == '.' and (data[u] == '.' or data[l] == '.'):
      data[ul] = 'O'
      tmp.append(ul)

    if dr in data.keys() and data[dr] == '.' and (data[d] == '.' or data[r] == '.'):
      data[dr] = 'O'
      tmp.append(dr)

    if dl in data.keys() and data[dl] == '.' and (data[d] == '.' or data[l] == '.'):
      data[dl] = 'O'
      tmp.append(dl)

  new_plots = tmp
  d0 = [[data[i,j] for i in range(m)] for j in range(m)]
  print('\n'.join(''.join(i) for i in d0))
  print()

ss = sum(1 for (k,v) in data.items() if v == 'O')
print(ss)
