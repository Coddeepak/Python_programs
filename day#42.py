# enumerate function in python


marks = [12, 56, 34, 45,34,56,67,76,67]
index = 0
for mark in marks:
     print(mark)
     if(index == 3):
         print("Deepak, awesome!")
     index += 1




marks1 = [56,45,46,66,66,88,78,92,88,89]
for index, mark in enumerate(marks1):
    print(mark)
    if(index == 3):
        print("Deepak, Awsome!")


fruits = ['apple', 'banana','mango']
for index, fruit in enumerate(fruits):
    print(index,fruit)


sports = ['football','cricket','basketball']
for index,sport in enumerate(sports,start=2):
    print(index,sport)