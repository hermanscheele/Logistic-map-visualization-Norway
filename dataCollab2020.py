from MGdata2020 import ordreDict as postcode_orders
from excelReader import dictionary as kommune_postcodes




kommune_orders = {}



# Create a new dictionary to store the total orders per municipality
kommune_orders = {}

# Iterate over the postal code dictionary
for kommune, postcodes in kommune_postcodes.items():
    total_orders = 0

    # Sum up the orders for each postal code in the current municipality
    for postcode in postcodes:
        if postcode in postcode_orders:
            total_orders += postcode_orders[postcode]

    # Assign the total orders to the municipality in the new dictionary
    kommune_orders[kommune] = total_orders

# Print the resulting dictionary
# print(kommune_orders["ÅLESUND"])

