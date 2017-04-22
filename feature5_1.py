import csv
import os

pwd = os.getcwd()
norm_input = pwd + "/normal_with_past"
sarc_input = pwd + "/sarcastic_with_past"

result = []

for f in os.listdir(norm_input):
	input_file = open(os.path.join(norm_input, f), "r")
	reader = csv.reader(input_file)
	temp_res = []
	for row in reader:
		required = row[2]
		letters = []
		for i in required:
			letters.append(i)
		tot_letts = len(letters)
		letters = list(set(letters))
		if(tot_letts != 0):
			prob = len(letters)/tot_letts
		temp = []
		temp.append(prob)
		temp.append(tot_letts)
		temp_res.append(temp)
	result.append(temp_res)


for f in os.listdir(sarc_input):
	input_file = open(os.path.join(sarc_input, f), "r")
	reader = csv.reader(input_file)
	temp_res = []
	for row in reader:
		letters = []
		required = row[2]
		letters = []
		for i in required:
			letters.append(i)
		tot_letts = len(letters)
		letters = list(set(letters))
		if(tot_letts != 0):
			prob = len(letters)/tot_letts
		temp = []
		temp.append(prob)
		temp.append(tot_letts)
		temp_res.append(temp)
	result.append(temp_res)
print(result)