# local and global varialble in python
# x = 4   # global variable
# print(x)
#
#
#
# def hello():
#     x = 5   # local variable
#     print(x)
#     print("Hello Deepak")
#
# hello()


# x= 4
# print(x)
#
# def hello():
#      x = 5
#      print(f"The local x is {x}")
#      print("Hello Deepak")
#
# print(f"The global x is {x}")
# hello()
# x = 5
# print(f"The global x is {x}")


# local variable is defined in a function & also accessable through it and global variable is defined in the code



x = 10 # global variable

def my_function():
    global x    # changes global vairble
    x = 4
    y = 5 # local variable
    print(y)

my_function()
locals()    # this lend the local variable to run out from the function and update the data of the variable
print(x)


# print(y)  # this throws error as it is a local variable in the function not a global variable


