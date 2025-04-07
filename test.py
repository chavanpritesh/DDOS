import pandas as pd

# Load the Parquet file
df = pd.read_parquet(r'dataset\UDP-training.parquet')  # Use raw string for Windows paths

# Print the column names
print(df.columns.tolist())
