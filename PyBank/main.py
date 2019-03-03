import csv
import os

months = []
profits = []
output = []

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
avg_changes = round((profits[-1] - profits[0])/(tot_months - 1), 2)
max_increase = max(profits)
max_month = months[profits.index(max_increase)]
max_decrease = min(profits)
min_month = months[profits.index(max_decrease)]

# Create financial analysis
output.append("Financial analysis:")
output.append("----------------------")
output.append(f"Total months: {tot_months}")
output.append(f"Total: ${net_profit}")
output.append(f"Average Change: ${avg_changes}")
output.append(f"Greatest Increase in Profits: {max_month} (${max_increase})")
output.append(f"Greatest Decrease in Profits: {min_month} (${max_decrease})")

# Print analysis
for line in output:
    print(line)

# Write to file
with open("output.txt", 'w') as of:
    for line in output:
        of.write(line+"\n")