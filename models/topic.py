from db import db

class TopicModel(db.Model):
    __tablename__ = 'topic'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    desc = db.Column(db.String(240))

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Topic {self.name}>'
    
    @classmethod
    def find_by_topic_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_by_topic_id(cls, _id):
        return cls.query.filter_by(id=_id).first()