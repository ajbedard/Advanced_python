import csv
from datetime import datetime


class StockPriceReader:
    def __init__(self, file_path, threshold):
        self.file = open(file_path, "r")
        self.reader = csv.reader(self.file)
        self.headers = next(self.reader)
        self.threshold = threshold

    def __iter__(self):
        return self

    def __next__(self):
        try:
            row = next(self.reader)
        except StopIteration:
            self.file.close()
            raise StopIteration

        stock_data = {header: value for header, value in zip(self.headers, row)}
        high_price = float(stock_data["high"])
        datetime_obj = datetime.strptime(stock_data["datetime"], "%Y-%m-%d %H:%M:%S")

        if high_price > self.threshold:
            return datetime_obj
        else:
            return self.__next__()


def get_dates_above_threshold(file_path, threshold):
    stock_price_reader = StockPriceReader(file_path, threshold)
    dates_above_threshold = []

    for date in stock_price_reader:
        dates_above_threshold.append(date)

    return dates_above_threshold


file_path = "data/iterators/dummy_stock_data.csv"
threshold = 1000
dates_above_threshold = get_dates_above_threshold(file_path, threshold)
print(dates_above_threshold)
