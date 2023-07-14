import pandas as pd
from sklearn import linear_model
from sklearn.datasets import fetch_california_housing
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Step 1: Fetch data
data, target =fetch_california_housing(as_frame=True,return_X_y=True)
data_ds = pd.DataFrame(data)[["AveRooms","AveBedrms"]]
target_ds = np.array(target)

# print(data.shape,target.shape)
# data=data.dropna()
# target=target.dropna()
# print(data.shape,target.shape)
# # data_ds=data_ds.isna().sum()

# # data_ds=data_ds.isna().sum()
# print(data_ds.shape)

#
#
# print(target)
# print("s")
# # print(data_ds)
# # print("s")
# print(target_ds)

# Step 2: Prepare data
X_train, X_test, y_train, y_test = train_test_split(data_ds, target, test_size=0.33)

# Step 3: Model
lasso=linear_model.LassoLars(alpha=.2)
lasso.fit(X_train, y_train)
print("Lasso Score:", lasso.score(X_train,y_train))
# print("R2 Score:", r2_score(X_train, y_train))

# Step 4: Predict
y_pred = lasso.predict(X_test)
# print(y_pred)
print("R2 Score:", r2_score(y_test, y_pred))