from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
import json
from forms import NewPost

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route("/")
def index():
    new_post = NewPost(meta={'csrf': False})
    return render_template("blog.html", template_form = new_post)

# Add a New Post #
file_connection = open("/Users/olganaymushina/code/github/personal_blog/new_post.json", 'r')
posts_json = json.load(file_connection)
file_connection.close()

@app.route("/add-post", methods=["POST"])
def new_post():
    new_post = NewPost(meta={'csrf': False})
    if new_post.validate_on_submit():
        id = len(posts_json) + 1
        posts_json.append({
            "date": str(new_post.date.data),
            "post": str(new_post.post.data)
        })
        file_connection = open("/Users/olganaymushina/code/github/personal_blog/new_post.json", 'w')
        json.dump(posts_json, file_connection)
        file_connection.close()
    return redirect("/")


# Display All Posts #
@app.route("/display-all")
def all_posts():
    return render_template("all_posts.html", posts_json=posts_json)


# Academics Page #
@app.route("/academics")
def academ():
    return render_template("academics.html")

# Hobbies Page #
@app.route("/hobbies")
def my_hobbies():
    return render_template("hobbies.html")

# Contact Info Page #
@app.route("/contact-info")
def contact_info():
    return render_template("contact.html")




if __name__ == "__main__":
    app.run(debug=True)