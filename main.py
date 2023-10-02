from flask import Flask, request, jsonify

app = Flask(__name__)

# <user_id> will change depending on the value of user_id passed as argument
@app.route("/get-user/<user_id>") # this is a get route (GET is default method)
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    # we can pass query parameters to the route
    # ex: "get-user/123?extra=hello world"
    # here, the question mark indicates an extra query parameter which is extra
    extra = request.args.get("extra") # and here's how you can retrieve it from the route that was passed
    if extra:
        user_data["extra"] = extra

    # jsonify the dict to parse it, status code 200 is default for success
    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    # if request.method == "POST" # if more than one methods specified

    data = request.get_json()

    return jsonify(data), 201 # 201 is successful POST request

"""
To test the API you can use several methods, postman is one of them
"""

"""
GET # retrieve values from the server
POST # create a resource
PUT # upd a resource
DELETE # delete data

Are different methods for the routes
"""

if __name__ == "__main__":
    app.run(debug=True)