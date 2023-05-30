from flask import Flask, render_template, request, redirect, url_for
from models.topic import TopicModel
from models.question import QuestionModel
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['DEBUG'] = True

uri = os.getenv("DATABASE_URL", "sqlite:///data.db")

if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

## uncomment to add entries to db
# db = SQLAlchemy(app)

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/quizzes")
def quizzes():

    topics = TopicModel.query.all()

    entries_topics = [
        (
            entry.name,
            entry.desc
        )
        for entry in topics
    ]

    return render_template("quizzes.html", entries_topics=entries_topics)

@app.route("/quiz/<topic>/<question_num>", methods = ['POST', 'GET'])
def quiz(topic, question_num):

    topic = topic
    question_num = int(question_num)

    question_obj = QuestionModel.query.filter_by(topic_name=topic, question_num=question_num).first()

    question = question_obj.question
    answers = question_obj.answers.split("|")
    answer_correct = question_obj.answer_correct
    question_max = question_obj.question_max

    answer_response = ''

    global tally

    if request.method == "POST":

        movement = request.form['submit_movement']

        if movement == 'submit':

            answer_selection = request.form.get('options')

            if question_num == 1:

                tally = []

            if answer_selection == answer_correct:
            
                answer_response = 'Correct!'

                tally.append(1)

            else:
                answer_response = 'Incorrect!'

                tally.append(0)

        else:

            if question_num < question_max:

                return redirect(url_for('quiz', topic=topic, question_num=(question_num + 1)))

            else:

                return redirect(url_for('result', topic=topic))

    return render_template("quiz.html", question=question, answers=answers, answer_response=answer_response)

@app.get("/result/<topic>")
def result(topic):

    result = sum(tally) / len(tally)
    result = f"{result:.0%}"

    return render_template("result.html", topic=topic, result=result)


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