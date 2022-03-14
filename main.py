from flask import Flask, render_template, url_for


app = Flask(__name__, template_folder= "template");
host = "0.0.0.0";
port = 5050;

@app.route("/")
def index():
    return render_template("index.html");


if __name__ == "__main__":
    app.run(host, port, debug = True);