import csv

gas = []

with open('cost_distribution.csv') as data:
    reader = csv.DictReader(data)
    for row in reader:
        gas.append(row['Gas'].strip('$'))
        
print(gas)
