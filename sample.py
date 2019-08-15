import csv
filename = 'csv/sample.csv'

with open(filename) as csvfile:

    #reader = csv.reader(csvfile)
    reader = csv.DictReader(csvfile)

    keys = []
    values = []

    for row in reader:
        keys.append(row['surname'])
        values.append(row['age'])
    dd=dict(zip(keys,values))
    print(dd)
