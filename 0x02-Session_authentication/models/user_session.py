#!/usr/bin/env python3
"""session model"""
from models.base import Base


class UserSession(Base):
    def __init__(self, *args, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
