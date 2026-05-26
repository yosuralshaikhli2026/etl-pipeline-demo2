import csv

def extract_data(path="data/input.csv"):
    row = []
    with open(payh, newline="") as f:
        reader= csv.dictreader(f)
        for row in reader:
            rows.append(row)
    return rows        