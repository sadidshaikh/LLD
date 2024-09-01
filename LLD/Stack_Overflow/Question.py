from datetime import datetime

from LLD.Stack_Overflow.Commentable import Commentable
from LLD.Stack_Overflow.Tag import Tag
from LLD.Stack_Overflow.Votable import Votable
from LLD.Stack_Overflow.Vote import Vote


class Question(Commentable, Votable):
    VOTE_REPUTATION = 5

    def __init__(self, author, content: str, title: str, tag_names: list):
        self.id = id(self)
        self.author = author
        self.content = content
        self.title = title
        self.answers = []
        self.comments = []
        self.votes = []
        self.tags = [Tag(name) for name in tag_names]
        self.creation_date = datetime.now()

    def add_answer(self, answer):
        if answer not in self.answers:
            self.answers.append(answer)

    def vote(self, user, value: int):
        if value not in {-1, 1}:
            raise ValueError("Vote value must be either 1 or -1")
        self.votes.append(Vote(user, value))
        self.author.update_reputation(Question.VOTE_REPUTATION * value)

    def get_vote_count(self):
        return sum(v.value for v in self.votes)

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_comments(self):
        return self.comments.copy()
