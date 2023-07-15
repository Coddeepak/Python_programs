# set methods in python


s = {1,2,3,5,6,6}
s1 = {3,4,45,7,6}
print(s.union(s1))
s.update(s1)
print(s ,s1)
print(s.intersection(s1))


cities = { "Tokyo", "Madrid", "Kathmandu", "Kabul"}
cities1 = { "Tokyo", "Delhi","Paris","Dhaka"}
cities3 = cities.union(cities1)
print(cities3)

cities = { "Tokyo", "Madrid", "Kathmandu", "Kabul"}
cities1 = { "Tokyo", "Delhi","Paris","Dhaka"}
cities3 = cities.intersection_update(cities1)
print(cities)

cities = { "Tokyo", "Madrid", "Kathmandu", "Kabul"}
cities1 = { "Tokyo", "Delhi","Paris","Dhaka"}
cities3 = cities.symmetric_difference(cities1)
print(cities3)

cities = { "Tokyo", "Madrid", "Kathmandu", "Kabul"}
cities1 = { "Tokyo", "Delhi","Paris","Dhaka"}
cities3 = cities.difference(cities1)
print(cities3)


cities = { "Tokyo", "Madrid", "Kathmandu", "Kabul"}
cities1 = { "Tokyo", "Delhi","Paris","Dhaka"}
cities3 = cities.update(cities1)
print(cities)


cities = { "Tokyo", "Madrid", "Kathmandu", "Kabul"}
cities1 = { "Tokyo", "Delhi","Paris","Dhaka"}
cities3 = cities.isdisjoint(cities1)
print(cities3)

cities = { "Tokyo", "Madrid", "Kathmandu", "Kabul"}
cities1 = { "Tokyo", "Delhi","Paris","Dhaka"}
cities3 = cities.issubset(cities1)
print(cities3)

cities = { "Tokyo", "Madrid", "Kathmandu", "Kabul"}
cities1 = { "Tokyo", "Delhi","Paris","Dhaka"}
cities3 = cities.issuperset(cities1)
print(cities3)

cities = { "Tokyo", "Madrid", "Kathmandu", "Kabul"}
cities.add("Sydney")
print(cities)

cities = { "Tokyo", "Madrid", "Kathmandu", "Kabul"}
cities.remove("Tokyo")
print(cities)

cities = { "Tokyo", "Madrid", "Kathmandu", "Kabul"}
cities1 = { "Tokyo", "Delhi","Paris","Dhaka"}
cities.update(cities1)
print(cities)

cities = { "Tokyo", "Madrid", "Kathmandu", "Kabul"}
cities.discard("Delhi")
print(cities)

cities = { "Tokyo", "Madrid", "Kathmandu", "Kabul"}
item = cities.pop()  # pop give one out of this set
print(cities)
print(item)

cities = { "Tokyo", "Madrid", "Kathmandu", "Kabul"}
del cities   # it throws error throughout the program execution
print(cities)


cities = { "Tokyo", "Madrid", "Kathmandu", "Kabul"}
cities.clear()  # it doesnot throws error, it throws empty set
print(cities)

info = {"California", 19, False, 5.6}
if "California" in info:
    print("California is present in the sentence.")
else:
    print("California is not present in the sentence.")