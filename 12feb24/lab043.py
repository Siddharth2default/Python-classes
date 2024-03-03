#break
#for -> 1 to 10 -> range(1,11,1)
#i = 5 -> break from the loop - kicked out from loop
for counter in range(1,11):
    if counter==5:
        break
    print(counter)
print("out of loop")