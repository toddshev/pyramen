from pathlib import Path
import csv

#initialize variables
pl_sum = 0 # sum of profit/loss
sum_diff = 0 #sum of change
avg_diff = 0 # average of change
num_months = 0 # month count
pl_maxdiff = 0 #max value of change
pl_maxmonth = '' #month associated with maxdiff
pl_mindiff = 0 # min value of change
pl_minmonth = '' #month associated with mindiff
print_list = [] #list of items to print, for convenience
records = [] #list to capture incoming data
header = [] #header for incoming/outgoing data

file_in = Path("budget_data.csv")  #input path
file_out = "output.csv"  #output file name

with open(file_in,'r') as f:  #read in file
    csvreader = csv.reader(f,delimiter = ',')
    
    header = next(csvreader)
    
    for row in csvreader:
        dt = row[0]
        val = int(row[1])
        pl_sum += val
        records.append(row)

    num_months = len(records)  #get total record count after loop completes
    
    i = 0  #iterator to use in change calc
    for i in range(0,num_months):
        if (i != 0): #skip first row since change is N/A
            diff = (int(records[i][1]) - int(records[i-1][1]))
            if diff > pl_maxdiff:  #get max d
                pl_maxdiff = diff
                pl_maxmonth = records[i][0]
            
            if diff < pl_mindiff:
                pl_mindiff = diff
                pl_minmonth = records[i][0]
            
            sum_diff += diff
            records[i].append(int(diff))
    
    avg_diff = round(sum_diff/(num_months-1),2)



L1 = "Financial Summary"
L2 = "-----------------------------------"
L3 = "Total Months: " + str(num_months)
L4 = "Total: $" + str(pl_sum)
L5 = "Average Change: $" + str(round(avg_diff,2))
L6 = "Greatest Increase in Profits: " + pl_maxmonth + "  ($" + str(pl_maxdiff) + ")"
L7 = "Smallest Increase in Profits: " + pl_minmonth + "  ($" + str(pl_mindiff) + ")"

print_list = [L1,L2,L3,L4,L5,L6,L7]

for item in print_list:
    print(item)
    
with open(file_out,'w') as out:
    csvwriter = csv.writer(out,delimiter = ',')
    
    for item in print_list:
        csvwriter.writerow([item])    
    
    for item in print_list:
        csvwriter.writerow([item])