# California Housing Price Prediction

This Python code uses the LassoLars regression model to predict housing prices in California based on the average number of rooms and bedrooms in a house.
The California housing dataset is used for training and testing the model.

## Prerequisites

Make sure you have the following dependencies installed:

- pandas
- scikit-learn

You can install them using pip:

```
pip install pandas scikit-learn
```

## Usage

1. Import the required libraries:

```python
import pandas as pd
from sklearn import linear_model
from sklearn.datasets import fetch_california_housing
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
```

2. Fetch the California housing dataset and select the relevant features:

```python
data, target = fetch_california_housing(as_frame=True, return_X_y=True)
data_ds = pd.DataFrame(data)[["AveRooms", "AveBedrms"]]
target_ds = np.array(target)
```

3. Split the data into training and testing sets:

```python
X_train, X_test, y_train, y_test = train_test_split(data_ds, target, test_size=0.33)
```

4. Build the LassoLars regression model:

```python
laso = linear_model.LassoLars(alpha=0.2)
laso.fit(X_train, y_train)
```

5. Evaluate the model's performance:

```python
print("Training Score:", laso.score(X_train, y_train))

y_pred = laso.predict(X_test)
print("Predicted Values:", y_pred)
print("Testing Score:", r2_score(y_test, y_pred))
```

The `score` method calculates the coefficient of determination (R^2) on the training set, which indicates the proportion of variance in the target variable explained by the model. The `predict` method is used to make predictions on the testing set, and `r2_score` is used to evaluate the model's performance on the testing set.

Feel free to adjust the parameters, such as the test size or the LassoLars alpha value, to experiment with different settings and improve the model's performance.

---

Please note that the README assumes familiarity with Python and the mentioned libraries. It provides a brief overview of the code's functionality and usage. You may consider adding more details or instructions depending on the intended audience or specific project requirements.