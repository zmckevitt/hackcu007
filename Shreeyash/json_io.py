from flask import Flask
from flask import request
app = Flask(__name__)

# @app.route("/output")
#
# def output():
# 	return "Hello World peen master!"
#
#
# if __name__ == "__main__":
# 	app.run("0.0.0.0", "5010")


# allow both GET and POST requests
# allow both GET and POST requests
@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')

    return '''<h1>The language value is: {}</h1>'''.format(language)

# allow both GET and POST requests
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Language: <input type="text" name="language"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>'''

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == "__main__":
	app.run("0.0.0.0", "5010")
