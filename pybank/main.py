import os
import csv

# Set the path to the CSV file
csv_path = os.path.join("/Users", "peijuwu", "Desktop", "python-challenge", "PyBank", "Resources", "budget_data.csv")

# Open the CSV file
with open(csv_path, "r") as f:
    csv_reader = csv.reader(f)
    header= next(csv_reader)  # Store the header row
    
    total_months = 0
    total = 0
    pre_profit_loss = 0
    changes = []
    dates = []

    # Iterate over each line in the CSV file
    for line in csv_reader:
        total_months += 1 # Increment the total number of months
        total += int(line[1]) # Accumulate the total profit/loss
        dates.append(line[0]) # Collect the dates from each line

        # Calculate changes in profit/loss between months
        if pre_profit_loss != 0:
            current_profit_loss = int(line[1])
            change = current_profit_loss - pre_profit_loss
            changes.append(change)
        
        #Update the previous profit/loss value for the next iteration
        pre_profit_loss = int(line[1])

    # Calculate average change, maximum increase, and maximum decrease
    average_change = round(sum(changes) / len(changes), 2)
    max_increase = max(changes)
    max_increase_index = changes.index(max_increase)
    max_increase_date = dates[max_increase_index + 1]
    max_decrease = min(changes)
    max_decrease_index = changes.index(max_decrease)
    max_decrease_date = dates[max_decrease_index + 1]

    # Print the financial analysis results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {str(total_months)}")
    print(f"Total: ${str(total)}")
    print(f"Average Change: ${str(average_change)}")
    print(f"Greatest Increase in Profits: {str(max_increase_date)} (${str(max_increase)})")
    print(f"Greatest Decrease in Profits: {str(max_decrease_date)} (${str(max_decrease)})")

# Set the path for the output file
file_path = os.path.join("/Users", "peijuwu", "Desktop", "python-challenge", "PyBank", "analysis", "Financial_Analysis.txt")

# Write the financial analysis results to a text file
with open(file_path, "w") as new_f:
    new_f.write("Financial Analysis\n")
    new_f.write("---------------------------------\n")
    new_f.write(f"Total Months: {str(total_months)}\n")
    new_f.write(f"Total: ${str(total)}\n")
    new_f.write(f"Average Change: ${str(average_change)}\n")
    new_f.write(f"Greatest Increase in Profits: {str(max_increase_date)} (${str(max_increase)})\n")
    new_f.write(f"Greatest Decrease in Profits: {str(max_decrease_date)} (${str(max_decrease)})\n")
