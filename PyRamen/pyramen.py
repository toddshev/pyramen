'''
PyRamen assignment:  
'''

#libraries and dependencies
from pathlib import Path
import csv

#input file paths
menu_file = Path("menu_data.csv")
sales_file = Path("sales_data.csv")

#initialize variables
menu = []
sales = []
quantity = 0
menu_item = ''
report = {}

# function to more easily check for keys
def check_key(keytocheck,dict):
    if keytocheck in dict.keys():
        return True
    else:
        return False
    
# open, read in menu_data using csvr
with open(menu_file,'r') as f_menu:
    csvreader = csv.reader(f_menu, delimiter = ',')
    next(csvreader)
    
    for row in csvreader:
        menu.append(row)

#open, read in sales_data using csvr
with open (sales_file,'r') as f_sales:
    csvreader = csv.reader(f_sales, delimiter = ',')
    next(csvreader)
    
    for row in csvreader:
        sales.append(row)

for row in sales:
    quantity = int(row[3])
    sales_item = row[4]
    
    if not check_key(sales_item,report):
        report[sales_item] = sales_item # add sales items as keys
        report[sales_item] = {
            "01-count":0,
            "02-revenue":0,
            "03-cogs":0,
            "04-profit":0
        }

    for menu_item in menu:
        item = menu_item[0]
        price = float(menu_item[3])
        cost = int(menu_item[4])
        profit = price - cost

        r = report[sales_item] # - just to make it easier to read
        if item == sales_item: # - add to the aggregate values
            r["01-count"] += quantity
            r["02-revenue"] += price * quantity
            r["03-cogs"] += cost * quantity
            r["04-profit"] += profit * quantity
            
print(report)
