"""
main.py

Application entry point.
"""

from controllers.migration_controller import MigrationController


def main():
    print("=" * 50)
    print("IonClinic Excel Tool")
    print("=" * 50)

    controller = MigrationController()
    controller.migrate()


if __name__ == "__main__":
    main()