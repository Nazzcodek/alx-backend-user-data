#!/usr/bin/env python3
""" This is the auth module """
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """the auth object instances"""

    def require_auth(self,  path: str, excluded_paths: List[str]) -> bool:
        """required auth method"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        for excluded_path in excluded_paths:
            # Normalize paths to ensure they end with '/'
            if not path.endswith('/'):
                path += '/'
            if not excluded_path.endswith('/'):
                excluded_path += '/'

            if path == excluded_path:
                return False

            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """authorization header method"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ method to get current user"""
        if request is None:
            return None

    def session_cookie(self, request=None):
        """session cookies"""
        if request is None:
            return None

        SESSION_NAME = os.environ('SESSION_NAME')
        if SESSION_NAME is None:
            return None

        cookies = request.cookies.get(SESSION_NAME)
        return cookies

