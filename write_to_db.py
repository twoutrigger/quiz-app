from models.topic import TopicModel
from models.question import QuestionModel

# add topics:
t_1 = TopicModel(
        name = 'Data Science',
        desc = 'Questions related to Data Science'
        )

t_2 = TopicModel(
        name = 'Business Intelligence',
        desc = 'Questions related to Business Intelligence'
        )

t_3 = TopicModel(
        name = 'Data Engineering',
        desc = 'Questions related to Data Engineering'
        )

# add questions:
q_x = QuestionModel(
        question = 'Test Question',
        answers = ['1', '2', '3'],
        answer_correct = '1',
        topic_name = 'Test Topic',
        question_num = 1,
        num_max = 3
        )

q_1 = QuestionModel(
        question = 'Is Confusion Matrix useful for classification?',
        answers = "True|False",
        answer_correct = 'True',
        topic_name = 'Data Science',
        question_num = 1,
        num_max = 3
        )

q_2 = QuestionModel(
        question = '',
        answers = "|",
        answer_correct = '',
        topic_name = 'Data Science',
        question_num = 2,
        num_max = 3
        )

q_3 = QuestionModel(
        question = '',
        answers = "|",
        answer_correct = '',
        topic_name = 'Data Science',
        question_num = 3,
        num_max = 3
        )