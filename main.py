from flask import Flask, render_template, request
app = Flask(__name__)

# Home Routing
@app.route('/')
def home():
	return render_template('index.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		usr = request.form['usr']
		pwd = request.form['pwd']
		error = None

		if not usr:
			error = "Username required."
		elif not pwd:
			error = "Password required."

		if error is None:
			return "worked"

		flash(error)
	return render_template('login.html')

# Profile Placeholder
@app.route('/u<id>')
def profile(id):
	return "Your id is {}".format(id)

if __name__ == '__main__':
	app.run()