from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from preprocessing import load_and_preprocess_data

def train_and_save_model():
    # Load and preprocess data
    X, y, protocol_enc, label_enc = load_and_preprocess_data("dataset/sample_ddos.csv")

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Decision Tree
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {acc * 100:.2f}%")

    # Save model and encoders
    joblib.dump(model, "models/ddos_model.pkl")
    joblib.dump(protocol_enc, "models/protocol_encoder.pkl")
    joblib.dump(label_enc, "models/label_encoder.pkl")
    print("Model and encoders saved in 'models/'")

if __name__ == "__main__":
    train_and_save_model()

