import pandas as pd

def load_and_preprocess_data(filepath=r'dataset\UDP-training.parquet'):

    # Read parquet file
    df = pd.read_parquet(filepath)

    # Print columns to check structure (remove after testing)
    print("Columns:", df.columns.tolist())

    # Drop NaN values if needed
    df = df.dropna()

    # Optional: Select only a few useful columns
    df = df[[
        'Flow Duration', 'Tot Fwd Pkts', 'Tot Bwd Pkts', 'Protocol', 'Label'
    ]]

    # Rename to match your model input
    df = df.rename(columns={
        'Flow Duration': 'packet_rate',
        'Tot Fwd Pkts': 'src_ip_count',
        'Tot Bwd Pkts': 'dst_port',
        'Protocol': 'protocol',
        'Label': 'result'
    })

    # Convert label to 'DDoS Attack 🚨' or 'Normal ✅'
    df['result'] = df['result'].apply(lambda x: 'DDoS Attack 🚨' if 'DDoS' in x else 'Normal ✅')

    return df
