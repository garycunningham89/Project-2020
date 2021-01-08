from flask import Flask, request, jsonify
from sklearn import model_selection
import joblib
import traceback
import pandas as pd
import numpy as np

app = Flask(__name__,
            static_url_path='', 
            static_folder='staticpages')
            
app.secret_key = 'SecretMachineL'

#index
@app.route('/')
def home():
    return app.send_static_file('index.html')
    
@app.route('/api/keras')
def keras(kmodel):
    return {"value": kmodel()}
#curl http://127.0.0.1:5000/api/keras/16

@app.route('/api/sklearn')
def sklearn(skmodel):
    return {"value": skmodel()}
@app.route('/predictk', methods=['POST'])
def kmodel(x):
    lr = joblib.load('model.pkl') 
    if lr:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(lr.predict(query))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')
@app.route('/predictsk', methods=['POST'])
def skmodel():
    lr = joblib.load('model.pkl') 
    if lr:
            try:
                json_ = request.json
                print(json_)
                query = pd.get_dummies(pd.DataFrame(json_))
                query = query.reindex(columns=model_columns, fill_value=0)

                prediction = list(lr.predict(query))

                return jsonify({'prediction': str(prediction)})

            except:

                return jsonify({'trace': traceback.format_exc()})
            else:
                print ('Train the model first')
                return ('No model here to use')

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)