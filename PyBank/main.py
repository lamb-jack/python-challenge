
# PyBank

import os
import csv
import statistics # to get mean
import sys # to export print

file_path = os.path.join("..", "Resources", "budget_data.csv")

lot = []
total = []
change = []

with open(file_path, newline='') as csvfile:    #to populate months and total
    reader = csv.reader(csvfile, delimiter=",")
    next(reader, None) # skip header

    for row in reader:
        lot.append(row)

        convert = int(row[1])
        total.append(convert)


highest = max(total)
lowest = min(total)

index_h = int(total.index(highest))
index_l = int(total.index(lowest))

top = []
bottom = []

with open(file_path, newline='') as csvfile:    # to populate increase and decrease
    reader = csv.reader(csvfile, delimiter=",")
    next(reader, None)
    for i, row in enumerate(reader):
        if i == index_h:
            top.extend(row)
        elif i == index_l:
            bottom.extend(row)
            break

Increase = " ($".join(top)
Decrease = " ($".join(bottom)

print("Financial Analysis")
print("-----------------------------------------")
print(f"Total lot: {len(lot)}")   # print to terminal
print(f"Total: ${sum(total)}")
print(f"Average  Change: ${(change)}")
print(f"Greatest Increase in Profits: {Increase})")
print(f"Greatest Decrease in Profits: {Decrease})")


original_stdout = sys.stdout

with open("../Analysis/PyBank_final.txt", "w") as f:    #export to .txt file
    sys.stdout = f
    print("Financial Analysis")
    print("-----------------------------------------")
    print(f"Total lot: {len(lot)}")
    print(f"Total: ${sum(total)}")
    print(f"Average  Change: ${(change)}")
    print(f"Greatest Increase in Profits: {Increase})")
    print(f"Greatest Decrease in Profits: {Decrease})")
    sys.stdout = original_stdout

