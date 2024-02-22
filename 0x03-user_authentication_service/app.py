#!/usr/bin/env python3
from flask import Flask, jsonify
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def msg() -> str:
    """message method"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users' method['POST'])
def users() -> str:
    '''route to register new user'''
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    msg = {"email": email, "message": "user created"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
