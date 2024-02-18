#!/usr/bin/env python3
"""session route"""
from flask import Flask, request, jsonify, make_response
import os
from api.v1.models.user import User
from api.v1.auth.auth import Auth


@app.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handles the login process for session authentication."""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}),  400
    if not password:
        return jsonify({"error": "password missing"}),  400

    # Search for the user in the database using the email
    users = User.search(attributes={'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}),  404

    # Getting the first user
    user = users[0]

    # Verify the password
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}),  401

    # Create a session ID for the user
    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    # Set the session cookie in the response
    response = make_response(jsonify(user.to_json()))
    response.set_cookie(os.environ.get('SESSION_NAME', 'session_id'), session_id)

    return response
