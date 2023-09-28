# Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvpath = Path('C:\\Users\\samus\\OneDrive\\Desktop\\UCB-VIRT-FIN-PT-09-2023-U-LOLC\\Starter_Code\\PyBank\\Resources\\budget_data.csv')
output_file = Path('financial_analysis.txt')

# Initialize variables to hold data
list_Date = []
list_profit_loss = []
list_change_profit = []

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
        list_Date.append(date)
        list_profit_loss.append(profit_loss)

# Calculate statistics
total_months = len(list_Date)
net_total_profit_loss = sum(list_profit_loss)

# Calculate the change in profit/loss for each month
for i in range(1, len(list_profit_loss)):
    change = list_profit_loss[i] - list_profit_loss[i - 1]
    list_change_profit.append(change)

# Calculate the average change in profit/loss
average_change = round(sum(list_change_profit) / (total_months - 1), 2)

# Find the greatest increase and decrease in profits
max_increase = max(list_change_profit)
max_decrease = min(list_change_profit)

# Find the corresponding dates for the greatest increase and decrease
max_increase_date = list_Date[list_change_profit.index(max_increase) + 1]
max_decrease_date = list_Date[list_change_profit.index(max_decrease) + 1]

# Print the results
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_total_profit_loss}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})')
print(f'Greatest Decrease in Losses: {max_decrease_date} (${max_decrease})')

# Write the results to a new file
with open(output_file, 'w') as txtfile:
    txtfile.write('Financial Analysis\n')
    txtfile.write('----------------------------\n')
    txtfile.write(f'Total Months: {total_months}\n')
    txtfile.write(f'Total: ${net_total_profit_loss}\n')
    txtfile.write(f'Average Change: ${average_change}\n')
    txtfile.write(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})\n')
    txtfile.write(f'Greatest Decrease in Losses: {max_decrease_date} (${max_decrease})\n')

# Print message that results have been exported
print(f'Financial analysis results have been exported to {output_file}')







