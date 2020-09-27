from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Quotes:
    '''
    Quote class to define Quote Objects
    '''
    def __init__(self,id,author,quote):
        self.id =id
        self.author = author
        self.quote = quote



class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'



class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'


class Blog(db.Model):
    '''
    Blog class that define Blog Objects
    '''
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    blog = db.Column(db.Text)
    date = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.add(self)
        db.session.commit()
    
    def update_blog(self):
        db.session.update(self)
        db.session.commit()
    
    @classmethod
    def get_all_blogs(cls):
        return Blog.query.all()



class Comment(db.Model):
    
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save_comments(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments

    @classmethod
    def clear_(cls):
        Comment.all_comments.clear()


    def delete_comments(self):
        db.session.add(self)
        db.session.commit()
    
    def update_comments(self):
        db.session.update(self)
        db.session.commit()