import openpyxl
from dataCollab import kommune_orders

# Create a new workbook
workbook = openpyxl.Workbook()

# Select the active sheet (first sheet by default)
sheet = workbook.active

sheet.append(['navn', 'ordre'])

for kommune, ordre in kommune_orders.items():

    sheet.append([kommune, ordre])

# # Save the workbook
workbook.save("kommune_ordre.xlsx")
