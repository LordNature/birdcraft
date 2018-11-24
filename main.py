from flask import Flask, render_template, request
app = Flask(__name__)

# Home Routing
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	return "In development"

# Profile Placeholder
@app.route('/u<id>')
def profile(id):
	return "Your id is {}".format(id)

if __name__ == '__main__':
	app.run()