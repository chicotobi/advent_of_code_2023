d = open('9').read().splitlines()
d2 = [[int(i) for i in j.split(" ")] for j in d]

def predict(x):
  if len(set(x)) == 1:
    return x[0]
  else:
    x2 = [j-i for i, j in zip(x[:-1], x[1:])]
    return x[-1] + predict(x2)
  
s = sum(predict(i[::-1]) for i in d2)
print(s)