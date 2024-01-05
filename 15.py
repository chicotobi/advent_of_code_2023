d = open('15').read().splitlines()[0]

d2 = d.split(",")

def myhash(x):
  s = 0
  for i in x:
    s += ord(i)
    s *= 17
    s = s%256
  return s

def process(x, boxes):
  print(x)
  if '=' in x:
    label, focal = x.split("=")
    idx = myhash(label)
    box = boxes[idx]
    replaced = False
    for (i,(label0,focal0)) in enumerate(box):
      if label0 == label:
        box[i] = (label,focal)
        replaced = True
        break
    if not replaced:
      box.append((label,focal))
  elif '-' in x:
    label = x.split("-")[0]
    idx = myhash(label)
    box = boxes[idx]
    tmp = [i for i in box if i[0]==label]
    if len(tmp) > 0:
      box.remove(tmp[0])      
  else:
    raise
  boxes[idx] = box
  return boxes

boxes = {i:[] for i in range(256)}
for i in d2:
  boxes = process(i,boxes)
  bx2 = {k:v for (k,v) in boxes.items() if len(v)>0}
  print(bx2)
  
# score
ss = sum((k+1)*(i+1)*int(j) for (k,v) in boxes.items() if len(v)>0 for (i,(l,j)) in enumerate(v))
print(ss)