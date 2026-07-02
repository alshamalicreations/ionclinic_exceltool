"""
patient.py

Represents a patient independently of any
Excel workbook or clinic system.
"""

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(slots=True)
class Patient:
    """
    Represents one patient.
    """

    file_number: int

    full_name: str

    full_name_en: str

    phone_number: str

    gender: str

    birth_date: Optional[date]