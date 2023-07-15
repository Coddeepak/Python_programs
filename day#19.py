for i in range(12):
    if(i == 10):
        break
    print("5 x", i+1, "=",5 * (i+1))


print("Loop ko chodjar nikal gaya")

# loop ko chodkar nikal jawo = break/stop from this on way.
# iteration/skip  ko chodkar nikal jawo = continue

for i in range(12):
    if(i == 10):
        print("Skip the iteration.")
        continue
    print("5 x", i+1,"=",5*(i+1))