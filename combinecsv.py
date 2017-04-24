import csv
import os

file1=open("feature1_norm.csv", "rb")
# file3=open("feature1_2.csv", "rb")
file2=open("feature1_2_past.csv", "rb")
outp=open("final_feature1.csv", "wb")
writer = csv.writer(outp)
r1,r2 = csv.reader(file1),csv.reader(file2)
import csv
# with open('A','rb') as f1, open('B','rb') as f2, open('out.csv','wb') as w:
writer = csv.writer(outp)
r1,r2 = csv.reader(file1),csv.reader(file2)
while True:
    try:
        writer.writerow(next(r1)+next(r2))
    except StopIteration:
        break