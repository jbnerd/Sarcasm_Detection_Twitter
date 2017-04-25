import numpy as np
import csv
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn import tree
import random

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

#print(str(X[0]) + "\n")
#print(str(X[0])  + "     " + str(Y[4000]) + "\n")

X = np.asarray(X)
Y = np.asarray(Y)

for i in X:
	for j in i:
		j = float(j)

for i in Y:
	for j in i:
		j = float(j)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1, random_state = 42)

#SVM classifier 
clf = svm.SVC()
clf.fit(x_train, y_train)

print("SVM rbf kernel Classifier")
print(clf.score(x_test, y_test))
print("\n")

#Decision Tree Classifier

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1, random_state = 42)

clftree = tree.DecisionTreeClassifier()
clftree.fit(x_train, y_train)

print("Decision Tree Classifier")
print(clftree.score(x_test, y_test))
print("\n")

x = []
y = []

for i in range(0, len(X)):
	a = random.uniform(0, 5)
	if a <= 1:
		x.append(X[i])
		y.append(Y[i])
print('random sampling')

#SVM polynomial classifier

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.5, random_state = 42)

clf = svm.SVC(kernel = 'poly')
clf.fit(x_train, y_train)

print("SVM polynomial kernel Classifier")
print(clf.score(x_test, y_test))
print("\n")
