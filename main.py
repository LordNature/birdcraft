from flask import Flask
app = Flask(__name__)

# Home Routing
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	return "In development"

# Profile Placeholder
@app.route('/<id>')
def hello_name(name):
	return "Your id is {}".format(id)

if __name__ == '__main__':
	app.run()