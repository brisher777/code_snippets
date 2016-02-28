import sqlite3


class DBContextManager():
    """Context Manager for sqlite3 database interaction."""
    def __init__(self, db_name):
        self._db_name = db_name
        self._conn = None

    def __enter__(self):
        self._conn = sqlite3.connect(self._db_name)
        self._conn.text_factory = str
        return self._conn

    def __exit__(self, type, value, traceback):
        if type:
            self._conn.rollback()
            print('Exception: {}'.format(value))
        self._conn.commit()
        self._conn.close()
