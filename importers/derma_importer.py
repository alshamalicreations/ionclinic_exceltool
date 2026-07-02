"""
derma_importer.py

Importer for Derma Excel workbooks.
"""

from importers.base_importer import BaseImporter


class DermaImporter(BaseImporter):

    def import_data(self):
        print("Importing Derma workbook...")