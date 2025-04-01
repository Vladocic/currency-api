import sqlite3
import config


def create_table():
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS currencies (
            num_code TEXT,
            char_code TEXT,
            unit INTEGER,
            name TEXT,
            rate REAL
        )
    ''')
    conn.commit()
    conn.close()

