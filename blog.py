from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from forms import Blog

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'


@app.route("/")
def index_page():
    blog = Blog(csrf_enabled=False)
    return render_template("index.html",template_form = blog)



@app.route("/academics")
def academics_page():
    return render_template("academics.html")


if __name__ == "__main__":
    app.run(debug=True)