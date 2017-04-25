import numpy as np
import csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import SGDClassifier

x = []
y = []

with open('output.csv') as csvfile:
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

#print(str(X[0]) + "\n")
#print(str(X[0])  + "     " + str(Y[4000]) + "\n")

X = np.asarray(X)
Y = np.asarray(Y)

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

print(y[0])

x = np.asarray(x)
y = np.asarray(y)

#SGDClassifier

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 42)

clf = SGDClassifier()
clf.fit(x_train, y_train)

print("SGDClassifier")
print(clf.score(x_test, y_test))
print("\n")
