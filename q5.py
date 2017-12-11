from flask import Flask,abort,redirect
import requests
app=Flask(__name__)
@app.route('/robots.txt')
def deny():
	abort(403)
@app.route('/robot.txt')
def deny2():
	return redirect('http://httpbin.org/deny')

if __name__== "__main__":
	app.run()
	
	
