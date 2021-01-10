from flask import Flask, request, jsonify
import traceback

def skmodel():
    return skl

app = Flask(__name__,
            static_url_path='', 
            static_folder='staticpages')
            
app.secret_key = 'SecretMachineL'



#index
@app.route('/')
def home():
    return app.send_static_file('index.html')
    
@app.route('/api/keras', methods = ['POST'])
def keras():
    from kmodel import kr
    return {"Model Prediction: ": kr}

@app.route('/api/sklearn', methods = ['POST'])
def sklearn():
    from skmodel import skl
    return {"Model Prediction: ": skl}

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)