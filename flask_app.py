
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
comments = []
app.config["DEBUG"] = True

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        print(comments)
        return render_template("main_page.html", comments=comments)
    comments.append(request.form["contents"])
    return redirect(url_for('index'))
