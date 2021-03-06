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
    # result = ''
    # try:
    #     data = request.get_json()
    #     result = 'SUCCESS'
    # except:
    #     result = 'FAIL'
    # if request.is_json:
    #     print("is json")
    #     data = request.get_json()

    #     for item in data:
    #         result += str(item['firstname'])
    #         break
    # else:
    #     print(type(request))

    # result = 'hello'
    # data = request.json
    # try: 
    #     data = request.json
    #     try:
    #         json_obj = json.loads(data)
    #         result = 'success'
    #     except:
    #         result = 'fail1'
    # except:
    #     result = 'fail'

    # print(data)
    # return result

    data = request.get_json()
    print(data['title'])
    print(request)
    return data['title']
    # data = request.json
    # print("data is " + format(data))
    # return redirect('localhost:5020/receiver')

if __name__ == "__main__":
    # run!
	app.run("0.0.0.0", "5020")
