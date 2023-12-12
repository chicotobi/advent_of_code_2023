x = [i for i in '0123456789']

y = ['zero','one','two','three','four','five','six','seven','eight','nine']

def find_last_occurence_in_string(s,x):
  finds = [i for i in range(len(s)) if s.startswith(x, i)]
  if len(finds) > 0:
    return max(finds)
  else:
    return -1

def find_first_occurence_in_string(s,i):
  return s.find(i)


ss = 0
for i in open('1'):
  
  first = -1    
  last = -1
  for (idx,j) in enumerate(i):
    if j in x:
      last = int(j)
      last_idx = idx
      if first == -1:
        first = int(j)
        first_idx = idx

  # Look for first string digit
  z = [find_first_occurence_in_string(i,yy) for yy in y]
  z2 = [j for j in z if j > -1] 
  if len(z2) > 0:
    min_val = min(z2)
    if min_val < first_idx:
      first = z.index(min_val)
  
  # Look for last string digit
  z = [find_last_occurence_in_string(i,yy) for yy in y]
  z2 = [j for j in z if j > -1] 
  if len(z2) > 0:
    max_val = max(z2)
    if max_val > last_idx:
      last = z.index(max_val)
  
      
  ss += first * 10 + last
  print("this line:", i, first * 10 + last)