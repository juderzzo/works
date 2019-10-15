import sqlite3

db = sqlite3.connect("database.db")
c = db.cursor()

# create the average table
c.execute("DROP TABLE IF EXISTS stu_avg")
c.execute("CREATE TABLE IF NOT EXISTS stu_avg (id INTEGER PRIMARY KEY, student_id INTEGER, average FLOAT)")


# get a student's average based on their id
def get_student_average(id):
    r = c.execute("SELECT mark FROM courses WHERE other_id = " + str(id)).fetchall()
    s = 0
    for i in r:
        s += i[0]
    return s / len(r)


# get all student ids
all_student_ids = c.execute("SELECT id FROM students").fetchall()

for student_id in all_student_ids:
    student_id = student_id[0]
    avg = get_student_average(student_id)
    c.execute("INSERT INTO stu_avg (student_id, average) VALUES (" + str(student_id) + ", " + str(avg) + ")")


db.commit()
db.close()

if __name__ == '__main__':
    pass
