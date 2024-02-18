#!/usr/bin/env python3
"""basic authentication module"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar, Optional

user = TypeVar('User')


class BasicAuth(Auth):
    """the basic auth object instance"""

    def extract_base64_authorization_header(
                    self, authorization_header: str) -> str:
        """base64 auth header"""
        if (
            authorization_header is None
            or not isinstance(authorization_header, str)
        ):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
                    self, base64_authorization_header: str) -> str:
        """Decodes the Base64 part of the Authorization header"""
        if (
            base64_authorization_header is None
            or not isinstance(base64_authorization_header, str)
        ):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (TypeError, ValueError):
            return None

    def extract_user_credentials(
                    self,
                    decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts the user email and password
        from the Base64 decoded value.
        """
        if (
            decoded_base64_authorization_header is None
            or not isinstance(decoded_base64_authorization_header, str)
        ):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':',  1)
        return email, password

    def user_object_from_credentials(
                    self, user_email: str,
                    user_pwd: str) -> Optional[User]:
        """Returns the User instance based on email and password."""
        if (
            user_email is None
            or not isinstance(user_email, str)
            or user_pwd is None
            or not isinstance(user_pwd, str)
        ):
            return None

        # Search for the user in the database using the email
        users = User.search(attributes={'email': user_email})
        if not users:
            # No user found with the given email
            return None

        # Assuming the search returns a list of users, get the first one
        user = users[0]

        # Verify the password
        if not user.is_valid_password(user_pwd):
            # Password does not match
            return None

        # Return the user instance if the email and password are valid
        return user
