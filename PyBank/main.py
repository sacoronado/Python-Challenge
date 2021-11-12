import os
import csv

path = "PyBank/Resources/budget_data.csv"

with open(path) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    data = []
    for row in csvreader:
        data.append(row)

    print(data)

    months = len(data)
    print(months)

    pandl = []
    for row in data:
        pandl.append(int(row[1]))
    total_pandl = sum(pandl)
    print(total_pandl)

    changes = []
    for i in range(1, len(pandl)):
        value = pandl[i]
        prev_value = pandl[i - 1]
        change = value - prev_value
        changes.append(change)
    print(changes)

    avg_change = sum(changes)/len(changes)
    print(avg_change)

    max_change = max(changes)
    print(max_change)
    max_index = changes.index(max_change)
    max_month = data[max_index + 1][0]
    print(max_month)

    min_change = min(changes)
    print(min_change)
    min_index = changes.index(min_change)
    min_month = data[min_index + 1] [0]
    print(min_month)

    print("--------------------------")
    print(f"Total months: {months}")
    print(f"Total profit/loss: ${round(total_pandl, 2)}")
    print(f"Average change: ${round(avg_change, 2)}")
    print(f"Greatest increse: {max_month} (${max_change})")
    print(f"Greatest loss: {min_month} (${min_change})")