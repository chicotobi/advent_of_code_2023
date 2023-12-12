from collections import Counter

l = []
for i in open('7'):
  tmp = i.replace("\n","").split(" ")
  tmp[1] = int(tmp[1])
  l.append(tmp)

def card_value(char):
  if char == 'A':
    return 14
  if char == 'K':
    return 13
  if char == 'Q':
    return 12
  if char == 'J':
    return 11
  if char == 'T':
    return 10
  return int(char)

def hsh(hand):
  return hand[0] * 15**4 + hand[1] * 15**3 + hand[2] * 15**2 + hand[3] * 15 + hand[4]

def fitness(item):
  x = [card_value(i) for i in item[0]]
  val = 0
  ct = Counter(x).values()
  if 5 in ct:
    val += 10e9
  elif 4 in ct:
    val += 9e9
  elif 3 in ct and 2 in ct:
    val += 8e9
  elif 3 in ct:
    val += 7e9
  elif 2 in Counter(ct).values():
    val += 6e9
  elif 2 in ct:
    val += 5e9
  val += hsh(x)
  return val

l.sort(key = fitness)

l0 = len(l)
value = sum((position+1) * bet for (position,(hand, bet)) in enumerate(l))