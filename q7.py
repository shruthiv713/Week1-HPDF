from flask import Flask,request,render_template
app=Flask(__name__,template_folder='Templates')
@app.route('/input')
def inp():
	return render_template('input.html')
@app.route('/result',methods=['POST','GET'])
def res():
	if request.method=='POST' :
		result=request.form['inp']
		print result
		return result
if __name__=="__main__":
	app.run()
	
