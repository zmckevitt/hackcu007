#!flask/bin/python
import sys
from flask import Flask, render_template, request, redirect, Response
import random, json
app = Flask(__name__, template_folder="templates")

@app.route("/")
def output():
	return render_template("tentacles.html", name="Joe")
    #return "Hello World!"

@app.route('/receiver', methods = ['GET','POST'])
def worker():

    data = request.get_json()
    # print(request)
    string_dat = "fname: " + data['title'] + "lname: " + data['article'] + "time: " + data['time']
    print(string_dat)
    return string_dat


if __name__ == "__main__":
    # run!
	app.run("0.0.0.0", "5020")
