import csv
import random
from datetime import datetime, timedelta

def random_walk(start, step, min_value, max_value):
    current_value = start
    while True:
        current_value += random.uniform(-step, step)
        current_value = max(min(current_value, max_value), min_value)
        yield current_value

def generate_stock_data(num_days, start_date, output_file):
    open_walk = random_walk(500, 10, 0, 1100)
    close_walk = random_walk(500, 10, 0, 1100)
    volume_walk = random_walk(1000, 100, 0, 5000)

    with open(output_file, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["high", "low", "open", "close", "volume", "datetime"])

        current_date = start_date
        for _ in range(num_days):
            open_price = next(open_walk)
            close_price = next(close_walk)
            high_price = max(open_price, close_price)

            # Introduce occasional artifacts with high prices in the range 1000-1100
            if random.random() < 0.01:
                high_price = random.uniform(1000, 1100)

            low_price = min(open_price, close_price)
            volume = int(next(volume_walk))
            date_str = current_date.strftime("%Y-%m-%d %H:%M:%S")

            csv_writer.writerow([high_price, low_price, open_price, close_price, volume, date_str])

            current_date += timedelta(days=1)

start_date = datetime(2020, 1, 1)
output_file = "\\data\\iterators\\dummy_stock_data.csv"
num_days = 365 * 3  # 3 years of daily data
generate_stock_data(num_days, start_date, output_file)
