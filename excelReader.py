import pandas as pd

data = pd.read_excel('Postnummerregister-Excel.xlsx')

postnummer = data['Postnummer']
kommunenavn = data['Kommunenavn']

dictionary = {}


for i in range(len(postnummer)):
    kommunenavn_key = kommunenavn[i]

    # Add leading zeros to postnummer if necessary
    postnummer_value = str(postnummer[i]).zfill(4)

    if kommunenavn_key in dictionary:
        dictionary[kommunenavn_key].append(postnummer_value)
    else:
        dictionary[kommunenavn_key] = [postnummer_value]



# print(dictionary["HALDEN"])
