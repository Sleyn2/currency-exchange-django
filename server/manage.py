#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from server.yahooData import fetch

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django"
        ) from exc
    execute_from_command_line(sys.argv)
    fetch()


if __name__ == '__main__':
    main()
