import mysql.connector

conn = mysql.connector.connect(user="root",password="root",database="test")
#cursor = conn.cursor()
#cursor.execute("create table user (id varchar(20) PRIMARY  KEY , name VARCHAR (30) )")
#cursor.execute("insert into user(id,name) VALUES (%s,%s)",['1','mike'])
#cursor.rowcount
#conn.commit()
#cursor.close()
cursor = conn.cursor()
cursor.execute("select * from user where id = %s",("1",))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()


