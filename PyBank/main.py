# Import the pathlib and csv library
import csv
from pathlib import Path


# Set the file path
csvpath = Path('Resources/budget_data.csv')
file_to_load = Path("Resources/budget_data.csv")
file_to_output = Path("analysis/budget_analysis.txt")

# Initialize variable to answer questions
list_date = []
total_months = 0
list_profit_loss = []
list_change_profit = []
max_increase = ["",0]
max_decrease = ["",999999999999]
max_decrease_date =[]
max_increase_date =[]
total_net = 0


# Open the input path as a file object
with open(csvpath) as csvfile:
   


    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')


    # Go to the next row from the start of the file
    # (which is often the first row/header) and iterate line_num by 1
    header = next(csvreader)
  


    # Read each row of data after the header
    for row in csvreader:
    
        # Set salary variable equal to the value in the 4th column of each row
        dates1 = str(row[0])
        # Append the row salary value to the list of salaries
        list_date.append(dates1)
        profit_loss1 = int(row[1])
        list_profit_loss.append(profit_loss1)
       
       
        
    print(list_date)
    print(list_profit_loss)



print('toal sum of profit')
print(sum(list_profit_loss))
print('total months')
print(len(list_date))


# Find the greatest increase and decrease in profits
print('GREATEST INCREASE IN PROFITS')
print(max(list_profit_loss))
print('greatest decrease in profits')
print(min(list_profit_loss))

# Find the corresponding dates for the greatest increase and decrease
max_increase_date = list_date[list_change_profit.index(max_increase) + 1]
max_decrease_date = list_date[list_change_profit.index(max_decrease) + 1]


# Create a dictionary from the two lists
result = dict(zip(list_date, list_profit_loss))

# Print the dictionary
print(result)



list_change_profit = []

for i in range(1, len(list_profit_loss)):
    change = list_profit_loss[i] - list_profit_loss[i - 1]
    list_change_profit.append(change)  

print(list_change_profit)

total = sum(list_change_profit)

bottom = len(list_profit_loss)
# Step 3: Divide the sum by the number of elements in the list to find the average
average = total / bottom

# Step 4: Print the average
print("The average is:", average)

