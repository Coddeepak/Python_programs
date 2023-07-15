l = [11,21,12,1,2,3,4,6]
print(l)
l.append(7)
print(l)
l.sort()
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(1))
print(l.count(1))
print(l)
m = l
m[0]=0
print(l)
m=l.copy()
m[0]=0
print(l)
l.insert(1,899)
print(l)
m = [900,1000,1100]
l.extend(m)
print(l)
k = l + m
print(k)