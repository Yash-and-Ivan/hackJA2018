from flask import Flask

# create app
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "Hello, world"
