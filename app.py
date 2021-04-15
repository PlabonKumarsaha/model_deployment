from flask import Flask, render_template, request
import marks

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        hrs = request.form['hrs']
        marks_pred = marks.marks_prediction(hrs)
        mk = marks_pred
        print("ok" + marks_pred)

    return render_template("index.html",my_marks = mk)


@app.route('/sub', methods=['POST'])
def submit():
    # data from html -> python
    if request.method == "POST":
        name = request.form["userName"]
    # python file to html
    return render_template("sub.html", nameData=name)


if __name__ == '__main__':
    app.run()
