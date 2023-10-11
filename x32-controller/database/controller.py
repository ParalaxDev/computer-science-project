import os, utils, sqlite3


class Controller:
    def __init__(self) -> None:
        # check for tables
        
        if not os.path.exists('x32-controller/assets/db'):
            os.makedirs('x32-controller/assets/db')
            utils.log.warn('database directory does not exist, its been created in /assets/db')

        self.conn = sqlite3.connect('x32-controller/assets/db/main.db')
        self.cursor = self.conn.cursor()

        # try:
        #     self.cursor.execute('DROP TABLE users')
        #     self.cursor.execute('DROP TABLE base')
        #     self.cursor.execute('DROP TABLE saves')
        #     self.cursor.execute('DROP TABLE channel')
        # except:
        #     pass

        # self.cursor.execute('''
        #     CREATE TABLE "base" (
        #         "id" INTEGER UNIQUE,
        #         "name" TEXT NOT NULL,
        #         "colour" INTEGER,
        #         "source" INTEGER,
        #         "link" INTEGER,
        #         "delay_on" INTEGER,
        #         "delay_time" REAL,
        #         "gate_on" INTEGER,
        #         "gate_thresh" REAL,
        #         "gate_range" REAL,
        #         "dyn_on" INTEGER,
        #         "dyn_thresh" REAL,
        #         "dyn_ratio" REAL,
        #         "eq_on" INTEGER,
        #         "eq_1_type" INTEGER,
        #         "eq_1_f" REAL,
        #         "eq_1_g" REAL,
        #         "eq_1_q" REAL,
        #         "eq_2_type" INTEGER,
        #         "eq_2_f" REAL,
        #         "eq_2_g" REAL,
        #         "eq_2_q" REAL,
        #         "eq_3_type" INTEGER,
        #         "eq_3_f" REAL,
        #         "eq_3_g" REAL,
        #         "eq_3_q" REAL,
        #         "eq_4_type" INTEGER,
        #         "eq_4_f" REAL,
        #         "eq_4_g" REAL,
        #         "eq_4_q" REAL,
        #         "gain" REAL,
        #         "mute" INTEGER,
        #         "pan" REAL,
        #         PRIMARY KEY("id" AUTOINCREMENT)
        #     )
        # ''')

        # self.cursor.execute('''
        #     CREATE TABLE "channel" (
        #         "id" INTEGER UNIQUE,
        #         "base_id" INTEGER,
        #         "headamp_source" INTEGER,
        #         "headamp_gain" REAL,
        #         "hp_on" INTEGER,
        #         "hp_freq" REAL,
        #         "phantom" INTEGER,
        #         PRIMARY KEY("id" AUTOINCREMENT)
        #         FOREIGN KEY ("base_id")
        #             REFERENCES "base" ("id")
        #     )
        # ''')

        # self.cursor.execute('''
        #     CREATE TABLE "saves" (
        #         "id" INTEGER UNIQUE,
        #         "name" TEXT NOT NULL,
        #         "created_at" TEXT,
        #         "updated_at" TEXT,
        #         PRIMARY KEY("id" AUTOINCREMENT)
        #     )
        # ''')
        
        # self.cursor.execute('''
        #     CREATE TABLE "users" (
        #         "id" INTEGER UNIQUE,
        #         "name" TEXT NOT NULL,
        #         "hashed_password" TEXT,
        #         "saves_id" INTEGER,
        #         PRIMARY KEY ("id" AUTOINCREMENT),
        #         FOREIGN KEY ("saves_id")
        #             REFERENCES "saves" ("id")
        #     )
        # ''')

    def execute(self, sql):
        try:
            val = self.cursor.execute(sql)
            self.conn.commit()
            return val
        except Exception as e:
            utils.log.error(f'Failed to execute SQL: {e}')