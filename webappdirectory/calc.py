from flask import Flask, render_template, request
import requests
import os


app = Flask(__name__)


@app.route('/')
def calc():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getnum():
    text = request.form['textarea']
    num = text.split()
    ip = os.environ['add_ip']
    r = requests.post('http://' + ip + ':3000/add', json={"param1": num[0],
                                                          "param2": num[2]})
    return r.text


if __name__ == "__main__":
    app.run(host='0.0.0.0')
