ss = 0
for i in open('2'):
  i1 = i.replace(",","").replace(";","").replace(":","")
  i2 = i1.split()
  game_id = int(i2[1])
  i3 = i2[2:]
  n = len(i3)//2
  maxi = {"red":0,"blue":0,"green":0}
  for j in range(n):
    m = int(i3[2*j])
    col = i3[2*j+1]
    maxi[col] = max(maxi[col],m)
  print(maxi)
  power = maxi["red"] * maxi["green"] * maxi["blue"]
  ss += power