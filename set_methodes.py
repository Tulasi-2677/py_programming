s = {1,4,5,6,78,34,5,5,"sila"}
print(s,type(s))
s.add(99)
print(s,type(s))
s.pop()
print(s)

A = {1, 2, 3}
B = {3, 4, 5}

A.add(6)
print(A)                      # {1, 2, 3, 6}

A.update([7, 8])
print(A)                      # {1, 2, 3, 6, 7, 8}

A.remove(2)
print(A)                      # {1, 3, 6, 7, 8}

print(A.union(B))             # {1, 3, 4, 5, 6, 7, 8}
print(A.intersection(B))      # {3}
print(A.difference(B))        # {1, 6, 7, 8}
print({1, 2}.issubset({1, 2, 3}))      # True
print({1, 2, 3}.issuperset({2}))       # True

