from flask import Flask, render_template, request
from agent import run_search

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    query = None
    if request.method == "POST":
        query = request.form.get("query")
        result = run_search(query)
    return render_template("index.html", result=result, query=query)

if __name__ == "__main__":
    app.run(debug=True)