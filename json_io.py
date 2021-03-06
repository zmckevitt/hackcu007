#!flask/bin/python
import sys
from flask import Flask, render_template, request, redirect, Response
import random, json
app = Flask(__name__, template_folder="templates")

@app.route("/")
def output():
	return render_template("index.html", name="Joe")
    #return "Hello World!"

@app.route('/receiver', methods = ['GET','POST'])
def worker():
	# read json + reply
    # data = request.get_json()
    result = ''
    if request.is_json:
        print("is json")
        data = request.get_json()

        for item in data:
            result += str(item['firstname'])
            break
    else:
        print(type(request))

    return str(request)

if __name__ == "__main__":
    # run!
	app.run("0.0.0.0", "5020")
