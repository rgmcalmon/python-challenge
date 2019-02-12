import csv
import os

csv_path = os.path.join("Resources","election_data.csv")

# Load information on votes and candidates from file
votes = {}
with open(csv_path,newline='') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    next(csv_reader)
    
    for row in csv_reader:
        cand = row[2]
        if not (cand in votes):
            votes[cand] = 0
        votes[cand] += 1

total = sum(votes.values())

output = ["Election Results",
         '-'*30,
         f"Total Votes: {total}",
         "-"*30]
# Iterate over candidate, vote-count pairs
for c,v in votes.items():
    perc = round(v*100/total,3)
    output.append(f"{c}: {perc}% ({v})")

output.append("-"*30)
winner = max(votes,key=votes.get)
output.append(f"Winner: {winner}")
output.append("-"*30)

# Output analysis
for o in output:
    print(o)

# Write analysis to file
with open("output.txt",'w') as of:
    for o in output:
        of.write(o+"\n")