'''
PyRamen Assignment: Gather sales and menu data to determine volume and profitability metrics
'''
#Imports
from pathlib import Path
import csv

menu_file = Path("menu_data.csv")
sales_file = Path("sales_data.csv")

#initialize variables
menu = [] #read in menu data to list
sales = [] #read in sales data to list
quantity = 0 #number sold
menu_item = '' #name of item sold from menu file
sales_item = ''#name of item sold from sales file
report = {} #dictionary of aggregated totals

#fuction to see if key already exists
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
    
    #if key doesn't exist, add it as key and new dict item
    if not check_key(sales_item,report): 
        report[sales_item] = sales_item
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
        
        r = report[sales_item] #to shorten code
        if item == sales_item: #aggregate and calc values at item level
            r["01-count"] += quantity
            r["02-revenue"] += price * quantity
            r["03-cogs"] += cost * quantity
            r["04-profit"] += profit * quantity
print(report)
