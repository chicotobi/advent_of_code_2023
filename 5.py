# input_range: input_start_value, input_range_length
# rule: destination_range_start, source_range_start, range_length
def apply_rule(input_range, rule):  
  # Application of a rule may result in splitting the input range in up to three parts
  x0, xl = input_range
  dst, r0, rl = rule
  # Check all cases...
  if x0 < r0:
    if x0 + xl <= r0:
      # One unmapped range, zero mapped ranges
      new_ranges_unmapped = [input_range]
      new_ranges_mapped = []
    elif x0 + xl <= r0 + rl:
      # One unmapped range, one mapped range
      new_ranges_unmapped = [[x0,r0-x0]]
      new_ranges_mapped = [[dst,x0+xl-r0]]
    else:
      # Two unmapped ranges, one mapped range
      new_ranges_unmapped = [[x0,r0-x0],[r0+rl,x0+xl-r0-rl]]
      new_ranges_mapped = [[dst,rl]]
  elif x0 < r0 + rl:
    if x0 + xl <= r0 + rl:
      # One mapped range, zero unmapped range
      diff = x0 - r0
      x1 = dst + diff
      new_ranges_unmapped = []
      new_ranges_mapped = [[x1,xl]]
    else:
      # One unmapped range, one mapped range
      new_ranges_unmapped = [[r0+rl,x0+xl-r0-rl]]
      new_ranges_mapped = [[x0+dst-r0,r0+rl-x0]]
  else:
    # One unmapped range, zero mapped ranges
    new_ranges_unmapped = [input_range]
    new_ranges_mapped = []
  return new_ranges_unmapped, new_ranges_mapped

assert apply_rule([79,1],[52,50,48]) == ([],[[81,1]])


assert apply_rule([5,1],[100,10,5]) == ([[5,1]],[])
assert apply_rule([12,1],[100,10,5]) == ([],[[102,1]])
assert apply_rule([12,3],[100,10,5]) == ([],[[102,3]])

# With split
assert apply_rule(input_range = [12,8], rule = [100,10,5]) == ([[15,5]],[[102,3]])
assert apply_rule(input_range = [8,5], rule = [100,10,5]) == ([[8,2]],[[100,3]])
assert apply_rule(input_range = [8,12], rule = [100,10,5]) == ([[8,2], [15,5]], [[100,5]])

# walk seeds
ranges_unmapped = []
for i in open('5'):
  if 'seeds' in i:
    seeds = i.split(": ")[1].replace("\n","").split(" ")# Round 1
    seeds = [int(j) for j in seeds]
    # Round 1
    #ranges_mapped = [[i,1] for i in seeds]
    # Round 2
    ranges_mapped = list(zip(seeds[::2],seeds[1::2]))
    continue
  if 'map' in i:
    ranges_unmapped = ranges_mapped
    ranges_mapped = []
    print("apply rules in",i[:-1])
    continue
  if i == '\n':
    ranges_mapped += ranges_unmapped
    ranges_unmapped = []
    continue
  rule = [int(j) for j in i.replace("\n","").split(" ")]
  tmp = []
  for range0 in ranges_unmapped:
    new_ranges_unmapped, new_ranges_mapped = apply_rule(range0,rule)
    #print("applied rule",rule,"to range",range0)
    #print("result: new_ranges_unmapped",new_ranges_unmapped)
    #print("result: new_ranges_mapped",new_ranges_mapped)
    ranges_mapped += new_ranges_mapped
    tmp += new_ranges_unmapped
  ranges_unmapped = tmp
  #print("applied rule ",rule,"to all ranges")
  #print("result: ranges_unmapped",ranges_unmapped)
  #print("result: ranges_mapped",ranges_mapped)
  #print()
ranges_mapped += ranges_unmapped
ranges_unmapped = []
#print(ranges_mapped)
print(min(i for (i,j) in ranges_mapped))