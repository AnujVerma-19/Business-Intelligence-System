from flask import Flask, render_template
from routes import register_routes

app = Flask(
    __name__,
    template_folder="../Frontend/templates",
    static_folder="static"
)

app.secret_key = "blinkit_secret_key"

@app.route("/")
def home():
    return render_template("index.html")

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)