"""
migration_engine.py

Coordinates the migration workflow.
"""

from engine.source_detector import SourceDetector
from engine.workbook_analyzer import WorkbookAnalyzer
from importers.derma_importer import DermaImporter
from models.migration_request import MigrationRequest
from services.workbook_service import WorkbookService


class MigrationEngine:

    def __init__(self):

        self.workbook_service = WorkbookService()
        self.analyzer = WorkbookAnalyzer()
        self.detector = SourceDetector()

    def run(self, request: MigrationRequest):

        print()

        print("Loading source workbook...")
        source = self.workbook_service.load(request.source_file)
        print("✓ Source workbook loaded")

        print()

        print("Loading template workbook...")
        template = self.workbook_service.load(request.template_file)
        print("✓ Template workbook loaded")

        print()

        workbook_type = self.detector.detect(source)

        print(f"Detected workbook: {workbook_type}")

        print()

        if workbook_type == "DERMA":

            importer = DermaImporter(source)

            patients = importer.read_patients()

            print(f"✓ Imported {len(patients)} patients")

            print()

            print("First five patients:")

            print("-" * 60)

            for patient in patients[:5]:

                print(
                    patient.file_number,
                    "|",
                    patient.full_name,
                    "|",
                    patient.phone_number,
                )

        else:

            print("Unsupported workbook.")