s = {1, 2, 3, 4, 5}
print(s)

s.update([6, 7])
print(s)

s.remove(7)
print(s)

s1 = frozenset(s)
print(s1)

s1.remove(2)
print(s1)
