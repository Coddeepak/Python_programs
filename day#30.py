# Recursion in python

# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(3) = 3*2*1
# factorial(2) = 2*1
# factorail(1) = 1
# factorail(0) = 1


# factorail(n) = n * factorial(n-1)
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(3))
# print(factorial(4))
# print(factorial(5))

# print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1


# Ficonacci  Sequence
# Quick Quiz: write a program to print the fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f1 + f0
# f(n) = f(n-1) + f(n-2)


# def fibonacci():
#     n = int(input("Enter how many Fibonacci numbers you want to display: "))
#     a = 0
#     b = 1
#
#     if n == 1:
#         print(a)
#     elif n >= 2:
#         print(a, b, end=" ")
#
#         for i in range(2, n):
#             f = a + b
#             print(f, end=" ")
#             a = b
#             b = f
#
# fibonacci()
# # Using recursion concept
#
# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         sequence = fibonacci(n - 1)
#         sequence.append(sequence[-1] + sequence[-2])
#         return sequence
#
# n = int(input("Enter how many Fibonacci numbers you want to display: "))
# fib_sequence = fibonacci(n)
# print("Fibonacci sequence:", fib_sequence)


