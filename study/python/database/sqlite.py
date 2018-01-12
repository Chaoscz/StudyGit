import os,sqlite3

db_file = os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file) :
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor();
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low,high):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor();
    try:
        cursor.execute('select name from user where score >=? and score<= ?',(low,high))
        values = cursor.fetchall()
        return [x[0] for x in values]
    except Exception as e :
        print(e)
    finally:
        cursor.close()
        conn.close()


v = get_score_in(60,95)

print(v)


