
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump

# Load training data
df = pd.read_csv('ML/training_data.csv')

# Split into features and labels
X = df[['slack', 'violations', 'area']]
y = df['class']

# Split into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save model
dump(clf, 'ML/model.pkl')

print("Done: model retrained and saved as model.pkl")
