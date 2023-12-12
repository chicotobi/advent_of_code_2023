ss = 0
n_cards = 0
multiplier = [1] * 221
for (idx,j) in enumerate(open('4')):
  print()
  j2 = j[:-1]
  tmp = j2.split(":")[1].split("|")
  winning = [i for i in tmp[0].split(" ") if len(i)>0]
  my_numbers = [i for i in tmp[1].split(" ") if len(i)>0]
  intersect = [i for i in winning if i in my_numbers]
    
  # get the current multiplier
  mm = multiplier[0]
  multiplier = multiplier[1:]
  multiplier = [el+mm if i < len(intersect) else el for (i,el) in enumerate(multiplier) ]
  
  points = 0
  if len(intersect) > 0:
    points = 2 ** (len(intersect)-1)
  print("card index",idx+1)
  print("multiplier",mm)
  print("card worth",points)
  print("points*mm",points*mm)
  ss += points * mm
  n_cards += mm
print()
print(n_cards)