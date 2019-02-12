import csv
import os

months = []
profits = []

# Read in csv file
csv_path = os.path.join("Resources","budget_data.csv")

with open(csv_path,newline='') as csv_file:
    csvreader = csv.reader(csv_file,delimiter=',')

    next(csvreader)

    for row in csvreader:
        # Add profits from the month
        months.append(row[0])
        profits.append(int(row[1]))

# Financial analysis
# Total months
tot_months = len(profits)
net_profit = sum(profits)
avg_changes = round(net_profit / tot_months, 2)
max_increase = max(profits)
max_month = months[profits.index(max_increase)]
max_decrease = min(profits)
min_month = months[profits.index(max_decrease)]

# Give financial analysis
print("Financial analysis:")
print("----------------------")
print(f"Total months: {tot_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${avg_changes}")
print(f"Greatest Increase in Profits: {max_month} (${max_increase})")
print(f"Greatest Decrease in Profits: {min_month} (${max_decrease})")