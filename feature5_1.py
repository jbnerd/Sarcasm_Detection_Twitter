import csv
import os

pwd = os.getcwd()
norm_input = pwd + "/normal_with_past_PP"
sarc_input = pwd + "/sarcastic_with_past_PP"
csvfile = open("feature5_1.csv","w")
f5 = csv.writer(csvfile,delimiter=",")


for f in sorted(os.listdir(norm_input)):
	input_file = open(os.path.join(norm_input, f), "r")
	reader = csv.reader(input_file)
	reader = list(reader)
	required = reader[1][2]
	letters = required.split(" ")
	let = "".join(letters)
	letters = []
	for c in let:
		letters.append(c)
	tot_letts = len(letters)
	letters = list(set(letters))
	if(tot_letts != 0):
		prob = len(letters)/tot_letts
	temp = []
	temp.append(prob)
	temp.append(tot_letts)
	f5.writerow(temp)
	input_file.close()

for f in sorted(os.listdir(sarc_input)):
	input_file = open(os.path.join(sarc_input, f), "r")
	reader = csv.reader(input_file)
	reader = list(reader)
	required = reader[1][2]
	letters = required.split(" ")
	letters = "".join(letters)
	let = "".join(letters)
	letters = []
	for c in let:
		letters.append(c)
	tot_letts = len(letters)
	letters = list(set(letters))
	if(tot_letts != 0):
		prob = len(letters)/tot_letts
	temp = []
	temp.append(prob)
	temp.append(tot_letts)
	f5.writerow(temp)
	input_file.close()

csvfile.close()