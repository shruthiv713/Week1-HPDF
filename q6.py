from flask import Flask,render_template
app=Flask(__name__,template_folder='Templates')
@app.route('/image')
def render():
        return render_template('show.html')
if __name__=="__main__":
	app.run()
	

