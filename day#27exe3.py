# Kon Banega Crorepati(KBC)

# list index through 1 to further not by 0
questions = [
    [
        "1.Who is the Prime Minister of Nepal?","Puspa Kamal Dahal","Khadga Prasad Oli","Sher Bahadur Deuba","Deepak Jaiswal",1
    ],
    [
        "2.Who is the Prime Minister of Nepal?","Puspa Kamal Dahal","Khadga Prasad Oli","Sher Bahadur Deuba","Deepak Jaiswal",1
    ],
    [
        "3.Who is the Prime Minister of Nepal?","Puspa Kamal Dahal","Khadga Prasad Oli","Sher Bahadur Deuba","Deepak Jaiswal",1
    ],
    [
        "4.Who is the Prime Minister of Nepal?","Puspa Kamal Dahal","Khadga Prasad Oli","Sher Bahadur Deuba","Deepak Jaiswal",1
    ],
    [
        "5.Who is the Prime Minister of Nepal?","Puspa Kamal Dahal","Khadga Prasad Oli","Sher Bahadur Deuba","Deepak Jaiswal",1
    ],
    [
        "6.Who is the Prime Minister of Nepal?","Puspa Kamal Dahal","Khadga Prasad Oli","Sher Bahadur Deuba","Deepak Jaiswal",1
    ],
    [
        "7.Who is the Prime Minister of Nepal?","Puspa Kamal Dahal","Khadga Prasad Oli","Sher Bahadur Deuba","Deepak Jaiswal",1
    ],
    [
        "8.Who is the Prime Minister of Nepal?","Puspa Kamal Dahal","Khadga Prasad Oli","Sher Bahadur Deuba","Deepak Jaiswal",1
    ],

    [
        "9.Who is the Prime Minister of Nepal?","Puspa Kamal Dahal","Khadga Prasad Oli","Sher Bahadur Deuba","Deepak Jaiswal",1
    ],
    [
        "10.Who is the Prime Minister of Nepal?","Puspa Kamal Dahal","Khadga Prasad Oli","Sher Bahadur Deuba","Deepak Jaiswal",1
    ],
    [
        "11.Who is the Prime Minister of Nepal?","Puspa Kamal Dahal","Khadga Prasad Oli","Sher Bahadur Deuba","Deepak Jaiswal",1
    ],
    [
        "12.Who is the Prime Minister of Nepal?","Puspa Kamal Dahal","Khadga Prasad Oli","Sher Bahadur Deuba","Deepak Jaiswal",1
    ],
    [
        "13.Who is the Prime Minister of Nepal?","Puspa Kamal Dahal","Khadga Prasad Oli","Sher Bahadur Deuba","Deepak Jaiswal",1
    ],
    [
        "14.Who is the Prime Minister of Nepal?","Puspa Kamal Dahal","Khadga Prasad Oli","Sher Bahadur Deuba","Deepak Jaiswal",1
    ],
    [
        "15.Who is the Prime Minister of Nepal?","Puspa Kamal Dahal","Khadga Prasad Oli","Sher Bahadur Deuba","Deepak Jaiswal",1
    ],

]
levels = [1000, 2000, 3000, 5000, 1000, 20000, 40000, 800000, 160000, 320000, 640000, 1250000, 2500000,5000000,10000000,30000000,70000000]
money = 0
for i in range(0,len(questions)):

    question = questions[i]
    print(f"\n Question for Rs.{levels[i]}")
    print(question[0])
    print(f"a. {question[1]}            b. {question[2]}")
    print(f"c. {question[3]}            d. {question[4]}")
    reply = int(input("Enter your answer (1-4): Or 0 to quit:\n "))
    if (reply == 0):
        money = levels[i-1]
        break
    if (reply == question[-1]):
        print(f"Yes,({question[1]})is correct answer, you have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong answer! ")
        break
print(f"Your take home money is {money}\n\n\n\n\n")