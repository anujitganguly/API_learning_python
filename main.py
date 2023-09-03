# can be run in windows terminal using "python main.py"
from flask import Flask, request, jsonify

# creating a Flask application called app
app = Flask(__name__)

# creating a route
# adding decorator @app so that we can access the route and "/" means default route
# @app.route("/") this is a demo route for testing, it is advised to run it to verify the installations in
# def home():
#   return "Home"

# actual route to be used in the project
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "User One",
        "email": "userone@mail.com"
    }

# Query parameter: whenever we are accessing a route, we can access some extra value eg.- "get-user/123?extra = hello world"
    extra = request.args.get("extra")
    if extra:       # checking if any extra value exists
        user_data["extra"] = extra

    return jsonify(user_data), 200      # 200 is server status code for success

# Creating a post route
@app.route("/create-user", methods = ["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201


# running the flask application
if __name__ == "__main__":
    app.run(debug=True)
