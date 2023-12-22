d = open('18').read().splitlines()

d2 = [i.split() for i in d]

x0, y0 = 0, 0
s = {}
part = 2
if part == 1:
  d2 = [(i,int(j)) for (i,j,_) in d2]
else:
  dct = {0:'R',1:'D',2:'L',3:'U'}
  d2 = [(dct[int(k[7])], int(k[2:7],16)) for (_,_,k) in d2]

last_dire = d2[-1][0]
for (dire,n) in d2:
  if x0 not in s.keys():
    s[x0] = {}
  if last_dire == 'U' and dire == 'R':
    typ = 'r'
  if last_dire == 'U' and dire == 'L':
    typ = '7'
  if last_dire == 'D' and dire == 'R':
    typ = 'L'
  if last_dire == 'D' and dire == 'L':
    typ = 'J'
  if last_dire == 'R' and dire == 'U':
    typ = 'J'
  if last_dire == 'R' and dire == 'D':
    typ = '7'
  if last_dire == 'L' and dire == 'U':
    typ = 'L'
  if last_dire == 'L' and dire == 'D':
    typ = 'r'
  s[x0][y0] = typ
  if dire == 'U':
    x0 -= n
  if dire == 'R':
    y0 += n
  if dire == 'D':
    x0 += n
  if dire == 'L':
    y0 -= n
  last_dire = dire


s = {k:dict(sorted(v.items())) for (k,v) in s.items()}
s = dict(sorted(s.items()))

line_idxs = s.keys()

def simplify_intervals(intervals):
  t_in  = [(i,1) for i in intervals[::2]]
  t_out = [(i,-1) for i in intervals[1::2]]
  data = sorted(t_in+t_out)
  out = []
  s = 0
  for (i,v) in data:
    if s == 0 and v == 1:
      out += [i]
    if s == 1 and v == -1:
      out += [i]
    s += v
  return out
assert( simplify_intervals([1,4,7,10,3,5,11,14]) == [1,5,7,10,11,14])


def idx_inside(row,idx):
  left = row[::2]
  right = row[1::2]
  left_sum = sum(1 for i in left if i <= idx)
  right_sum = sum(1 for i in right if i < idx)
  return (left_sum+right_sum)%2 == 1

assert(not idx_inside([3,25,37,48,57,68],2))
assert(idx_inside([3,25,37,48,57,68],57))
assert(idx_inside([3,25,37,48,57,68],40))
assert(idx_inside([3,25,37,48,57,68],12))
assert(not idx_inside([3,25,37,48,57,68],36))
assert(not idx_inside([3,25,37,48,57,68],26))
assert(not idx_inside([3,25,37,48,57,68],49))
assert(not idx_inside([3,25,37,48,57,68],69))


all_sum = 0
vals = 0
top_vertices_row = []
last_row_was_empty = False
for x in range(min(line_idxs),max(line_idxs)+1):
  if x%10000 == 0:
    nn = x - min(line_idxs)
    dd = max(line_idxs) + 1 - min(line_idxs)
    print(nn/dd)
  #print("row idx ",x)
  if x in s.keys():
    row_info = s[x]
    last_row_was_empty = False
  else:
    if last_row_was_empty:
      all_sum += vals
      #print("it was simple")
      continue
    row_info = {}
    last_row_was_empty = True

  bottom_left_inside = False

  # Transfer info from top vertices row to cell row
  for y in top_vertices_row[::2]:
    if y-1 not in row_info.keys():
      row_info[y-1] = '|'
  for y in top_vertices_row[1::2]:
    if y not in row_info.keys():
      row_info[y] = '|'
  row_info = dict(sorted(row_info.items()))
  #print(row_info)

  # Transfer info from cell row to bottom vertices row
  bottom_vertices_row = []
  for (y, typ) in row_info.items():
    #print("col idx",y)
    bottom_left_inside = len(bottom_vertices_row)%2 == 0
    top_left_inside = idx_inside(top_vertices_row,y)
    top_right_inside = idx_inside(top_vertices_row,y+1)
    if typ in ['r','|']:
      if bottom_left_inside:
        bottom_vertices_row += [y+1]
      else:
        bottom_vertices_row += [y]
    if typ in ['7']:
      if bottom_left_inside:
        bottom_vertices_row += [y+1]
      else:
        bottom_vertices_row += [y]
    bottom_right_inside = len(bottom_vertices_row)%2 == 0
  #print(bottom_vertices_row)


  # Count cells by using bottom vertices row and top vertices row
  cells = simplify_intervals(top_vertices_row+bottom_vertices_row)
  vals = sum([i-j+2 for (i,j) in zip(cells[1::2],cells[::2])])
  #print(vals)
  all_sum += vals

  # Shift
  top_vertices_row = bottom_vertices_row

print("all_sum",all_sum)
