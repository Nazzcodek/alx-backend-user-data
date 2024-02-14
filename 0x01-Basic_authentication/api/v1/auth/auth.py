#!/usr/bin/env python3
""" This is the auth module """
from flask import request


class Auth:
    """the auth object instances"""

    def require_auth(self,  path: str, excluded_paths: List[str]) -> bool:
        """required auth method"""
        return False

    def authorization_header(self, request=None) -> str:
        """authorization header method"""
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ method to get current user"""
        if request is None:
            return None
