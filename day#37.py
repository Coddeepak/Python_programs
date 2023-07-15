## finally keywords in python


# It is mainly always executed in function as it is executable in python
# try:
#     l= [1,5,6,6,7]
#     i = int(input("Enter the index "))
#     print(l[i])
# except:
#     print("Some error occured!")
# finally:
#     print("I am always executed")
# print("I am always executed")


def function():
    try:
        l = [1,5,6,7,8]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    # except:
    #     print("Some error occured")
    finally:
        print("I am always executed.")
        return 0
    print("I am always executed.")
x = function()
print(x)