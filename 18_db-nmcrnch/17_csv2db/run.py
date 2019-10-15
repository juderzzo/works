import sqlite3
import csv

db = sqlite3.connect("database.db")
c = db.cursor()

# make tables
c.execute("DROP TABLE IF EXISTS students")
c.execute("DROP TABLE IF EXISTS courses")
c.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name INTEGER, age STRING)")
c.execute("CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY, code STRING, mark INTEGER, other_id INTEGER)")


with open("courses.csv") as file:
    next(file)
    reader = csv.reader(file)
    for line in reader:
        cmd = "INSERT INTO courses (code, mark, other_id) VALUES (\"" + line[0] + "\"," + line[1] + "," + line[2] + ")"
        c.execute(cmd)

with open("students.csv") as file:
    next(file)
    reader = csv.reader(file)
    for line in reader:
        cmd = "INSERT INTO students (name, age, id) VALUES (\"" + line[0] + "\"," + line[1] + "," + line[2] + ")"
        c.execute(cmd)

db.commit()
db.close()


if __name__ == '__main__':
    pass
