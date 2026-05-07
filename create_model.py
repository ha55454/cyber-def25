from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

# Dummy training data
X = pd.DataFrame({
    'feature1': [10, 20, 30, 40],
    'feature2': [1, 0, 1, 0]
})

y = [0, 1, 0, 1]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, 'model.pkl')

print("model.pkl created successfully")
