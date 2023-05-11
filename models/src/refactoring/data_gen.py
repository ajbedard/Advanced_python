import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(0)

# Generate a DataFrame with 1000 rows and three columns
data = pd.DataFrame({
    'Age': np.random.randint(18, 65, 1000),  # Age between 18 and 65
    'Income': np.random.randint(30000, 120000, 1000),  # Income between 30,000 and 120,000
    'Spending': np.random.randint(1000, 50000, 1000)  # Spending between 1,000 and 50,000
})

# Save the DataFrame to a CSV file
data.to_csv('../../../data/refactoring/dummy_data.csv', index=False)
