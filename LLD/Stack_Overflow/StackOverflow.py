from LLD.Stack_Overflow.Answer import Answer
from LLD.Stack_Overflow.Commentable import Commentable
from LLD.Stack_Overflow.Question import Question
from LLD.Stack_Overflow.Tag import Tag
from LLD.Stack_Overflow.User import User
from LLD.Stack_Overflow.Votable import Votable


class StackOverflow:
    def __init__(self):
        self.users: dict[int, User] = {}
        self.questions: dict[int, Question] = {}
        self.answers: dict[int, Answer] = {}
        self.tags: dict[str, Tag] = {}

    def create_user(self, username: str, email: str):
        user = User(username, email)
        self.users[user.id] = user
        return user

    def post_question(self, user: User, title: str, content: str, tags: list):
        question = user.ask_question(title, content, tags)
        self.questions[question.id] = question
        for tag in question.tags:
            self.tags.setdefault(tag.name, tag)
        return question

    def post_answer(self, user: User, question: Question, content: str):
        answer = user.answer_question(question, content)
        self.answers[answer.id] = answer
        return answer

    def add_comment(self, user: User, commentable: Commentable, content: str):
        return user.comment_on(commentable, content)

    def add_vote(self, user: User, votable: Votable, value: int):
        votable.vote(user, value)

    def accept_answer(self, answer: Answer):
        answer.accept()

    def search_question(self, query: str):
        return [q for q in self.questions.values() if
                query.lower() in q.title.lower() or
                query.lower() in q.content.lower() or
                any(query.lower() == tag.name for tag in q.tags)]

    def get_user(self, user_id: int):
        return self.users.get(user_id)

    def get_questions_by_user(self, user: User):
        return user.questions

    def get_question(self, question_id: int):
        return self.questions.get(question_id)

    def get_answer(self, answer_id: int):
        return self.answers.get(answer_id)

    def get_answers_by_question(self, question: Question):
        return question.answers

    def get_tag(self, name: str):
        return self.tags.get(name)
