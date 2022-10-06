#!/usr/bin/env python3
from typing import TypeVar, List
from flask import request


class Auth:
    """Class Auth"""

    def require(self, path: str, excluded_paths: List[str]) -> bool:
        """Require function"""
        return False

    def authorization_header(self, request: None) -> str:
        """authorization_header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user"""
        return None
