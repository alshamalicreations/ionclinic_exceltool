"""
file_service.py

General file utilities.
"""

from pathlib import Path


class FileService:
    """
    Handles common file operations.
    """

    @staticmethod
    def exists(path: str | Path) -> bool:
        return Path(path).exists()

    @staticmethod
    def create_directory(path: str | Path):
        Path(path).mkdir(parents=True, exist_ok=True)