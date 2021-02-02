import sqlite3
from User import User


class DBMS:
    def __init__(self,filename: str):
        self.connection = sqlite3.connect(filename)
    
    def create_tables(self):
        c = self.connection.cursor()
        c.execute("""
            CREATE TABLE "users" (
                "user_id" INTEGER NOT NULL,
                "selected_region" VARCHAR(100) NULL DEFAULT NULL,
                "selected_province" VARCHAR(100) NULL DEFAULT NULL,
                "send_notifications" INTEGER NOT NULL DEFAULT '1'
            );
        """)
        self.connection.commit()
        c.close()

    def get_user(self,user_id: str):
        c = self.connection.cursor()
        c.execute("SELECT * FROM users WHERE user_id = ?",user_id)
        result = c.fetchone()
        c.close()
        return User(result[0],result[1],result[2],result[3])

    def insert_user(self,user_id: str):
        c = self.connection.cursor()
        c.execute("INSERT INTO users VALUES (?,?)",user_id,1)
        self.connection.commit()
        c.close()
