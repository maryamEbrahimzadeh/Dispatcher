from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/')

def calc():

    return render_template(

        'index.html')

@app.route('/<string:ip>',methods=['POST'])

def getnum():
	text = request.form['textarea']
	num = text.split()
	if num[1]=="+" :
		r = requests.post(ip + ':3000',json={"param1": num[0],"param2" : num[2]})
	elif  num[1]=="-"
		r = requests.post(ip + ':3000',json={"param1": num[0],"param2" : num[2]})
	elif  num[1]=="/"
		r = requests.post(ip + ':3000',json={"param1": num[0],"param2" : num[2]})
	elif  num[1]=="*"
		r = requests.post(ip + ':3000',json={"param1": num[0],"param2" : num[2]})
	


if __name__ == "__main__":

    app.run(host = '0.0.0.0')

