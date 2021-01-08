from flask import Flask, request, jsonify
from sklearn import model_selection
from kmodel import keral
from skmodel import skl
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
    
#@app.route('/api/keras')
#def keras(kmodel):
    #return {"value": kmodel()}
#curl http://127.0.0.1:5000/api/keras/16

@app.route('/predictk', methods=['POST'])
def kmodel():
    return keral
@app.route('/predictsk', methods=['POST'])
def skmodel():
    return skl

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)