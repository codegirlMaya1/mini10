import sqlite3
connect1=sqlite3.connect('members-sqlite.db')
connect1.commit()
cursor1=connect1.cursor()
#cursor1.execute(''' CREATE TABLE member
 #(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INT)               
 #               ''')

membersToinsert=[
    ('1', " Lori Lewis", '32'),
    ('2', " Jamie Jones", '43'),
    ('3', " Carl Crawford", '54')
]
cursor1.executemany('''
                INSERT INTO member(id, name, age)           
                VALUES (?,?,?) ''', membersToinsert)

cursor1.execute(" SELECT * FROM member")
print(cursor1.fetchall())
cursor1.execute(" SELECT name FROM member")
print(cursor1.fetchall())
