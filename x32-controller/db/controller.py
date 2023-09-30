import os, utils, sqlite3


class Controller:
    def __init__(self) -> None:
        # check for tables
        
        if not os.path.exists('x32-controller/assets/db'):
            os.makedirs('x32-controller/assets/db')
            utils.log.warn('database directory does not exist, its been created in /assets/db')

        conn = sqlite3.connect('x32-controller/assets/db/main.db')
        cursor = conn.cursor()

        try:
            cursor.execute('DROP TABLE users')
            cursor.execute('DROP TABLE base')
            cursor.execute('DROP TABLE sessions')
        except:
            pass

        cursor.execute('''
            CREATE TABLE "base" (
                "id" INTEGER UNIQUE,
                "name" TEXT NOT NULL,
                "colour" INTEGER,
                "source" INTEGER,
                "link" INTEGER,
                "delay_on" INTEGER,
                "delay_time" REAL,
                "gain" REAL,
                "mute" INTEGER,
                PRIMARY KEY("id" AUTOINCREMENT)
            )
        ''')

        cursor.execute('''
            CREATE TABLE "sessions" (
                "id" INTEGER UNIQUE,
                "name" TEXT NOT NULL,
                "created_at" TEXT,
                "updated_at" TEXT,
                
                PRIMARY KEY("id" AUTOINCREMENT)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE "users" (
                "id" INTEGER UNIQUE,
                "name" TEXT NOT NULL,
                "password" TEXT,
                "sessions_id" INTEGER,
                PRIMARY KEY ("id" AUTOINCREMENT),
                FOREIGN KEY ("sessions_id")
                    REFERENCES "sessions" ("id")
            )
        ''')