normal_base = 8
plus_base = 8

rampage = []
rampage_plus = []

for i in range(15):
    rampage.append(normal_base)
    normal_base += 5
    rampage_plus.append(plus_base)
    plus_base += 8

delta = [rampage_plus[i] - rampage[i] for i in range(len(rampage))]

print(rampage)
print(rampage_plus)
print(delta)
