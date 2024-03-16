#file handling
#how to read a text and write using py code
#function -
# to read
  #open("filename","mode")
#mode -
# 'r' - reading (default) , 'w' -write  (creating new file or truncates and existing one)
#'a' - appending
#'b' - binary  zoom.exe - binary
#'+' - for updating(reading and writing)

#read and write content
#   read entire content : content = file_obj.read()
#   read one line -> file_obj.readline()
#   read for all lines in a list -> file_obj.readlines()

#close the file

ob1 = open("testdata.txt", "r")
#print(ob1.read())
print(ob1.readline(),end="")
print(ob1.readline(),end="")
print(type(ob1))
ob1.close()





