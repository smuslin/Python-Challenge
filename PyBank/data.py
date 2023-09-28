# Import the pathlib and csv library
import csv
from pathlib import Path

# Set the file path
csvpath = Path('Resources/budget_data.csv')

# Initialize variables to answer questions
list_date = []
total_months = 0
list_profit_loss = []
list_change_profit = []
max_increase = ["", 0]
max_decrease = ["", 999999999999]
total_net = 0  # Initialize net total to 0

# Open the input path as a file object
with open(csvpath) as csvfile:
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delimiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # Extract and store the data in appropriate lists
        date = str(row[0])
        profit_loss = int(row[1])
        list_date.append(date)
        list_profit_loss.append(profit_loss)
        total_net += profit_loss  # Accumulate total_net

# Calculate total_months
total_months = len(list_date)

# Calculate the change in profit/loss for each month
for i in range(1, len(list_profit_loss)):
    change = list_profit_loss[i] - list_profit_loss[i - 1]
    list_change_profit.append(change)

# Find the greatest increase and decrease in profits
max_increase[1] = max(list_change_profit)
max_decrease[1] = min(list_change_profit)

# Find the corresponding dates for the greatest increase and decrease
max_increase[0] = list_date[list_change_profit.index(max_increase[1]) + 1]
max_decrease[0] = list_date[list_change_profit.index(max_decrease[1]) + 1]

# Calculate the average change in profit/loss
average_change = round(sum(list_change_profit) / (total_months - 1), 2)

# Print the results
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_net}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})')
print(f'Greatest Decrease in Losses: {max_decrease[0]} (${max_decrease[1]})')
