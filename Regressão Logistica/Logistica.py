import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

arquivo_csv = "auto-mpg.csv"
df = pd.read_csv(arquivo_csv)

df.replace('?', np.nan, inplace=True)

df = df.apply(pd.to_numeric, errors='coerce')

df.dropna(inplace=True)

df['high_mpg'] = np.where(df['mpg'] > 20, 1, 0)

X = df[["cylinders", "displacement", "horsepower", "weight", "acceleration"]]
y = df["high_mpg"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy * 100:.2f}%")

cm = confusion_matrix(y_test, y_pred)
print("Matriz de Confusão:")
print(cm)

plt.scatter(y_test, y_pred)
plt.xlabel("Valores Reais")
plt.ylabel("Valores Preditos")
plt.title("Regressão Logística: Real vs Predito")
plt.show()
