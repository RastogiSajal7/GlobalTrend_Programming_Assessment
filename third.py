import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

X, y = make_regression(n_samples=1000, n_features=1, noise=10, random_state=42)
X = pd.DataFrame(X, columns=['Feature'])
y = pd.Series(y, name='Target')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2) Score: {r2}")
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, alpha=0.7, edgecolors='b', s=100, label="Actual values")
plt.scatter(X_test, y_pred, alpha=0.7, edgecolors='r', s=100, label="Predicted values")
plt.plot(X_test, y_pred, color='red', lw=2, label="Regression Line")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.title("Actual vs Predicted Values")
plt.legend()
plt.show()
