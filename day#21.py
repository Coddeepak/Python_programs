def average(a,b):
    print("The average is ",(a+b)/2)

average(4, 6)
def average(a=9, b=1):
    print("The average is ",(a+b)/2)

average(1,5)
def average(a=9, b=1):
    print("The average is ",(a+b)/2)

average(5)

def average(a=9, b=1):
    print("Th e average is ",(a+b)/2)

average(b=9)
def name(fname, mname = "Deepak",lname = "Jaiswal"):
    print("Hello,",fname ,mname ,lname)

name("Dipmala","Shah")

def average(a=9, b=1):
    print("The average is ",(a+b)/2)

average(b=9, a=21)
def average(a, b=1):
    print("The average is ",(a+b)/2)
average(a=21)

def average(a, b,c=1):
    print("The average is ",(a+b+c)/2)

average(5,6)

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
        print("Average is: ",sum / len(numbers))
average(5,6,7)

def name(**name):
    print(type(name))

    print("Hello,",name["fname"],name["mname"], name["lname"])

name(mname = "Prasad", lname = "Jaiswal", fname ="Lal")

def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
        # print("Average is: ",sum / len(numbers))
    return sum / len(numbers)
c = average(5,6,7,1)
print(c)


def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
        # print("Average is: ",sum / len(numbers))
    # return sum / len(numbers)
c = average(5,6,7,1)
print(c)



def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
        # print("Average is: ",sum / len(numbers))
    # return sum / len(numbers)
    return(7)
    return sum / len(numbers)
c = average(5,6,7,1)
print(c)