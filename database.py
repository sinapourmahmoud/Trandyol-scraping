import sqlite3
class Database():
    _instance=None

    def __new__(cls,db_path=-"app.db"):
        if not cls._instance:
            cls._instance=super(Database,cls).__new__(cls)
            cls._instance.init_instance(db_path)
        return cls._instance
    def init_instance(self,db_path):
        self.connection=sqlite3.connect(db_path)
        self.cursor=self.connection.cursor()
    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()
        Database._instance = None

    

    