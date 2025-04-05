from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask demo!"


@app.route("/items/<int:item_id>")
def get_item(item_id):
    return f"You requested item {item_id}"


if __name__ == "__main__":
    app.run(debug=True)
