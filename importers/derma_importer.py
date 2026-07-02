"""
derma_importer.py

Reads patients from a Derma workbook.
"""

from models.patient import Patient
from importers.base_importer import BaseImporter


class DermaImporter(BaseImporter):

    def read_patients(self) -> list[Patient]:

        sheet = self.workbook["Patient"]

        patients: list[Patient] = []

        # Skip header row
        for row in sheet.iter_rows(min_row=2, values_only=True):

            patient = Patient(
                file_number=row[0],
                full_name=row[1] or "",
                full_name_en=row[2] or "",
                phone_number=str(row[3] or ""),
                gender=row[4] or "",
                birth_date=row[5],
            )

            patients.append(patient)

        return patients