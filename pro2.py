import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='manager',database='electronic_shop')
if conn.is_connected:
    print('ELECTRONIC SHOP SYSTEM')
    print('1.items')
    print('2.labours')
    print('3.customers')
    print('4.sales')
    print('5.expenses')
cur=conn.cursor()
cur.execute('create table items(s_no int(10),item varchar(50) primary key,availability_of_item int(10),price int(7))')
conn.commit()            

