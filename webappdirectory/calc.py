from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/')

def calc():

    return render_template(

        'index.html')

@app.route('/',methods=['POST'])

def getnum():

	text = request.form['textarea']
	num = text.split()
	r = requests.post('0.0.0.0:3000',json={"param1": num[0],"param2" : num[1]})
	#return num[0]


if __name__ == "__main__":

    app.run(host = '0.0.0.0')

