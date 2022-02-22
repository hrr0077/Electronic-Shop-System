import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='manager',database='electronic_shop')
cur=conn.cursor()
cur.execute('create table labours(name varchar(25) primary key,age int(10),place varchar(25),department varchar(25))')
cur.execute('create table customer(customer_name varchar(50) primary key,age int(10),place varchar(25),item_bought varchar(25))')
conn.commit() 
