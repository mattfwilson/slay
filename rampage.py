normal_base = 8
plus_base = 8

rampage = []
rampage_plus = []
delta = []

for i in range(15):
    rampage.append(normal_base)
    normal_base += 5
    rampage_plus.append(plus_base)
    plus_base += 8

for i, j in zip(rampage_plus, rampage):
  print(i, j)
  diff = i - j
  delta.append(diff)

print(rampage)
print(rampage_plus)
print(delta)
