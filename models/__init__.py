#!/usr/bin/python3
"""Initialize the models package."""

from models.engine.file_storage import FileStorage


# Create a single storage instance for the whole application
storage = FileStorage()
storage.reload()
