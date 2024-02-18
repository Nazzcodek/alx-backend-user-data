#!/usr/bin/env python3
"""session db module"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """session db auth object instances"""

    def create_session(self, user_id: str=None):
        """this is create session method"""
        # Create a new session ID
        session_id = self.generate_session_id()
        
        # Create a new UserSession instance and store it in the database
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()

        return session_id

    def user_id_for_session_id(self, session_id: str=None):
        """user id for session id method"""
        # Retrieve the UserSession from the database based on the session_id
        user_session = UserSession.query.filter_by(session_id=session_id).first()
        
        if user_session:
            return user_session.user_id
        else:
            return None

    def destroy_session(self, request=None):
        """destroy method"""
        # Retrieve the session ID from the cookie
        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        # Delete the UserSession from the database
        user_session = UserSession.query.filter_by(session_id=session_id).first()
        if user_session:
            user_session.delete()
            return True
        else:
            return False
