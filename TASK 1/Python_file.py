import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1. Load the Dataset
# Ensure 'churn-bigml-80.csv' is in your project folder
df = pd.read_csv('churn-bigml-80.csv')

# --- OBJECTIVE 1: PREPROCESSING ---
# The computer can't read "Yes/No" or "True/False", so we turn them into 1s and 0s
le = LabelEncoder()
df['International plan'] = le.fit_transform(df['International plan'])
df['Voice mail plan'] = le.fit_transform(df['Voice mail plan'])
df['Churn'] = le.fit_transform(df['Churn'])

# We drop 'State' because it's a name, not a number the model can calculate easily
X = df.drop(['State', 'Churn'], axis=1)
y = df['Churn']

# Feature Scaling: Making sure big numbers (like minutes) don't
# overpower small numbers (like calls)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into Training (80%) and Testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# --- OBJECTIVE 2 & 3: TRAIN & EVALUATE MULTIPLE MODELS ---
# We are hiring 3 different "Experts" to see who is best at predicting churn
models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(max_depth=5),
    "Random Forest": RandomForestClassifier(n_estimators=50, max_depth=5)
}

print("--- MODEL EVALUATION REPORT ---")
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"\nModel Expert: {name}")
    print(f"Accuracy Score: {accuracy_score(y_test, predictions):.2%}")
    # This shows Precision, Recall, and F1-Score as required by the task
    print(classification_report(y_test, predictions))

# --- OBJECTIVE 4: HYPERPARAMETER TUNING (Grid Search) ---
print("\n--- Running Grid Search to find the best settings... ---")
# We tell the computer to try different "recipes" for the Random Forest
param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [5, 10, None]
}
grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=3)
grid_search.fit(X_train, y_train)

print(f"Best Parameters Found: {grid_search.best_params_}")
final_pred = grid_search.predict(X_test)
print(f"Final Optimized Accuracy: {accuracy_score(y_test, final_pred):.2%}")