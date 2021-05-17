from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/hello")
def hello_world2():
    return "Once again hello world!"

def hello_world3():
    return "Another hello world!"

app.add_url_rule("/hello_again", "hello_again", hello_world3)


if __name__ == "__main__":
    app.run(debug = True)
