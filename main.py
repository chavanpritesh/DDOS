from utils.preprocessing import load_and_preprocess_data

X, y, protocol_enc, label_enc = load_and_preprocess_data("dataset/sample_ddos.csv")

print("Sample features:\n", X.head())
print("Sample labels:\n", y.head())
