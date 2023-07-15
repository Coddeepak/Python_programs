# set data type in python
s = { 2,3,4,5,2,3,3,4,5,4,2,}
print(s)

# set doesnot maintain order of set
info = {"Carla", 19, False, 5.9, 19}
print(info)
# it gives empty dictionary not set cause both have same syntax
harry = {}
print(type(harry))

harry = set() # this will give set
print(type(harry))
for value in info:  # for i in info is not used in set vaule is used instead of i

    print(value)