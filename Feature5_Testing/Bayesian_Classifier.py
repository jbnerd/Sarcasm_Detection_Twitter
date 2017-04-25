import numpy as np
import csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.naive_bayes import GaussianNB

x = []
y = []

with open('feature5.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter = ' ')
	for row in reader:
		x.append(row[0: (len(row))])

for i in x:
	i[0] = i[0].split(',')
	y.append(i[0][-1])
	del i[0][-1]

X = []
for i in x:
	X.append(i[0])
Y = []
for i in y:
	Y.append(i)

#print(str(x[0]) + "\n")
#print(str(x[0])  + "     " + str(y[4000]) + "\n")

#X = np.asarray(X)
#Y = np.asarray(Y)

x = []
y = []

for i in X:
	temp = []
	for j in i:
		temp.append(float(j))
	x.append(temp)

for i in Y:
	temp = []
	for j in i:
		temp.append(float(j))
	y.append(temp)

#print(y[0])

x = np.asarray(x)
y = np.asarray(y)
#print(x[0])

#Naive Bayes Classifier

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 42)

clfnb = GaussianNB()
clfnb.fit(x_train, y_train)

print("Naive Bayes classifier")
print(clfnb.score(x_test, y_test))
print("\n")
