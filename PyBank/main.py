
# PyBank

import os
import csv
import sys # to export print

file_path = os.path.join("Resources", "budget_data.csv")

lot = []
total = []
change = 0
previous_budget = 0
change_total = 0
change_count = 0
greatest_increase = 0
greatest_decrease = 0

with open(file_path, newline='') as csvfile:    #to populate months and total
    reader = csv.reader(csvfile, delimiter=",")
    next(reader, None) # skip header

    for row in reader:

        lot.append(row) # append to get total

        convert = int(row[1])
        total.append(convert)

        current_budget = int(row[1])
        
        if previous_budget != 0: # to get change
            change = current_budget - previous_budget
            change_total += change
            change_count += 1
            
        previous_budget = current_budget

        if change > greatest_increase: # to get greatest increase and decrease
            greatest_increase = change
            i_date = row[0]
        if change < greatest_decrease:
            greatest_decrease = change
            d_date = row[0]


change_avg = round(change_total/change_count, 2) # change average

print("")
print("Financial Analysis")
print("-----------------------------------------")
print(f"Total Months: {len(lot)}")   # print to terminal
print(f"Total: ${sum(total)}")
print(f"Average  Change: ${(change_avg)}")
print(f"Greatest Increase in Profits: {i_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {d_date} (${greatest_decrease})")

original_stdout = sys.stdout

with open("Analysis/PyBank_final.txt", "w") as f:    #export to .txt file
    sys.stdout = f
    print("")
    print("Financial Analysis")
    print("-----------------------------------------")
    print(f"Total Months: {len(lot)}")
    print(f"Total: ${sum(total)}")
    print(f"Average  Change: ${(change_avg)}")
    print(f"Greatest Increase in Profits: {i_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {d_date} (${greatest_decrease})")
    sys.stdout = original_stdout

