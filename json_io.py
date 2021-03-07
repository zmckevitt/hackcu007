#!flask/bin/python
import sys
from flask import Flask, render_template, request, redirect, Response
import random, json, subprocess, time

app = Flask(__name__, template_folder="templates")
python_file = 'spotify_data.py'
_fname = 'out.txt'

uname_old = 'zackagawea10'
uname_new = ''

#add port variable

def query_pipe(arg1, arg2):
    timeoutInSeconds = 5                                                                     # Our timeout value.
    cmd   =  'python ' + python_file + ' ' + arg1 + ' ' +  arg2                              # Your desired command.
    proc  =  subprocess.Popen(cmd,shell=True)                                                # Starting main process.
    timeStarted = time.time()                                                                # Save start time.
    cmdTimer     =  "sleep "+str(timeoutInSeconds)                                           # Waiting for timeout...
    cmdKill      =  "kill "+str(proc.pid)+" 2>/dev/null"                                     # And killing process.
    cmdTimeout   =  cmdTimer+" && "+cmdKill                                                  # Combine commands above.
    procTimeout  =  subprocess.Popen(cmdTimeout,shell=True)                                  # Start timeout process.
    proc.communicate()    

def remove_cache(uname):
    try:
        timeoutInSeconds = 1                                                                     # Our timeout value.
        cmd   =  'rm -r .cache-' + uname                                                         # Your desired command.
        proc  =  subprocess.Popen(cmd,shell=True)                                                # Starting main process.
        timeStarted = time.time()                                                                # Save start time.
        cmdTimer     =  "sleep "+str(timeoutInSeconds)                                           # Waiting for timeout...
        cmdKill      =  "kill "+str(proc.pid)+" 2>/dev/null"                                     # And killing process.
        cmdTimeout   =  cmdTimer+" && "+cmdKill                                                  # Combine commands above.
        procTimeout  =  subprocess.Popen(cmdTimeout,shell=True)                                  # Start timeout process.
        proc.communicate()    
    except:
        print("No cache file to delete")

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
@app.route("/home", methods = ['GET','POST'])
def output():
	return render_template("index.html")

@app.route('/receiver', methods = ['GET','POST'])
def worker():
    global uname_old
    global uname_new
    data = request.get_json()
    print(request)
    arg1 = data['title']
    arg2 = data['time']
    uname_new = arg1
    arg1 = uname_old
    string_dat = "uname: " + arg1 + " time: " + arg2
    query_pipe(arg1, arg2)
    if(arg1 != ''):
        remove_cache(arg1)
        return redirect("/home")
    else:
        uname_new = uname_old
        uname_old = uname_new
    
    print(string_dat)
    return redirect("/redirect")

@app.route("/redirect")
def redirected():
    #need to read file to determine arguments
    #call kwarg generator function
    kwargs = gen_kwargs(44)
    #, **kwargs
    return render_template("redirect.html", **kwargs)

@app.route("/callback")
def auth():
    #need to read file to determine arguments
    #call kwarg generator function
    #, **kwargs
    return render_template("OLD_index.html")

if __name__ == "__main__":
    # run!
	app.run("0.0.0.0", "5020")
