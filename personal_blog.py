from flask import Flask, redirect, render_template, request
from flask_bootstrap import Bootstrap
import json
from blog_forms import Postsforms

app=Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route("/")
def homepage():
    postsform= Postsforms(csrf_enabled=False)
    return render_template("personal_blog.html", template_form = postsform)

postsl=[]
file_connection = open("C:/code/bootstrap/personal_blog/posts.json", 'r')
postsl = json.load(file_connection)
file_connection.close()

@app.route("/addpost", methods = ["GET", "POST"])
def addpost():
    postsform= Postsforms(csrf_enabled=False)
    if postsform.validate_on_submit():
        id = len(postsl) + 1
        postsl.append({
            "date": str(postsform.date.data), 
            "post_message": str(postsform.post_message.data)
            })
    print("my post", postsl)
    file_connection = open("C:/code/bootstrap/personal_blog/posts.json", 'w')
    json.dump(postsl, file_connection)
    file_connection.close()
    return render_template("message.html", postsl=postsl, template_form = postsform)


@app.route("/academics")
def academics():
    return render_template("academics.html")

@app.route("/posts", methods=["GET", "POST"])
def allposts():
    return render_template("post_page.html", postsl=postsl)

@app.route("/contactme", methods=["GET", "POST"])
def contactme():
    return render_template("contactinfo.html")


