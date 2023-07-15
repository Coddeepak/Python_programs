# while loop in python


for i in range(3):
    print(i)


i = 0
while(i<=3):
    print(i)
    i= i+1
print("Done with the loop")


i = int(input("Enter the number: "))
print(i)
while(i<=38):
    i = int(input("Enter the number: "))
    print(i)
print("Done with the loop")

i = 0
while True:
    print(i)
    i = i+ 1
    if (i%100 == 0):
        break



count = 5
while (count > 0):
    print(count)
    count = count - 1
else:
    print("I am inside else")



# in other language like c

#     do {
#     #loop body:
# }while(condition);

while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number>0:
        break