from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/',methods=["post","get"])
def hello_world():
	if request.method == 'POST':
		return request.form["email"]
	else:
		return render_template("index.html")
