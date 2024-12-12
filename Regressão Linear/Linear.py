import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

arquivo_csv = "auto-mpg.csv" 
df = pd.read_csv(arquivo_csv)

df.replace('?', np.nan, inplace=True)

df = df.apply(pd.to_numeric, errors='coerce')

df.dropna(inplace=True)

X = df[["cylinders", "displacement", "horsepower", "weight", "acceleration"]]
y = df["mpg"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Erro quadrático médio (MSE): {mse}")

plt.scatter(y_test, y_pred)
plt.xlabel("Valores Reais")
plt.ylabel("Valores Preditos")
plt.title("Regressão Linear: Real vs Predito")
plt.show()