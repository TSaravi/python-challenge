import os 
import csv

#path to collect the data from the resource folder 
dirname = os.path.dirname(__file__)
election_data = os.path.join(dirname, "Resources","election_data.csv")

with open(election_data, 'r') as csvfile:
    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter =",")
    header = next(csvreader)

print(header)