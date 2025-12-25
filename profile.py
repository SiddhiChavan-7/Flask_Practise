from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def student_profile():
    return render_template(
        "profile.html",
        name="Siddhi",
        is_topper=True,
        subjects=["Math", "Science", "History"]
    )

@app.route("/")
def test():
    return "Flask is working"

if __name__ == "__main__":
    app.run(debug=True)
