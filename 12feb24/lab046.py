#triangle classifier
#side1== side2 ==side3 -> eq
#s1==s2 or s2==s3 or s1==s3 -> iso
#else-> scalene
s1 = float(input("Enter side 1\n"))
s2 = float(input("Enter side 2\n"))
s3 = float(input("Enter side 3\n"))
if s1==s2==s3:
    print("eql")
elif s1==s2 or s2==s3 or s3==s1:
    print("ISO")
else:
    print("scalene")