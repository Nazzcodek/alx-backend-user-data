#!/usr/bin/env python3
"""this is encryption module"""
import bcrypt as b


def hash_password(password: str) -> bytes:
    """this is a hash password method"""
    encrypt = b.hashpw(password.encode(), b.gensalt())
    return encrypt


def is_valid(hash_pwd: bytes, password: str) -> bool:
    """this method check if passowrd is valid"""
    decrypt = b.checkpw(password.encode(), hash_pwd)
    return decrypt
