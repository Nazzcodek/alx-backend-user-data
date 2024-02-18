#!/usr/bin/env python3
"""basic authentication module"""
from api.v1.auth.auth import Auth
import base64


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
        """Decodes the Base64 part of the Authorization header for Basic Authentication."""
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
