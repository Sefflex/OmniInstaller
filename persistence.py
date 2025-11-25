# persistence.py
import sqlite3
import os
from datetime import datetime

DB_NAME = "apps.db"

class MemoryBank:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.init_db()

    def init_db(self):
        """Veritabanını ve tabloyu oluşturur."""
        self.conn = sqlite3.connect(DB_NAME, check_same_thread=False)
        self.cursor = self.conn.cursor()
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS apps (
                app_id TEXT PRIMARY KEY,
                name TEXT,
                version TEXT,
                status TEXT,
                install_date TEXT
            )
        ''')
        self.conn.commit()

    def get_app_status(self, app_id):
        """Bir uygulamanın durumunu döndürür."""
        self.cursor.execute("SELECT status FROM apps WHERE app_id = ?", (app_id,))
        result = self.cursor.fetchone()
        return result[0] if result else "not_installed"

    def update_app_status(self, app_id, name, status, version="1.0"):
        """Uygulama durumunu günceller."""
        install_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Önce var mı kontrol et
        self.cursor.execute("SELECT app_id FROM apps WHERE app_id = ?", (app_id,))
        if self.cursor.fetchone():
            self.cursor.execute('''
                UPDATE apps 
                SET status = ?, version = ?, install_date = ? 
                WHERE app_id = ?
            ''', (status, version, install_date, app_id))
        else:
            self.cursor.execute('''
                INSERT INTO apps (app_id, name, version, status, install_date)
                VALUES (?, ?, ?, ?, ?)
            ''', (app_id, name, version, status, install_date))
        
        self.conn.commit()

    def get_installed_apps(self):
        """Yüklü uygulamaları listeler."""
        self.cursor.execute("SELECT * FROM apps WHERE status = 'installed'")
        return self.cursor.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()
