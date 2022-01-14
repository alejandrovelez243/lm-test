from core import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(40), unique=False, nullable=False)
    middle_name = db.Column(db.String(40), unique=False, nullable=True)
    last_name = db.Column(db.String(40), unique=False, nullable=False)
    zip_code = db.Column(db.String(10), unique=False, nullable=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'middle_name': self.middle_name,
            'zip_code': self.zip_code
        }


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(40), unique=False, nullable=False)
    country = db.Column(db.String(40), unique=False, nullable=True)
    state = db.Column(db.String(40), unique=False, nullable=False)
    latitud = db.Column(db.Float(20), unique=False, nullable=False)
    longitud = db.Column(db.Float(20), unique=False, nullable=False)
    zip_code = db.Column(db.String(10), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    user = db.relationship('User',
        backref=db.backref('posts', lazy=True))

    def __init__(self, **kwargs):
        super(City, self).__init__(**kwargs)

    def __repr__(self):
        return '<City %r>' % self.city

    def serialize(self):
        return {
            'id': self.id, 
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code
        }