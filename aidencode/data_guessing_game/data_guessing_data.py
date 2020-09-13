import csv

with open('resources/data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("Column names are {", row,"}")
            line_count += 1
        else:
            print("Row[",line_count,"] has the value:",row)
        line_count += 1

    print('Processed {line_count} lines.')