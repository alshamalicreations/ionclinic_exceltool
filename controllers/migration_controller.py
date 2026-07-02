"""
migration_controller.py

Receives commands from the GUI and starts the migration.
"""

from engine.migration_engine import MigrationEngine


class MigrationController:

    def __init__(self):
        self.engine = MigrationEngine()

    def migrate(self):
        self.engine.run()