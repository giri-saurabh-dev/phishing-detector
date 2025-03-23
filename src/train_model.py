import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from feature_extraction import extract_features

# Load dataset (Assuming the dataset has two columns: 'url' and 'label' (1 for phishing, 0 for legitimate))
df = pd.read_csv("./data/urls.csv")

# Extract features
features = pd.DataFrame([extract_features(url) for url in df["URL"]])
features["label"] = df["label"]

# Split into training and testing sets
X = features.drop(columns=["label"])
y = features["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
with open("./models/phishing_detector.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model training complete!")
