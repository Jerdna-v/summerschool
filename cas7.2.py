import pandas as pd
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# # Step 1: Get data
iris = load_iris()
# print(type(iris))
X = iris.data
y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names
print(feature_names)
print(target_names)
# df = pd.DataFrame(X)
# print(df)
# print("Feature names:", feature_names)
# print("Target names:", target_names)
# print("\nFirst 10 rows of X:\n", X[:10])

# # Step 2: Prepare data
X_train, X_test, y_train, y_test = train_test_split(
   X, y, test_size=0.33, random_state=42
)

#
# # Step 3: Build the model
classifier_knn = KNeighborsClassifier(n_neighbors=3)
decision_tree = DecisionTreeClassifier()

# # Step 4: Test the model
classifier_knn.fit(X_train, y_train)

decision_tree.fit(X_train, y_train)

y_pred_knn = classifier_knn.predict(X_test)

y_pred_tree = decision_tree.predict(X_test)
print(y_pred_knn)

print(y_pred_tree)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred_knn))
print("Accuracy:", metrics.accuracy_score(y_test, y_pred_tree))

# # Step 5: New data
sample = [[5, 5, 3, 2], [2, 4, 3, 5]]
preds = classifier_knn.predict(sample)
print(preds)
pred_species = [iris.target_names[p] for p in preds]
print("Predictions:", pred_species)