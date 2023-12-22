d = open("1").read()

floor = 0
i = 0
while floor >= 0:
  if d[i] == "(":
    floor += 1
  else:
    floor -= 1
  i += 1
