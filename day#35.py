#  loop with else in python programming


for i in range(5):
    print(i)

else:
    print("Sorry no i")


for i in []:
    print(i)

else:
    print("Sorry no i")


for i in range(6):
    print(i)
    if i == 4:
       continue     # continue the process

else:
    print("Sorry no i")


for i in range(6):
    print(i)
    if i == 4:
        break      # instantly break in the loop

else:
    print("Sorry no i")

i = 0
while i<7:
    print(i)
    i = i + 1
    # if i == 4:
#       break
else:
    print("Sorry i get it's limit")

for x in range(5):
    print("Iteration no {} in for loop.".format(x+1))
else:
    print("Else block in loop")
print("Out of loop")
