
#PyPoll

import os
import csv
import sys # to export print

file_path = os.path.join("Resources", "election_data.csv")

votes_lot = []
Khan = []
Correy = []
Li = []
OTooley = []

with open(file_path, newline='') as csvfile:    #to populate months and total
    reader = csv.reader(csvfile, delimiter=",")
    next(reader, None) # skip header

    for row in reader:

        votes_lot.append(row)
        
        # count votes for each candidate and append
        if row[2] == "Khan":
            Khan.append(row[2])
        elif row[2] == "Correy":
            Correy.append(row[2])
        elif row[2] == "Li":
            Li.append(row[2])
        else:
            row[2] == "O'Toolet"
            OTooley.append(row[2])
    
# calculate percentages

percent_k = round(int(len(Khan))/int(len(votes_lot))*100, 2)
percent_c = round(int(len(Correy))/int(len(votes_lot))*100, 2)
percent_l = round(int(len(Li))/int(len(votes_lot))*100, 2)
percent_o = round(int(len(OTooley))/int(len(votes_lot))*100, 2)

# compare percent from each candidate and get a winner

all_percents = [percent_k, percent_c, percent_l, percent_o]
most_votes = max(all_percents)

if most_votes == percent_k:
    winner = "Khan"
elif most_votes == percent_c:
    winner = "Correy"
elif most_votes == percent_l:
    winner = "Li"
else:
    winner = "O'Tooley"

# print all
print("")
print("Election Results")
print("---------------------------")
print(f"Total Votes: {len(votes_lot)}")
print("---------------------------")
print(f"Khan: {percent_k}% ({len(Khan)})")
print(f"Correy: {percent_c}% ({len(Correy)})")
print(f"Li: {percent_l}% ({len(Li)})")
print(f"OTooley: {percent_o}% ({len(OTooley)})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

original_stdout = sys.stdout

with open("Analysis/PyPoll_final.txt", "w") as f:    #export to .txt file
    sys.stdout = f
    print("")
    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {len(votes_lot)}")
    print("---------------------------")
    print(f"Khan: {percent_k}% ({len(Khan)})")
    print(f"Correy: {percent_c}% ({len(Correy)})")
    print(f"Li: {percent_l}% ({len(Li)})")
    print(f"OTooley: {percent_o}% ({len(OTooley)})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")
    sys.stdout = original_stdout
