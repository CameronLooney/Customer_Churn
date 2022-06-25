from transform_data import import_data, missing_values


data = import_data("/Users/cameronlooney/Documents/IBM-Telco.csv")
missing = missing_values(data)
print(missing)