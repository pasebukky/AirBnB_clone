from models.engine.file_storage import FileStorage
"""
Desc:
    when the application starts or when the models package is imported,
    a single instance of FileStorage is created.
    This instance is then accessible throughout the application.
    This allows different parts of code to use the same storage system.
"""


storage = FileStorage()
storage.reload()
