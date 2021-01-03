from flask import Flask, url_for, request, redirect, abort, jsonify, session

app = Flask(__name__, 
            static_url_path='', 
            static_folder='static-pages')


#index
@app.route('/')
def index():
    #return "hello"
    count=0
    count+=1

    if not 'counter' in session:
        session['counter'] =0
        print("new session")

    sessionCount=session['counter']
    sessionCount+=1
    session['counter']=sessionCount

    

    pageContent="<h1>counts</h1>" +\
        "session Count ="+str(sessionCount) +\
        "<br/>this Count ="+str(count)
    
    return pageContent
    
@app.route('/clear')
def clear():
    #session.clear()
    session.pop('counter',None)   

    return "done"
    
#curl http://127.0.0.1:5000