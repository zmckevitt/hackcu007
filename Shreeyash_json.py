#!flask/bin/python
import sys
from flask import Flask, render_template, request, redirect, Response
import random, json
app = Flask(__name__, template_folder="templates")

@app.route("/")
def output():
	p = '{"name": "Bob", "languages": ["Python", "Java"]}'
	y = json.loads(p)
	result=y["name"]
	return result
    #return "Hello World!"


if __name__ == "__main__":
    # run!
	app.run("0.0.0.0", "5020")
