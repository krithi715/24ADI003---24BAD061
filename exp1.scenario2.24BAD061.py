import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes.csv")

print(df.info())
print(df.isnull().sum())

df["Glucose"].hist()
plt.title("Glucose Distribution")
plt.show()

df["Age"].hist()
plt.title("Age Distribution")
plt.show()

df[["Glucose", "BMI"]].boxplot()
plt.show()
