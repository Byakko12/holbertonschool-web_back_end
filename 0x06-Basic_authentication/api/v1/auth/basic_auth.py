#!/usr/bin/env python3
"""BasicAuth Model"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth class """

    def extract_base64_authorization_header(self, authorization_header: str) \
            -> str:
        """Basic - Base64 part"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        base = authorization_header.split(' ')
        return base[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Returns decoded value of Base64 str """

        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None
