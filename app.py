from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

app.config['DEBUG'] = True

uri = os.getenv("DATABASE_URL", "sqlite:///data.db")

if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/quizzes")
def quizzes():

    entries = [1,2,3]

    return render_template("quizzes.html", entries=entries)

@app.route("/quiz/<topic>/<question_num>", methods = ['POST', 'GET'])
def quiz(topic, question_num):

    if request.method == "POST":
        pass

    return render_template("quiz.html")

@app.get("/result/<topic>")
def result():

    entries = [1,2,3]

    return render_template("result.html", entries=entries)


if __name__ == '__main__':
    from db import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # if app.config['DEBUG']:
    #     @app.before_first_request
    #     def create_tables():
    #         db.create_all()

    app.run(port=5000)