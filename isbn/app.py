from flask import Flask
import requests

app = Flask(__name__)


# route decorator, can have multiple routes stacked above the method home()
@app.route('/')
def home():
    return "Hello"


@app.route("/book/<isbn>")
def get_author(isbn):
    try:
        res = requests.get(f"https://openlibrary.org/isbn/{isbn}.json")
        if res.status_code == 200:
            return {"message": res.json()}
        elif res.status_code == 404:
            return {"message": "Something went wrong"}, 404
    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        return {"error": str(e)}, 500

@app.route("/hello/<name>")
def hello(name):
    return f"hello, {name}"

# flask --app app --debug run
# or
""" if __name__ == "__main__":
    app.run(debug=True) """
