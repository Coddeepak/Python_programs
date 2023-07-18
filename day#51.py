       # Other file handling functions in python




# seek() function
with open('file4.txt', 'r') as f:
    print(f)    # Output : Built in I/O module
    # Move to the 10th byte in the file
    f.seek(10)


    # Read the next 5 bytes
    data = f.read(5)
    print(data)

# tell() function
with open('file4.txt','r') as f:
    print(type(f))
    # move to the 10th byte in the file
    f.seek(f.tell())
    data = f.read(5)
    print(data)  # Output : 12345

with open('file4.txt','r') as f:
    print(type(f))
    # move to the 10th byte in the file
    # Show the location where we are
    print(f.tell())
    data = f.read(5)


# truncate() function

with open('sample.txt', 'w') as f:
    f.write("Hello World!")
    f.truncate(5)  # Size of the file should be 5 if we write 6 it give upto 6 size.


with open('sample.txt','r') as f:
    print(f.read())
