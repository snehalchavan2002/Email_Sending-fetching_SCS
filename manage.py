import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emailer.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
      


if __name__ == '__main__':
    main()
