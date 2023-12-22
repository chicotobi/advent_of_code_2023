# read data
d = {}
for i in open('20').read().splitlines():
  inp, dst = i.split(" -> ")
  typ = inp[0]
  s_dst = dst.split(", ")
  if typ == 'b':
    d["broadcaster"] = {"typ":"broadcaster", "dst":s_dst, "state": False}
  elif typ == '%':
    src = inp[1:]
    d[src] = {"typ": "flipflop", "dst": s_dst, "state": False}
  elif typ == '&':
    src = inp[1:]
    d[src] = {"typ": "nand", "dst": s_dst, "memory": {}, "state": True}
  elif typ == 'o':
    src = inp[1:]
    d["output"] = {"typ": "output", "dst": []}

# initialize memory of nand
for (src,dct) in d.items():
  for s_dst in dct["dst"]:
    if s_dst in d.keys():
      if d[s_dst]["typ"] == 'nand':
        d[s_dst]["memory"][src] = False

d = dict(sorted(d.items()))

# get the interesting part

nand_gate = [k for (k,v) in d.items() if v["dst"]==["rx"]][0]
monitor_states = list(d[nand_gate]["memory"].keys())

# process
lows = 0
highs = 0
n_buttons = 0

while True:
  pulses = [("button",False,"broadcaster")]

  n_buttons += 1

  inp_was_high = {i:False for i in monitor_states}

  while len(pulses) > 0:
    for (s,v,r) in pulses:
      msg = s + (" -high" if v else " -low") + "-> " + r
      if v:
        highs += 1
      else:
        lows += 1
    # send pulses
    new_pulses = []

    for (s_snd, value, s_rec) in pulses:
      if s_rec not in d.keys():
        if not value:
          print(n_buttons)
          raise
        continue

      rec = d[s_rec]

      for ss in monitor_states:
        if d[ss]["state"]:
          inp_was_high[ss] = True

      # Handle broadcaster
      if rec["typ"] == "broadcaster":
        rec["state"]
        for i in rec["dst"]:
          new_pulses += [(s_rec,rec["state"], i)]

      # Handle flipflop
      if rec["typ"] == "flipflop":
        if not value:
          rec["state"] = not rec["state"]
          for i in rec["dst"]:
            new_pulses += [(s_rec,rec["state"], i)]

      # Handle nand
      if rec["typ"] == "nand":
        rec["memory"][s_snd] = value
        rec["state"] = not all(rec["memory"].values())
        for i in rec["dst"]:
          new_pulses += [(s_rec,rec["state"], i)]
    pulses = new_pulses

  if any(inp_was_high.values()):
    print(inp_was_high,n_buttons)

print(highs*lows)
