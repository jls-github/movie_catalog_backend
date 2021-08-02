from ..db import db

class Movie(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), unique=False, nullable=False)

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'title'      : self.title,
       }

    def __repr__(self):
        return '<Movie %r>' % self.title