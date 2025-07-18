from flask import request

from app import app
from model.user_model import User_model

# User model object
model_obj = User_model()


@app.route("/user/signup", methods=["POST"])
def user_signup():
    data = request.get_json()
    model_obj = User_model()
    return model_obj.user_signup_logic(data)


# login routes where we get the post request from the server
@app.route("/user/login", methods=["POST"])
# funtion for login data
def user_login():
    # the that we get from the request will store in data variable
    data = request.get_json()
    # create an instance(object) of User_model
    model_obj = User_model()
    # call the user_login_logic method from User_model and pass the data and return the result
    return model_obj.user_login_logic(data)


@app.route("/user/getall", methods=["POST"])
def user_getall():
    data = request.get_json()
    model_obj = User_model()
    return model_obj.user_getall_logic(data)


# update route, from here data is passed to user_delete_logic to udpdate
@app.route("/user/update", methods=["PUT"])
def user_update():
    data = request.get_json()
    model_obj = User_model()
    return model_obj.user_update_logic(data)


# delete route, from here data is passed to user_delete_logic for logic
@app.route("/user/delete/<int:id>", methods=["DELETE"])
def user_delete(id):
    # data = request.get_json()
    model_obj = User_model()
    return model_obj.user_delete_logic(id)


# fetchall route, to fetchall user in postman
@app.route("/user/fetchall")
def fetchall():
    model_obj = User_model()
    return model_obj.fetch_all()
