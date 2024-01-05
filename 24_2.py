import sympy as sp

d = open('24_test').read().splitlines()

hail = []
for i in d:
  x, d = i.split(" @ ")
  x, y, z = x.strip().split(", ")
  a, b, c = d.strip().split(", ")
  hail += [(int(x),int(y),int(z),int(a),int(b),int(c))]

nhail = 4

symbols = 'x y z a b c ' + ' '.join('l'+str(i) for i in range(nhail))
symbs = sp.symbols(symbols)

equations = []
for i in range(nhail):
  l = 'l' + str(i)
  x1, y1, z1, a1, b1, c1 = hail[i]
  eqx = 'x + ' + l + ' * a - ' + str(x1) + ' - ' + l + ' * ' + str(a1)
  eqy = 'y + ' + l + ' * b - ' + str(y1) + ' - ' + l + ' * ' + str(b1)
  eqz = 'z + ' + l + ' * c - ' + str(z1) + ' - ' + l + ' * ' + str(c1)
  equations += [eqx, eqy, eqz]
  
eqs = [sp.sympify(i) for i in equations]
  
solutions = sp.solve(eqs, symbs)
print(sum(solutions[0][:3]))