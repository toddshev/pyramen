from pathlib import Path
import csv

pl_sum = 0
sum_diff = 0
avg_diff = 0
num_months = 0 
pl_maxdiff = 0
pl_mindiff = 0

print_list = []
records = []
header = []

file_in = Path("budget_data.csv")
file_out = "output.csv"

with open(file_in,'r') as f:
    csvreader = csv.reader(f,delimiter = ',')
    
    header = next(csvreader)
    
    for row in csvreader:
        dt = row[0]
        val = int(row[1])
        pl_sum += val
        records.append(row)

    num_months = len(records)
    
    i = 0
    for i in range(0,num_months):
        if (i != 0):
            diff = (int(records[i][1]) - int(records[i-1][1]))
            if diff > pl_maxdiff:
                pl_maxdiff = diff
                pl_maxmonth = records[i][0]
            
            if diff < pl_mindiff:
                pl_mindiff = diff
                pl_minmonth = records[i][0]
            
            sum_diff += diff
            records[i].append(int(diff))
    
    avg_diff = round(sum_diff/(num_months-1),2)


l1 = "Financial Summary"
l2 = "-----------------------------------"
l3 = "Total Months: " + str(num_months)
l4 = "Total: $" + str(pl_sum)
l5 = "Average Change: $" + str(round(avg_diff,2))
l6 = "Greatest Increase in Profits: " + pl_maxmonth + "  ($" + str(pl_maxdiff) + ")"
l7 = "Smallest Increase in Profits: " + pl_minmonth + "  ($" + str(pl_mindiff) + ")"

print_list = [l1,l2,l3,l4,l5,l6,l7]

for item in print_list:
    print(item)
    
with open(file_out,'w') as out:
    csvwriter = csv.writer(out,delimiter = ',')
    
    for item in print_list:
        csvwriter.writerow([item])