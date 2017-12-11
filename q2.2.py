from flask import Flask,jsonify,request,render_template
import requests
import simplejson 
import json

app = Flask(__name__,template_folder='Templates')

@app.route("/posts")
def home():
    uri = "https://jsonplaceholder.typicode.com/posts"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    return render_template('posts.html',posts=data)
    
if __name__ == "__main__":
    app.run(debug = True)
