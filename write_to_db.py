from models.topic import TopicModel
from models.question import QuestionModel

# add topics:
t_1 = TopicModel(
        name = 'Test Topic',
        desc = 'Test Description'
        )

# add questions:
q_1 = QuestionModel(
        topic_name = 'Test Topic',
        question_num = 1,
        question = 'Test Question',
        answers = [1, 2, 3],
        answer_correct = 1
        )