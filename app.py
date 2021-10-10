from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>hello world!!</h1>"

@app.route("/test")
def html():
    return render_template("test.html")

@app.route("/test2")
def html2():
    return render_template("test2.html")

if __name__ == "__main__":
    app.run()


