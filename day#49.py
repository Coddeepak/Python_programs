# # File Handeling in python
#
#
# # r for reading, w for writing, a for appending, x for create, t for text and b for binary.
#
#
#
#     # Read file
# # f = open('myfile.txt','r')
# f = open('myfile.txt')    # also works in the fabling way as r is a default
# # print(f)
# text = f.read()  # read/extract the file content.
# print(text)
# f.close()   # after writing it close the file.
#

    # Write file
# f = open('myfile1.txt','w')
# f.write('Hello,World!')
# f.close()








#     # Append file
# f = open('myfile1.txt','a')
# f.write('Hello,World!') # if we use append instead of write it throws error as for write and append (write) is same for both.
# f.close()



    # Using with statement we neednot to close a file as it is made like in python.
with open('myfile1.txt', 'a') as f:
    f.write("hey i am inside the freeze.")