import pandas as pd
import numpy as np
import sklearn

# Load the dataset in a dataframe object and include only four features as mentioned
input_file = "powerproduction.csv"
df = pd.read_csv(input_file, header = 0)
original_headers = list(df.columns.values)
df = df._get_numeric_data()

numeric_headers = list(df.columns.values)

# Logistic Regression classifier
import sklearn.linear_model as lin
def f(x, p):
    return p[0] + x * p[1]
windspeed = df[["speed", "power"]].dropna()
x = windspeed["speed"].to_numpy()
y = windspeed["power"].to_numpy()

x = x.reshape(-1, 1)

model = lin.LinearRegression()
model.fit(x, y)

p = [model.intercept_, model.coef_[0]]
def predict(x):
    return f(x,p)
# Save your model
from sklearn import model_selection
import joblib
joblib.dump(predict, 'model.pkl')
# Load the model that you just saved
s = joblib.load('model.pkl')
skl = ("The Scikit Learn Model Prediction simulated at ", str(s).strip('<function predict at ').rstrip('>'))