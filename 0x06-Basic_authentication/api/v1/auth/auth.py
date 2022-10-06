#!/usr/bin/env python3
"""Module of Auth"""
from typing import TypeVar, List
from flask import request


class Auth:
    """Class Auth"""

    def __init__(self) -> None:
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require function"""
        return False

    def authorization_header(self, request=None) -> str:
        """authorization_header"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user"""
        return request
