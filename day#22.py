l = [3,5,6]
print(l)
print(type(l))


marks = [3,5,6]
print(marks)
print(type(marks))
print([0])
print([1])
print([2])

marks = [3,5,6,"deepak", True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

marks1 = [3,5,6, "Deepak", True]
print(marks1[-3])   #Negative index
print(marks1[len(marks1)-3])  #Positive index
print(marks[5-3])  #Positive index
print(marks[2])   # Positive index

if "Deepak" in marks1:
    print("Yes")
else:
    print("No")

if 6 in marks1:
    print("Yes")
else:
    print("No")
Same thing is applied for strings as well
if "eepa" in "Deepak":
    print("Yes")

print(marks1)
print(marks1[:])
print(marks1[1:])
print(marks1[1:-1])
print(marks1[1:4])
print(marks1[1:4:2]) # 2 is jump index in the code

List comprehension   = on the flight list ko generate karaneko
lst = [i*i  for i in range(4)]
print(lst)


lst = [i  for i in range(4)]
print(lst)

lst1 = [i*i for i in range(10) if i%2 == 0]
print(lst1)







