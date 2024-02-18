#!/usr/bin/env python3
"""basic authentication module"""
from api.v1.auth.auth import Auth


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
