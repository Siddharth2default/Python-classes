import csv

data = [['name','age'],['alice',30,'NY'],['bob',25,'LA']]
try:
    with open('data1.csv', 'a') as fileA:
        content = csv.writer(fileA)
        content.writerows(data)
except FileNotFoundError as e:
    print(e)
finally:
    fileA.close()

