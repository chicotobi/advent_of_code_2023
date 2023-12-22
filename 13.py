d = open("13").read().split("\n\n")
d2 = [i.split("\n") for i in d]
d3 = [[[i for i in j] for j in p] for p in d2]

def pr(p):
  print()
  print('\n'.join(''.join(i) for i in p))

def find_mirror_idx(pattern, ori_line = ""):
  # Horizontal mirror
  n = len(pattern)
  for i in range(0,n-1):
    # mirror is then between idx i and i+1
    is_mirror = True
    #print("check mirror idx",i)
    for j in range(n-1):
      #print("check j",j)
      if i-j < 0 or i+1+j > n-1:
        break
      line1 = pattern[i-j]
      line2 = pattern[i+1+j]
      #print("check lines",line1,line2)
      if line1 != line2:
        is_mirror = False
        break
    if is_mirror:
      line = 'H' + str(i+1)
      if line != ori_line:
        #print("is horizontal mirror with idx",i+1)
        return line, (i+1)*100

  # Vertical mirror
  m = len(pattern[0])
  for i in range(0,m-1):
    # mirror is then between idx i and i+1
    is_mirror = True
    #print("check mirror idx",i)
    for j in range(m-1):
      #print("check j",j)
      if i-j < 0 or i+1+j > m-1:
        break
      line1 = [pattern[k][i-j] for k in range(n)]
      line2 = [pattern[k][i+1+j] for k in range(n)]
      #print("check lines",line1,line2)
      if line1 != line2:
        is_mirror = False
        break
    if is_mirror:
      line = 'V' + str(i+1)
      if line != ori_line:
        #print("is vertical mirror with idx",i+1)
        return line, (i+1)
  return "",0

s1 = 0
s2 = 0
for original in d3:
  pr(original)

  # find original pts
  ori_line, pt1 = find_mirror_idx(original)
  s1 += pt1
  print("Original reflection line:",ori_line)
  print("Part1 Points added",pt1)

  # add smudge anywhere??
  pt2 = 0
  smudge_found = False
  for i in range(len(original)):
    for j in range(len(original[0])):
      changed = [[i for i in j] for j in original]
      if original[i][j] == '.':
        changed[i][j] = '#'
      else:
        changed[i][j] = '.'
      cha_line, pt2 = find_mirror_idx(changed, ori_line)

      if ori_line != cha_line and pt2 > 0:
        print("Smudge at",i,j)
        print("Changed reflection line:",cha_line)
        print("Part2 Points added",pt2)
        s2 += pt2
        smudge_found = True
        break
    if smudge_found:
      break
  if not smudge_found:
    raise

print()
print("Points Part1",s1,"Part2",s2)
