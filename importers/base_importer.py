"""
base_importer.py

Defines the interface every importer must implement.
"""

from abc import ABC, abstractmethod


class BaseImporter(ABC):

    @abstractmethod
    def import_data(self):
        pass