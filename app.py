from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")

@app.get("/")
def paintings():
    return render_template('paintings.html')

if __name__ == "__main__":
    app.run(debug=True)
