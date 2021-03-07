#!flask/bin/python
import sys
from flask import Flask, render_template, request, redirect, Response
import random, json, subprocess, time

app = Flask(__name__, template_folder="templates")
python_file = 'test.py'
_fname = 'testfile.txt'

#add port variable

def query_pipe(arg1, arg2, arg3):
    timeoutInSeconds = 1                                                                     # Our timeout value.
    cmd   =  'python ' + python_file + ' ' + arg1 + ' ' +  arg2 + ' ' + arg3                 # Your desired command.
    proc  =  subprocess.Popen(cmd,shell=True)                                                # Starting main process.
    timeStarted = time.time()                                                                # Save start time.
    cmdTimer     =  "sleep "+str(timeoutInSeconds)                                           # Waiting for timeout...
    cmdKill      =  "kill "+str(proc.pid)+" 2>/dev/null"                                     # And killing process.
    cmdTimeout   =  cmdTimer+" && "+cmdKill                                                  # Combine commands above.
    procTimeout  =  subprocess.Popen(cmdTimeout,shell=True)                                  # Start timeout process.
    proc.communicate()     

def read_file(fname):
    f = open("txt_files/"+fname, "r")
    return f.readlines()

def gen_kwargs(num):
    # read file here to get data
    arg = []
    val = []
    _file = read_file(_fname)
    d = {}
    for i in range(0,num):
        arg.append("arg" + str(i))
        val.append(_file[i])
    d = {arg[i]: val[i] for i in range(num)}
    return d


@app.route("/")
def output():
	return render_template("index.html")

@app.route('/receiver', methods = ['GET','POST'])
def worker():
    data = request.get_json()
    print(request)
    arg1 = data['title']
    arg2 = data['article']
    arg3 = data['time']
    string_dat = "fname: " + arg1 + " lname: " + arg2 + " time: " + arg3
    query_pipe(arg1, arg2, arg3)
    print(string_dat)
    # return string_dat
    return redirect("/redirect")

@app.route("/redirect")
def redirected():
    #need to read file to determine arguments
    #call kwarg generator function
    kwargs = gen_kwargs(3)
    return render_template("redirect.html", **kwargs)

if __name__ == "__main__":
    # run!
	app.run("0.0.0.0", "5020")
