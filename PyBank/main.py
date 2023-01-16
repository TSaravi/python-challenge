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
    change = 0
    greatest_increase = 0
    greatest_increase_date = ""
    greatest_decrease = 0
    greatest_decrease_date = ""


    for row in csvreader:
        # counting the total number of months in the dataset
        total_num_months = total_num_months + 1

        # the net total amount of profit/losses over the entire period
        total_net_amount = total_net_amount + int(row[1])

        # the changes in profit/losses over the entire period and then the average of those changes

        if prev_value == float('-inf'):
            prev_value = int(row[1])
            greatest_increase_date = row[0]

        else:
            change = int(row[1]) - prev_value
            average_change = average_change + change
            prev_value = int(row[1])

        #the greatest increase in profits(date and amount) over the entire period
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row[0]

        #the greatest decrease in profits(date and amount)over the entire period
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row[0]


    average_change = round(average_change/(total_num_months - 1), 2)
    
    line_1 = "Financial Analysis"
    line_2 = "----------------------------"
    line_3 = "Total Months:" + str(total_num_months)
    line_4 = "Total Months: $" + str(total_net_amount)
    line_5 = "Average Change: $" + str(average_change)
    line_6 = 'Greatest Increase in Profits: {} (${})'.format(greatest_increase_date, greatest_increase)
    line_7 = 'Greatest Decrease in Profits: {} (${})'.format(greatest_decrease_date, greatest_decrease)

print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)
print(line_6)
print(line_7)

text_path = "PyBank_export.txt"

with open(text_path, 'w') as file:
    file.write(line_1 + "\n")
    file.write(line_2 + "\n")
    file.write(line_3 + "\n")
    file.write(line_4 + "\n")
    file.write(line_5 + "\n")
    file.write(line_6 + "\n")
    file.write(line_7 + "\n")
    

