from LLD.Stack_Overflow.Answer import Answer
from LLD.Stack_Overflow.Question import Question
from LLD.Stack_Overflow.Comment import Comment


class User:
    QUESTION_REPUTATION = 5
    ANSWER_REPUTATION = 10
    COMMENT_REPUTATION = 2

    def __init__(self, username: str, email: str):
        self.id = id(self)
        self.username = username
        self.email = email
        self.reputation = 0
        self.questions: list[Question] = []
        self.answers: list[Answer] = []
        self.comments: list[Comment] = []

    def ask_question(self, title: str, content: str, tags: list):
        question = Question(self, content, title, tags)
        self.questions.append(question)
        self.update_reputation(User.QUESTION_REPUTATION)
        return question

    def answer_question(self, question, content: str):
        answer = Answer(self, content, question)
        self.answers.append(answer)
        self.update_reputation(User.ANSWER_REPUTATION)
        return answer

    def comment_on(self, commentable, content: str):
        comment = Comment(self, content)
        self.comments.append(comment)
        commentable.add_comment(comment)
        self.update_reputation(User.COMMENT_REPUTATION)
        return comment

    def update_reputation(self, value):
        self.reputation += value
        self.reputation = max(self.reputation, 0)
