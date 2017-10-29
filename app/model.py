from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#create model User
class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.Integer, unique=True, index=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id'))
    #when dataengine get data from database then it create instance like User(**data)
    # (there are also can be problem with id) should init like this
    def __init__(self, password=None, **data):
        if password is not None:
            data['password_hash'] = generate_password_hash(password)
        super(User, self).__init__(**data)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)

class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    rolename = db.Column(db.String(255))
    users = db.relationship(
        'User',
        backref='role',
        lazy='dynamic'
    )

    def __init__(self, rolename):
        self.rolename = rolename

    def __repr__(self):
        return "<Role '{}'>".format(self.rolename)