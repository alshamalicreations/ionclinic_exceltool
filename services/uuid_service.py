"""
uuid_service.py

Generates unique identifiers.
"""

import uuid


class UUIDService:
    """
    UUID generation service.
    """

    @staticmethod
    def generate() -> str:
        return str(uuid.uuid4())