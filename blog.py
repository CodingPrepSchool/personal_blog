from flask import Flask, render_template, request, redirect
import json
import sqlite3
from flask_bootstrap import Bootstrap
from formes import Blog

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route("/")
def index():
    blog = Blog(csrf_enabled=False)
    return render_template("index.html",template_form=blog)

@app.route("/academics")
def grades():
    blog = Blog(csrf_enabled=False)
    return render_template("academincs.html")

@app.route("/all_posts")
def multiple_posts():
    return render_template("all_posts.html")


post0=[]
file_connection = open("C:/code/github/personal_blog/posts.json", 'r')
post0 = json.load(file_connection)
file_connection.close()
@app.route("/add-post", methods = ["GET", "POST"])
def homepage():
    blog = Blog(csrf_enabled=False)
    if blog.validate_on_submit():
      id=len(post0)+1
      post0.append({"date": blog.date.data, 
        "post_message": blog.new_post.data,})
    return render_template("message.html",blog=Blog, template_form = blog)
file_connection = open("C:/code/github/personal_blog/posts.json", 'w')
json.dump(post0, file_connection)
file_connection.close()

@app.route("/contact-me")
def contact_info():
    return render_template("contact.html")

@app.route("/hobbies")
def my_hobbies():
    return render_template("hobbies.html")
    



if __name__ == "__main__":
    app.run(debug=True)
