from flask import Flask, url_for, request, redirect, abort, jsonify, session
app = Flask(__name__,
            static_url_path='', 
            static_folder='staticpages')
            
app.secret_key = 'SecretMachineL'

#index
@app.route('/')
def home():
    return app.send_static_file('index.html')
    
@app.route('/api/keras')
def keras():
    return {"value": kmodel()}
#curl http://127.0.0.1:5000

@app.route('/api/sklearn')
def sklearn():
    return {"value": skmodel()}

def kmodel():
    return 'Hello World!'

def skmodel():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)