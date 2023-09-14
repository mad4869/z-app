from datetime import datetime

from .. import db


class Like(db.Model):
    __tablename__ = "likes"
    like_id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.user_id"))
    xweet_id = db.Column(db.Integer(), db.ForeignKey("xweets.xweet_id"))
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime())

    def serialize(self):
        return {
            "like_id": self.like_id,
            "user_id": self.user_id,
            "xweet_id": self.xweet_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __repr__(self):
        return f"{self.user_id} likes {self.xweet_id}"
