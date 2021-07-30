from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
	return render_template('firstpage.html')
@app.route('/ISRO')
def isro():
	return render_template('isro.html')
@app.route('/NASA')
def nasa():
	return render_template('nasa.html')
@app.route('/BLUEORIGIN')
def blueorigin():
	return render_template('blueorigin.html')
@app.route('/SPACEX')
def spacex():
	return render_template('spacex.html')

if __name__ == "__main__":
    app.run(debug=False)