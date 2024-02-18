#!/usr/bin/env python3
"""sessiobn authentication module"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """this is the session authentication object instances"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Session creation method"""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user id for session id"""
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Retrieves the User instance based on a cookie value."""
        if request is None:
            return None

        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        user = User.get(user_id)
        if user is None:
            return None

        return user

    def destroy_session(self, request=None):
        """Deletes the user session / logout."""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]

        return True
