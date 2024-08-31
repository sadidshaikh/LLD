from datetime import datetime

from LLD.Stack_Overflow.Comment import Comment
from LLD.Stack_Overflow.Commentable import Commentable
from LLD.Stack_Overflow.Question import Question
from LLD.Stack_Overflow.User import User
from LLD.Stack_Overflow.Votable import Votable
from LLD.Stack_Overflow.Vote import Vote


class Answer(Commentable, Votable):
    VOTE_REPUTATION = 10
    ACCEPTED_REPUTATION = 15

    def __init__(self, author: User, content: str, question: Question):
        self.id = id(self)
        self.author = author
        self.content = content
        self.question = question
        self.creation_date = datetime.now()
        self.votes = []
        self.comments = []
        self.is_accepted = False

    def vote(self, user: User, value: int):
        if value not in {-1, 1}:
            raise ValueError("Vote value must be either 1 or -1")
        self.votes = [v for v in self.votes if v.user != self.author]
        self.votes.append(Vote(user, value))
        self.author.update_reputation(Answer.VOTE_REPUTATION * value)

    def get_vote_count(self):
        return sum(v.value for v in self.votes)

    def add_comment(self, comment: Comment):
        self.comments.append(comment)

    def get_comments(self):
        return self.comments.copy()

    def accept(self):
        if self.is_accepted:
            raise ValueError("Value is already accepted")
        self.is_accepted = True
        self.author.update_reputation(Answer.ACCEPTED_REPUTATION)
