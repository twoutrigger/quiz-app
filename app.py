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

    # add start button for start a particular quiz

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

    # need to initiate an object to tally score

    if request.method == "POST":

        movement = request.form['submit_movement']

        if movement == 'submit':
            pass

        else:
            if question_num < question_max:

                print(f'topic: {topic} | question_num: {question_num} | question_max: {question_max}')

                redirect(url_for('quiz', topic=topic, question_num=(question_num + 1)))
                # redirect(url_for('quiz', topic=topic, question_num=2))

            else:

                redirect(url_for('result', topic=topic))

        # double check how to update page without refreshing page

        answer_response = 'Correct!'

    return render_template("quiz.html", question=question, answers=answers, answer_response=answer_response)

@app.get("/result/<topic>")
def result(topic):

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