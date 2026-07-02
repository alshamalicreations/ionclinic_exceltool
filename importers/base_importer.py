"""
base_importer.py

Defines the contract that every importer must follow.
"""

from abc import ABC, abstractmethod

from openpyxl.workbook.workbook import Workbook

from models.patient import Patient


class BaseImporter(ABC):
    """
    Base class for all importers.
    """

    def __init__(self, workbook: Workbook):
        self.workbook = workbook

    @abstractmethod
    def read_patients(self) -> list[Patient]:
        """
        Read all patients from the workbook.
        """
        raise NotImplementedError