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

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}!"

@app.route("/blog/<int:postID>")
def show_blog(postID):
    return f"Blog Number {postID}"

@app.route("/rev/<float:revNo>")
def revision(revNo):
    return f"Revision Number {revNo}"


if __name__ == "__main__":
    app.run(debug = True)
