import os
import csv

file_path = os.path.join("Resources","budget_data.csv")

with open(file_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    month_name = []
    profit_total = []
    change_total = []
    Total = 0
    count = 0
    for row in csvreader:
        month_name.append(row[0])
        profit_total.append(int(row[1]))
        Total = Total + int(row[1])
        count = count + 1
    
    change_total = [(profit_total[i+1]-profit_total[i]) for i in range(len(profit_total)-1)]
    max = 0
    max_name = ""
    min = 0
    min_name = ""
    j = 0
    while j < len(change_total):

        if max < change_total[j]:
            max = change_total[j]
            max_name = month_name[j+1]

        if change_total[j] < min:
            min = change_total[j]
            min_name = month_name[j+1]
        
        j += 1
        
    average = sum(change_total) / len(change_total)
    average_rounded = round(average, 2)


    print("Financial Analysis")
    print(30*"-")
    print(f"Total Months: {count}")
    print(f"Total: ${Total}")
    print(f"Average Change: {average_rounded}")
    print(f"Greatest Increase in Profits: {max_name} ({max})")
    print(f"Greatest Decrease in Profits: {min_name} ({min})")
        
with open (os.path.join("Analysis","output.txt"),"w") as output:
    output.write("Financial Analysis\n")
    output.write(30*"-")
    output.write(f"\nTotal Months: {count}\n")
    output.write(f"Average  Change: {average_rounded}\n")
    output.write(f"Greatest Increase in Profits: {max_name} ({max})\n")
    output.write(f"Greatest Decrease in Profits: {min_name} ({min})\n")


