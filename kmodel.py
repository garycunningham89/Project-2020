import pandas as pd
import numpy as np
import sklearn
import tensorflow
from tensorflow import keras as kr
from tensorflow.keras import layers
input_file = "powerproduction.csv"
df = pd.read_csv(input_file, header = 0)
original_headers = list(df.columns.values)
df = df._get_numeric_data()
numeric_headers = list(df.columns.values)
windspeed = df[["speed", "power"]].dropna()
x = windspeed["speed"].to_numpy()
x = x.reshape(-1, 1)


from sklearn.model_selection import train_test_split
X_train20, X_test20 = train_test_split(x, test_size=0.20)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
# fitting the 80% Training to the scaler.
scaler.fit(X_train20)
f = lambda x: 3.0 * x + 1.0
def predict(x):
    return f(x,p)
X_train = scaler.transform(X_train20)
X_test = scaler.transform(X_test20)
Y_train = f(X_train)
Y_test = f(X_test)

model = kr.models.Sequential()
model.add(kr.layers.Dense(1, input_shape=(1,), activation="linear", kernel_initializer='ones', bias_initializer='zeros'))
model.compile('adam', loss='mean_squared_error')
model.predict(X_train)

# Save yourlkl model
from sklearn import model_selection
import joblib
joblib.dump(predict, 'keralmodel.pkl')

# Load the model that you just saved
k = joblib.load('keralmodel.pkl')
kr = ("The Keras Model Prediction simulated at ", str(k).strip('<function predict at ').rstrip('>'))