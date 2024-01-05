d = open('24_test').read().splitlines()

hail = []
for i in d:
  x, d = i.split(" @ ")
  x, y, z = x.strip().split(", ")
  a, b, c = d.strip().split(", ")
  hail += [(int(x),int(y),int(z),int(a),int(b),int(c))]

vmin = 7
vmax = 27

#vmin = 200000000000000
#vmax = 400000000000000

n = len(hail)
s = 0
for i in range(n):
  for j in range(i+1,n):
    x1,y1,z1,a1,b1,c1 = hail[i]
    x3,y3,z3,a3,b3,c3 = hail[j]
    
    x2 = x1 + a1
    y2 = y1 + b1
    
    x4 = x3 + a3
    y4 = y3 + b3
    
    denom = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    
    result = "good"
    if denom != 0:
      nomx = (x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)
      nomy = (x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)
      xp = nomx / denom
      yp = nomy / denom
      # check for test area:
      if not (vmin <= xp <= vmax and vmin <= yp <= vmax):
        result = "outside"
        
      if (x2-x1) * (xp-x1) < 0:
        result = "in the past"
      elif (x2-x1) * (xp-x1) == 0:
        raise
        
      if (x4-x3) * (xp-x3) < 0:
        result = "in the past"
      elif (x4-x3) * (xp-x3) == 0:
        raise
    else:
      result = "parallel"
    
    #print(i,j,result)
    if result == "good":
      s += 1
      print(i,j,result)
      print("intersect at",xp,yp)
      
      