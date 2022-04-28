from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from forms import Blog
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'


@app.route("/")
def index_page():
    blog = Blog(csrf_enabled=False)
    return render_template("index.html",template_form = blog)



@app.route("/academics")
def academics_page():
    return render_template("academics.html")


file_connection = open("C:/code/github/personal_blog/all_posts.json", 'r')
posts = json.load(file_connection)
file_connection.close()


@app.route("/all_posts", methods=["GET", "POST"])
def all_the_posts():
    post = Blog(csrf_enabled=False)
    if post.validate_on_submit():
        id = len(posts) + 1
        posts.append({
            "date": post.date.data,
            "post": post.post.data
            })
        file_connection = open("C:/code/github/personal_blog/all_posts.json", 'w')
        json.dump(posts, file_connection)
        file_connection.close()
    return render_template("all_posts.html",posts=posts, template_form = post)




if __name__ == "__main__":
    app.run(debug=True)