import numpy as np
import pandas as pd
import csv
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

x = []
y = []

with open('all.csv') as csvfile:
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

#print(y[0])

x = np.asarray(x)
y = np.asarray(y)

#Logistic Regression l1 classifier

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 42)

clfl1 = LogisticRegression(penalty = 'l1')
clfl1.fit(x_train, y_train)

print("Logistic Regression l1 type classifier")
print(clfl1.score(x_test, y_test))
print("\n")

#Logistic Regression l2 classifier

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 42)

clfl2 = LogisticRegression(penalty = 'l2')
clfl2.fit(x_train, y_train)

print("Logistic Regression l2 type classifier")
print(clfl2.score(x_test, y_test))
print("\n")
