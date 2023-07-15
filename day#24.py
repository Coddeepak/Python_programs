# Tuple are not changed if written at once


tup = (1,5,6)
print(type(tup), tup)
tup = (1,)  # for tuple to support we need to give comma at last
print(type(tup), tup)

tup = (1,2,3,5,46,656,"green",True)
tup[0]= 90
print(type(tup), tup)
print(tup[0])
print(len(tup))
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
print(tup[6])
print(tup[7])
print(tup[-1])
if 46 in tup:
    print("Yes, 46 is present in this tuple")

Ntup2 = tup[1:4]
print(tup2)