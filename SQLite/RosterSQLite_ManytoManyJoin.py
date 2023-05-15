"""Code for creating database and joining tables using many-to-many relationship. This code is
similar to the previous "SQLite_emailsplitter_counter.py" code. The only difference is that we
 will be creating a seperate table which will have attributes of indiviual table's foreign keys.
 (reference: https://www.tutorialsteacher.com/sqlserver/tables-relations)  """

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS ROLE;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE ROLE (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name  TEXT UNIQUE
); 

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role_id        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title, role))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Role (name)
            VALUES ( ? )''', (role,))
    cur.execute('SELECT id FROM Role WHERE name = ? ', (role,))
    role_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role_id) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

    conn.commit()

#SQL code to join tables
"""SELECT User.name,Course.title, Member.role_id FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;"""

#SQL code to concat and convert table attributes to hexadecimal numbers
"""SELECT 'XYZZY' || hex(User.name || Course.title || Member.role_id ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;"""

#Python code to convert hex to string (for verification)
"""def hex_to_string(hex):
    if hex[:2] == '0x':
        hex = hex[2:]
    string_value = bytes.fromhex(hex).decode('utf-8')
    return string_value


hex_value = '0x41616D696E6168736933313030'
string = 'This is just a ' + hex_to_string('41616D696E6168736933313030')

print(string)"""