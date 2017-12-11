
from flask import Flask,request,make_response
app=Flask(__name__)
@app.route('/setcookie')
def setcookie():
	res=make_response();
	res.set_cookie('Name','Shru')
	res.set_cookie('Age','19')
	return res
@app.route('/getcookie')
def getcookie():
	name=request.cookies.get('Name')
	age=request.cookies.get('Age')
	return 'Name : '+name+' Age : '+age
if __name__ == "__main__":
    app.run()
