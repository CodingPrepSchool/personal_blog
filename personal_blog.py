from flask import Flask, redirect, render_template, request
from flask_bootstrap import Bootstrap
import json
from blog_forms import Postsforms

app=Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

postsl=[]
file_connection = open("C:/code/bootstrap/personal_blog/posts.json", 'r')
postsl = json.load(file_connection)
file_connection.close()
@app.route("/", methods = ["GET", "POST"])
def homepage():
    postsform= Postsforms(csrf_enabled=False)
    if postsform.validate_on_submit():
        id = len(postsl) + 1
        postsl.append({"date": postsform.date.data, 
        "post_message": postsform.post_message.data,})
        file_connection = open("C:/code/bootstrap/personal_blog/posts.json", 'w')
        json.dump(postsl, file_connection)
        file_connection.close()
    return render_template("personal_blog.html", postsl=postsl, template_form = postsform)

@app.route("/academics")
def academics():
    return render_template("academics.html")

@app.route("/posts", methods=["GET", "POST"])
def allposts():
    return render_template("post_page.html", postsl=postsl)

