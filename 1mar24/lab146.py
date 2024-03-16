with open("testdata2.txt", 'r') as file:
    lines = file.readlines()
    print(type(lines))
for i in lines:
    print(i,end="")

with open("testdata2.txt", 'a') as file3:
    file3.write("last char")
