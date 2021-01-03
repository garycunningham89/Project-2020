from flask import Flask

app = Flask(__name__)

# Create a new web app.
app = Flask(__name__)

# Add root route.
@app.route("/")
def home():
    return app.send_static_file('index.html')
    
#curl http://127.0.0.1:5000