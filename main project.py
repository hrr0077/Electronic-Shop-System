import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='manager',database='electronic_shop')
cur=conn.cursor()
if conn.is_connected:
    print('                                              ELECTRONIC SHOP SYSTEM')
    
    
    print('                                             1.admin')
    print('                                              2.customers')
choice=int(input('                               enter the choice:'))
if choice==1:
    pw='whysoserious'
    passwrd=input('enter the password:')
    print('                                             1.entry for item')
    print('                                             2.entry for labour')
    print('                                             3.entry for customer')
    choose=int(input('enter the choice for entry:'))
    if choose==1:
        item=input('enter the name of item:')
        availability=int(input('availability of the item:'))
        price=int(input('enter the price of item in rupees:'))
        cur.execute("insert into items values('" + item + "'," + str(availability) + "," + str(price) + ")")
        print('entry succesful')
        conn.commit()
    elif choose==2:
        name=input('enter the name of labour:')
        age=int(input('enter the age:'))
        place=input('enter the place of the labour:')
        dept=input('enter the name of the department:')
        cur.execute("insert into labours values('" + name + "','" + str(age) + "','" + place + "','" + dept + "')")
        print('entry sucessful')
        conn.commit()
    elif choose==3:
        name=input('enter the name of the customer:')
        age=int(input('enter the age:'))
        place=input('enter the place of the customer:')
        item=input('enter the item bought:')
        cur.execute("insert into customer values('" + name + "','" + str(age) + "','" + place + "','" + item + "')")
        print('entry sucessful')
        conn.commit()
elif choice==2:
    print('                                             1.Display of item list')
    print('                                             2.Display of labour list')
    print('                                             3.Display of customer list')
    ch=int(input('enter the choice'))
    if ch==1:
           print()
           cur.execute("select * from items")
           dataa=cur.fetchall()
           print('list of items')
           for row in dataa:
               print()
               print('item:',row[0])
               print('availablity:',row[1])
               print('price:',row[2])
    elif ch==2:
        print()
        cur.execute("select * from labours")
        data=cur.fetchall()
        print('list of labours')
        for row in data:
            print()
            print('name:',row[0])
            print('age:',row[1])
            print('place:',row[2])
            print('department:',row[3])
    elif ch==3:
        print()
        cur.execute("select * from customer")
        datas=cur.fetchall()
        print('list of customer')
        for row in datas:
            print()
            print('name:',row[0])
            print('age:',row[1])
            print('place:',row[2])
            print('item bought:',row[3])        
