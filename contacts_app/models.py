from contacts_app import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    contacts = db.relationship('Contact', backref='contacs_user', lazy=True)

    def __repr__(self) -> str:
        return self.username

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return self.name
