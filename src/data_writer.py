import csv
from config import OUTPUT_FILE, CSV_HEADERS

def write_pizza_data(filename, data):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(CSV_HEADERS)
        writer.writerows(data)