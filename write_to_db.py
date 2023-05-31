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
q_1 = QuestionModel(
        question = 'The Confusion Matrix is useful for evaluating a classification algorithm.',
        answers = "True|False",
        answer_correct = 'True',
        topic_name = 'Data Science',
        question_num = 1,
        question_max = 4
        )

q_2 = QuestionModel(
        question = 'K-Means is a common ________ learning algorithm.',
        answers = "supervised|unsupervised",
        answer_correct = 'unsupervised',
        topic_name = 'Data Science',
        question_num = 2,
        question_max = 4
        )

q_3 = QuestionModel(
        question = 'Logistic Regression uses the ________ function for separation.',
        answers = "Tanh|ReLU|Sigmoid",
        answer_correct = 'Sigmoid',
        topic_name = 'Data Science',
        question_num = 3,
        question_max = 4
        )

q_4 = QuestionModel(
        question = 'Gradient Boosting is NOT a form of ensemble learning.',
        answers = "True|False",
        answer_correct = 'False',
        topic_name = 'Data Science',
        question_num = 0,
        question_max = 4
        )