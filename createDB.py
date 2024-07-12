import sqlite3

conn = sqlite3.connect('testData.db')
cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS USERS(mobile TEXT UNIQUE, email TEXT UNIQUE, name TEXT)"
)

cursor.execute(
    "CREATE TABLE IF NOT EXISTS DISCUSSIONS(usermobile TEXT,textfield TEXT, imagefield BLOB, hashtags TEXT, createdon DATE)"
)

cursor.execute()
conn.commit()
conn.close()