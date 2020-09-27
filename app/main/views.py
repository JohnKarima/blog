from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from . import main
from ..request import get_quotes
from ..models import User, Blog, Comment
from .forms import UpdateProfile, BlogForm, CommentForm
from .. import db, photos
import markdown2


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'TheVoid.com'
    message = 'Blog Gang Rise UP!!!'
    quotes = get_quotes()
    blogs = Blog.get_all_blogs()
    return render_template('index.html', message = message, title = title, quotes=quotes, blogs = blogs)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



@main.route('/new_blog', methods = ['GET','POST'])
def new_blog():
    form = BlogForm()
    title = 'New Blog Post'
    if form.validate_on_submit():
        blog = Blog(blog = form.blog_post.data)
        
        blog.save_blog()
        return redirect(url_for('main.index'))

    return render_template('/new_blog.html',blog_form = form, title = title)



@main.route("/blog/<int:id>",methods = ["GET","POST"])
def blog_page(id):
    blog = Blog.query.filter_by(id = id).first()
    title = 'Blog Post'
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment = comment, blog = blog)
        new_comment.save_comments()
        return redirect(url_for('main.blog_page', id = blog.id))

    comments = Comment.query.filter_by(blog_id = blog.id)
    return render_template("blog.html", title = title, blog = blog, comment_form = form, comments = comments)



@main.route("/delete/comment/<id>")
def delete_comment(id):
    comment = Comment.query.filter_by(id = id).first()
    blog_id = comment.blog.id
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.blog_page", id = blog_id))



# @main.route('/add_comment', methods = ['GET','POST'])
# def new_comment():
#     form = CommentForm()
#     title = 'Add comment'
#     if form.validate_on_submit():
#         comment = Comment(comment = form.comment.data)
#         comment.save_comments()
#         return redirect(url_for('main.index'))
#     return render_template('/add_comment.html',comment_form = form, title = title)




# @main.route('/blog/comments/new/<int:id>',methods = ['GET','POST'])
# def new_comment(id):
#     form = CommentForm()
   
#     if form.validate_on_submit():
#         new_comment = Comment(blog_id =id,comment=form.comment.data)
#         new_comment.save_comments()
#         return redirect(url_for('main.post',blog_id=id))
    
#     return render_template('add_comment.html',comment_form=form)