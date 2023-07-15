# Write a python program to translate a message into secret code language.Use below
# rules to translate normal normal english language into secret code language.

 # coding:
 # if the code word contains atleast 3 characters, remove the first letter and append it at the end
 # now append three random characters at the starting and the end
 # else:
#    simply reverse the string


# decoding:
# if th word contains less than 3 characters, reverse it
# else:
#     remove 3 random characters from start and end.Now remove the last letter and append it to the beginning
# your program should ask whether you want to code or decode




st = input("Enter the message: ")
words = st.split(" ")
coding = input("1 for Coding  or 0 for Decoding: ")
coding = True if (coding == "1") else False
print(coding)
if(coding):
    nwords = []
    for word in words:
        if(len(st)>=3):
            r1 = "dsf"
            r2 = "des"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
        if (len(st) >= 3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))



















    




import string
import random
def code_word(user1,key):
    b = user1.split()
    list = []
    for i in b:
        if(len(i)<3):
            a = i[::-1]
            list.append(a)
        else:
            code = i[1:] + i[0]
            code1 = " ".join(random.choices(string.ascii_lowercase,k=key)) + code + " ".join(random.choices(string.ascii_lowercase,k=key))
            list.append(code1)
    a = " ".join(list)
    return a
def decode_word(user, key):
    b = user.split()
    list = []
    for i in b:
        if(len(i) < 3):
            code = i[::-1]
            list.append(code)
        else:
            code2 = i[key:-key]
            try:
                code1 = code2[-1] + code2[:-1]
            except IndexError:
                print("Your encryption key is greater than message: ")
            list.append(code)
    a  = " ".join(list)
    return a
while True:
    u = input("Enter code or Decode or Quit: ")
    if(u.lower() == "code"):
        user1 = input("Enter your message: ")
        try:
            user2 = int(input("Enter your key as (3 or 4  or 6): "))
        except Exception as a :
            pass
        try:
            print(code_word(user1, user2))
        except Exception as a:
            print("Please enter only one digits for encryption: ")
    elif(u.lower() == "decode"):
        user1 = input("Enter your message: ")
        try:
            key = int(input("Enter your key for decryption:"))
            if(key>len(user1)):
                print("Your decryption key is greater than message: ")
            else:
                print(decode_word(user1, key))
        except Exception as e:
            print("Please enter only digits for decryption: ")
    elif(u.lower()== "quit"):
        break
    else:
        print("Please enter valid detail: ")














def code():
    d = input("Please enter your message here: ")
    words = d.split()
    code = list()
    for a in words:
        if(len(a)<=2):
            word = a[1:]+a[0]
            code.append(word)
        else:
            last = a[:-1]
            first = a[0]
            second = a[3]
            word = a[1:] +a[0]
            fword = first + last + second + word + last + second + first
            code.append(fword)
    scode = " "
    return (scode.join(code))

