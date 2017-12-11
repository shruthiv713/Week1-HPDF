from flask import Flask,jsonify,request,render_template
import requests
import simplejson 
import json

app = Flask(__name__,template_folder='Templates')

@app.route("/count")
def home():
    ur1 = "https://jsonplaceholder.typicode.com/users"
    ur2="https://jsonplaceholder.typicode.com/posts"
    try:
        uRes1 = requests.get(ur1)
	uRes2 = requests.get(ur2)
    except requests.ConnectionError:
       return "Connection Error"  
    Jres1 = uRes1.text
    data1 = json.loads(Jres1)
    Jres2 = uRes2.text
    data2 = json.loads(Jres2)
    carr=[]
    for a in data1:
	ct=0
	d={}
	for p in data2:
		if a['id']==p['userId']:
			ct=ct+1
	d['Name']=a['name']
	d['Count']=ct
	carr.append(d)
    return render_template('count.html',res=carr)
if __name__ == "__main__":
    app.run(debug = True)
