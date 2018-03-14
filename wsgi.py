from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello From The Other Side!"

if __name__ == "__main__":
    application.run()
