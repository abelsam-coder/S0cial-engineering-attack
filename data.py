import sqlite3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
db = sqlite3.connect("database.db")
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS se (email TEXT,pin TEXT)")
db.commit()








