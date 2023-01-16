import os 
import csv

#path to collect the data from the resource folder 
dirname = os.path.dirname(__file__)
election_data = os.path.join(dirname, "Resources","election_data.csv")

output = []

with open(election_data, 'r') as csvfile:
    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter =",")
    header = next(csvreader)

    total_votes = 0
    candidates = {}
    


    for row in csvreader: 
        candidate = row[2]
        #total number of votes cast
        total_votes = total_votes + 1 

        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1
        else:
            candidates[candidate] = 1




    output.append("Election Results")
    output.append("-------------------------")
    output.append("Total Votes: " + str(total_votes))
    output.append("-------------------------")
    

    for candidate in candidates:
        vote_percentage = round((candidates[candidate]/total_votes) * 100, 3)
        output.append('{} {}% ({})'.format(candidate, vote_percentage, candidates[candidate]))
        

    winner = ""
    highest_votes = 0
    for candidate in candidates:
        if candidates[candidate] > highest_votes:
            highest_votes = candidates[candidate]
            winner = candidate

    output.append("-------------------------")
    output.append('Winner: {}'.format(winner))
    output.append("-------------------------")



text_path = "PyPoll_export.txt"

with open(text_path, 'w') as file:
    for line in output:
        file.write(line + "\n")
        print(line)