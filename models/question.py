from db import db

class QuestionModel(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(240))
    answers = db.Column(db.String(240)) # change to blob type, or string + split
    answer_correct = db.Column(db.String(80))
    topic_name = db.Column(db.String(80))
    question_num = db.Column(db.Integer)

    def __init__(self, question, answers, answer_correct, topic_name, question_num):
        self.question = question
        self.answers = answers
        self.answer_correct = answer_correct
        self.topic_name = topic_name
        self.question_num = question_num

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Question {self.topic_name} {self.question_num}>'
    
    @classmethod
    def find_by_question_id(cls, _id):
        return cls.query.filter_by(id=_id).first()