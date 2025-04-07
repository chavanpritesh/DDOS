import joblib
import pandas as pd

def detect_attack(packet_rate, src_ip_count, dst_port, protocol_str):
    # Load saved model and encoders
    model = joblib.load("models/ddos_model.pkl")
    protocol_encoder = joblib.load("models/protocol_encoder.pkl")

    # Encode protocol string (e.g., 'TCP', 'UDP')
    try:
        protocol = protocol_encoder.transform([protocol_str])[0]
    except ValueError:
        return "❌ Unknown Protocol!"

    # Create DataFrame for prediction
    input_data = pd.DataFrame([{
        "packet_rate": packet_rate,
        "src_ip_count": src_ip_count,
        "dst_port": dst_port,
        "protocol": protocol
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        return "✅ Normal Traffic"
    else:
        return "🚨 DDoS Attack Detected!"
