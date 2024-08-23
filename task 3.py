import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import tree
import seaborn as sns

# Upload the file
# Load the dataset from your local file system
file_path = 'heart-disease.csv'  # Update this path to where your CSV file is located
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(df.head())

# Splitting data into features and target variable
X = df.iloc[:, :-1].values  # Assuming the last column is the target
y = df.iloc[:, -1].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Visualize the Decision Tree
plt.figure(figsize=(30, 25))
tree.plot_tree(model, filled=True, feature_names=df.columns[:-1], class_names=['0', '1'])
plt.show()

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
print("Classification Report:\n", classification_report(y_test, predictions))
print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))
print("Accuracy Score:", accuracy_score(y_test, predictions))
