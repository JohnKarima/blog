from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    blog_post = TextAreaField('Create a new blog post', validators=[Required()])
    submit = SubmitField('Submit') 

class CommentForm(FlaskForm):
    comment = StringField('Comment',validators=[Required()])
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
    email = StringField("Enter email", validators = [Required()])
    submit = SubmitField("Subscribe")