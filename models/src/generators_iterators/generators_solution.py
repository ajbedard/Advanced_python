import csv


def dates_above_threshold_gen(file_path, threshold):
    # Open the CSV file and create a reader object
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        # Iterate through the CSV rows
        for row in reader:
            # Check if the 'high' value is above the threshold
            if float(row['high']) > threshold:
                # If the condition is met, yield the 'datetime' value for that row
                yield row['datetime']


file_path = "../data/iterators/dummy_stock_data.csv"
threshold = 1000

for date in dates_above_threshold_gen(file_path, threshold):
    print(date)