d = open("19").read().split("\n\n")

rules = d[0].splitlines()
parts = d[1].splitlines()

def apply(part):
  node = 'in'
  print(part)
  while node not in ['A','R']:
    print(node)
    rule = rules_dct[node]
    for dec in rule:
      if dec['typ'] == '>':
        if part[dec['var']] > dec['val']:
          node = dec['result']
          break
      if dec['typ'] == '<':
        if part[dec['var']] < dec['val']:
          node = dec['result']
          break
  print(node)
  if node == 'A':
    return part['x'] + part['m'] + part['a'] + part['s']
  else:
    return 0


rules_dct = {}
for r in rules:
  tmp = r.replace("}","").split("{")
  inp = tmp[0]
  decisions = tmp[1].split(",")
  rules_dct[inp] = []
  for dec in decisions:
    if ":" not in dec:
      rules_dct[inp].append({"typ":">","var":"x","val":-1,"result":dec})
    else:
      comparison = dec.split(":")[0]
      var = comparison[0]
      typ = comparison[1]
      val = int(comparison[2:])
      result = dec.split(":")[1]
      rules_dct[inp].append({"typ":typ,"var":var,"val":val,"result":result})

allval = 0
for p in parts:
  p2 = p[1:-1].split(",")
  p3 = {}
  for i in p2:
    var = i[0]
    val = int(i[2:])
    p3[var] = val
  v = apply(p3)
  print(p,v)
  allval += v
print(allval)
