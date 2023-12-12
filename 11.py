d = open('11').read().splitlines()

m = len(d[0])
n = len(d)

empty_row = ''.join(['.']*m)
empty_rows = []
for (idx,r) in enumerate(d):
  if r == empty_row:
    empty_rows.append(idx)

empty_col = ''.join(['.']*n)
empty_cols = []
for j in range(m):
  col = ''.join(r[j] for r in d)
  if col == empty_col:
    empty_cols.append(j)

galaxies = [(i,j) for (i,r) in enumerate(d) for (j,el) in enumerate(r) if d[i][j]=='#' ]

n_galaxies = len(galaxies)
dist = 0
for g1 in galaxies:
  for g2 in galaxies:
    i1, j1 = g1
    i2, j2 = g2
    tmp = abs(i1-i2) + abs(j1-j2)
    tmp += 999999 * sum(1 for i in empty_rows if min(i1,i2) < i and i < max(i1,i2))
    tmp += 999999 * sum(1 for i in empty_cols if min(j1,j2) < i and i < max(j1,j2))
    dist += tmp
print(dist//2)