from flask import Flask, render_template

portafolio = Flask(__name__)

@portafolio.route("/")

def home():
    return render_template("home.html")








if __name__ == '__main__':
    portafolio.run(debug=True)