d = open("19").read().split("\n\n")

rules = d[0].splitlines()
parts = d[1].splitlines()

def apply(part,node):
  if node == 'A':
    return len(part['x']) * len(part['m']) * len(part['a']) * len(part['s'])
  if node == 'R':
    return 0
  v = 0
  while len(part['x']) > 0:
    rule = rules_dct[node]
    for dec in rule:
      new_part = part.copy()
      if dec['typ'] == '>':
        new_part[dec['var']] = [i for i in new_part[dec['var']] if i > dec['val']]
        v += apply(new_part,dec['result'])
        part[dec['var']] = [i for i in part[dec['var']] if i <= dec['val']]
      if dec['typ'] == '<':
        new_part[dec['var']] = [i for i in new_part[dec['var']] if i < dec['val']]
        v += apply(new_part,dec['result'])
        part[dec['var']] = [i for i in part[dec['var']] if i >= dec['val']]
  return v

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
    p3[var] = [val]
  v = apply(p3,'in')
  print(p,v)
  allval += v
print(allval)


out = apply({"x":range(1,4001),"m":range(1,4001),"a":range(1,4001),"s":range(1,4001)},"in")
print(out)
