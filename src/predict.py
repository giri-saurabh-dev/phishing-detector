import pickle
import pandas as pd
from feature_extraction import extract_features

# Load trained model
with open("./models/phishing_detector.pkl", "rb") as file:
    model = pickle.load(file)

def predict_url(url):
    """Predicts if a URL is phishing or legitimate."""
    features = pd.DataFrame([extract_features(url)])
    prediction = model.predict(features)
    return "Phishing" if prediction[0] == 1 else "Legitimate"

if __name__ == "__main__":
    test_url = input("Enter a URL to check: ")
    print(f"The URL is: {predict_url(test_url)}")
