# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

# Load the dataset provided by Power BI
dataset = dataset.dropna()  # Drop missing values

# Encode categorical features
label_encoders = {}
for column in ['Category', 'Region', 'Ship Mode']:
    le = LabelEncoder()
    dataset[column] = le.fit_transform(dataset[column])
    label_encoders[column] = le

# Define features (X) and target (y)
X = dataset[['Category', 'Region', 'Ship Mode']]  # Add other relevant columns
y = dataset['Sales']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Prepare data for visualization
output = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
output.reset_index(inplace=True)
