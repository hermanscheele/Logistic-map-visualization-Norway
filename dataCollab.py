from MGdata import ordreDict as postcode_orders
from excelReader import dictionary as kommune_postcodes
from readFraktData import fraktDict



kommune_orders = {}



# Create a new dictionary to store the total orders per municipality
kommune_orders = {}
kommune_frakt = {}

# Iterate over the postal code dictionary
for kommune, postcodes in kommune_postcodes.items():
    total_orders = 0
    total_frakt = 0

    # Sum up the orders for each postal code in the current municipality
    for postcode in postcodes:
        if postcode in postcode_orders:
            total_orders += postcode_orders[postcode]
            total_frakt += fraktDict[postcode]
    


    if (total_orders != 0):

        snitt_frakt = total_frakt//total_orders
        kommune_frakt[kommune] = snitt_frakt

    elif total_orders == 0:
        kommune_frakt[kommune] = 0

    
    # Assign the total orders to the municipality in the new dictionary
    kommune_orders[kommune] = total_orders

# Print the resulting dictionary
# print(kommune_orders["TRONDHEIM"])
# print(kommune_frakt['OSLO'])

# print(kommune_frakt)


max_value = max(kommune_frakt.values())
max_key = max(kommune_frakt, key=kommune_frakt.get)

# print("Høyest snitt-frakt:", max_value)
# print("Kommune: ", max_key)

# print(kommune_frakt['BØ'])
