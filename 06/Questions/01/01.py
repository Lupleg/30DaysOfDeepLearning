import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Decision Tree classifier with Gini impurity
clf_gini = DecisionTreeClassifier(criterion='gini', random_state=42)
clf_gini.fit(X_train, y_train)

# Train a Decision Tree classifier with Entropy
clf_entropy = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf_entropy.fit(X_train, y_train)

# Predict and evaluate the models
y_pred_gini = clf_gini.predict(X_test)
y_pred_entropy = clf_entropy.predict(X_test)

accuracy_gini = accuracy_score(y_test, y_pred_gini)
accuracy_entropy = accuracy_score(y_test, y_pred_entropy)

print(f"Accuracy with Gini impurity: {accuracy_gini}")
print(f"Accuracy with Entropy: {accuracy_entropy}")

# Visualize the decision trees
plt.figure(figsize=(20, 10))
plt.subplot(1, 2, 1)
plot_tree(clf_gini, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("Decision Tree with Gini Impurity")

plt.subplot(1, 2, 2)
plot_tree(clf_entropy, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("Decision Tree with Entropy")

plt.show()

# Addressing the potential drawbacks of a highly complex decision tree model
# Let's train a highly complex decision tree
clf_complex = DecisionTreeClassifier(criterion='gini', max_depth=None, random_state=42)
clf_complex.fit(X_train, y_train)

# Predict and evaluate the complex model
y_pred_complex = clf_complex.predict(X_test)
accuracy_complex = accuracy_score(y_test, y_pred_complex)

print(f"\nAccuracy with a highly complex decision tree: {accuracy_complex}")

# Now, let's prune the tree to avoid overfitting
clf_pruned = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
clf_pruned.fit(X_train, y_train)

# Predict and evaluate the pruned model
y_pred_pruned = clf_pruned.predict(X_test)
accuracy_pruned = accuracy_score(y_test, y_pred_pruned)

print(f"Accuracy with a pruned decision tree (max_depth=3): {accuracy_pruned}")

# Visualize the pruned decision tree
plt.figure(figsize=(10, 10))
plot_tree(clf_pruned, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("Pruned Decision Tree (max_depth=3)")
plt.show()