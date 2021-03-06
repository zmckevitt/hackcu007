from flask import Flask
app = Flask(__name__)

@app.route("/")
def output():
	#return render_template("index.html", name="Joe")
    return "Hello World!"

if __name__ == "__main__":
	app.run()