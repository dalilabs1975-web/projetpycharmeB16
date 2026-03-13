from flask import Flask
app = Flask(__name__)
@app.route ('/acme/')
def index():
	return 'bienvenue'
if __name__ =='__name__':
	app.run(debug =True , port=5000)
