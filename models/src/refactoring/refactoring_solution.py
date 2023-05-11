import pandas as pd

class DataAnalyzer:
    def __init__(self, data, selected_columns):
        self.data = data[selected_columns]

    def calculate_correlation(self):
        return self.data.corr()

    def calculate_covariance(self):
        return self.data.cov()

# Load your data
data = pd.read_csv('../../../data/refactoring/dummy_data.csv')

# Select the columns to calculate the correlation and covariance matrices
selected_columns = ['Age', 'Income', 'Spending']

# Create an instance of the DataAnalyzer class
analyzer = DataAnalyzer(data, selected_columns)

# Call the functions
correlation_matrix = analyzer.calculate_correlation()
covariance_matrix = analyzer.calculate_covariance()

print("Correlation Matrix:")
print(correlation_matrix)
print("\nCovariance Matrix:")
print(covariance_matrix)
