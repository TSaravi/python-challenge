import os
import csv

# Path to collect data from the resource folder
dirname = os.path.dirname(__file__)
budget_data = os.path.join(dirname, "Resources", "budget_data.csv")
# budget_data = "python-challenge/PyBank/Resources/budget_data.csv"


with open(budget_data, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    total_num_months = 0
    total_net_amount = 0
    average_change = 0
    prev_value = float('-inf')

    for row in csvreader:
        # counting the total number of months in the dataset
        total_num_months = total_num_months + 1

        # the net total amount of profit/losses over the entire period
        total_net_amount = total_net_amount + int(row[1])

        # the changes in profit/losses over the entire period and then the average of those changes

        if prev_value == float('-inf'):
            prev_value = int(row[1])

        else:
            change = int(row[1]) - prev_value
            average_change = average_change + change
            prev_value = int(row[1])

    average_change = round(average_change/(total_num_months - 1), 2)

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:", total_num_months)
    print("Total Months: $" + str(total_net_amount))
    print("Average Change: $" + str(average_change))
