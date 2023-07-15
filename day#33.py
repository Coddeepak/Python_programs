#dictionary in python


dic = {
    "Harry":"Human Being",
    "Spoon":"Objects"
}
print(dic["Harry"])
dic1 = {
    344 : "Deepak",
    543 : "Neha",
    454 : "Subham",
    646 : "Gautam"
}

print(dic1[543])
info = {'name': 'Karan', 'age':18, 'eligible': True}
print(info)
print(info['name'])             # it give error for not given   #  two ways to get out the values from dictionary
print(info.get('eligible'))       # this donot give the error
print(info['name2'])
print(info.get('name2'))


info = {
    'name':'Karan', 'age':'18', 'eligible':True
}
print(info)
print(info.keys())          # this gives key as dictionary

for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")
info = {
    'name':'deepak', 'age': '18', 'eligible': True
}
print(info.items())
for key,value in info.items():
    print(f"The value corresponding to  the  {key} is {value}")
    dictionary creates mapping among the data