# Import necessary libraries:
import numpy as np                          # For numerical operations.
from sklearn.datasets import load_iris       # To load the Iris dataset.
from sklearn.linear_model import LogisticRegression  # Our classifier.
from sklearn.model_selection import train_test_split  # For splitting data into training and test sets.
from sklearn.metrics import classification_report     # For evaluating our model.

# Load the Iris dataset.
iris = load_iris()  # The Iris dataset is a classic dataset with 150 samples of iris flowers.
X = iris.data       # Feature matrix: measurements like sepal length, sepal width, petal length, petal width.
y = iris.target     # Target vector: numerical labels representing the iris species.

# Split the data into training and testing subsets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# test_size=0.3 -- 30% of data is reserved for testing.
# random_state=42 ensures reproducibility of the split.

# Initialize the Logistic Regression classifier.
clf = LogisticRegression(max_iter=200)
# max_iter=200 sets the maximum number of iterations (to ensure convergence for this dataset).

# Train the classifier on the training data.
clf.fit(X_train, y_train)  # The model learns the mapping from features to iris species.

# Use the trained model to predict the test set labels.
y_pred = clf.predict(X_test)

# Print the classification report to evaluate performance.
print(classification_report(y_test, y_pred))