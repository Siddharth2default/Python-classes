#CSV files
import csv
with open('data1.csv') as csvfile:
    reader = csv.reader(csvfile)
    for a in reader:
        print(a[0],a[1],a[2],sep="}")
