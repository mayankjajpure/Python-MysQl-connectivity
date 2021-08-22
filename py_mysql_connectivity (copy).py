import mysql.connector

try:
    conn=mysql.connector.connect(user='root',password='Mayank@680',database='pydb')
    if conn.is_connected():print('connection created success fully')
except:
    print('connection not created ')
# TABLE OVERVIEW
# sql='create table records(id int auto_increment Primary key,name varchar(25),phone intt)'



def insert():
    nm=input('Enter the name of record  :')
    ph=int(input('Enter phone number  :'))
    #  insert into records(name,phone) values("MAYANK",89089089)
    sql='insert into records(name,phone) values(%s,%s)'
    params=(nm,ph)
    myc=conn.cursor()
  
    try:
        myc.execute(sql,params)
        conn.commit()
        print(myc.rowcount,"rows changed")
        print("insertion succesfull")
    except:
        conn.rollback() 
        print('cant insert value')
    myc.close()

def display():
    myc=conn.cursor()
    sql='select * from records'
    try:
        myc.execute(sql)
        r=myc.fetchone()
        print("id | name   | phn")
        while r:
            print(r[0]," |",r[1],"|",r[2])
            r=myc.fetchone()
    except:
        print("error  in fetching records")

    myc.close()

def update(id):
    chng=id
    myc=conn.cursor(prepared=True)
    sql='update records set name=?,phone=? where id=?'
    nm=input("enter name : ")
    ph=int(input("enter phn number: "))
    param=(nm,ph,chng)
    try:
        myc.execute(sql,param)
        conn.commit()
        print("updated successfully")
    except:
        print("error in updating entity")

    # pass
def delete(id):
    myc=conn.cursor(prepared=True)
    sql='delete from records where id=?'
    try:
        myc.execute(sql,(id,))
        conn.commit()
        print("DELETED ")
    except:
        conn.rollback()
        print("error in deletion  ")

        
print("Hello user  welcome to your database")

while True:
    print()
    print("press 0 to exit ")
    print("press 1 to insert record in table")
    print("press 2 to show recordas of your table")
    print("press 3 to update record in table")
    print("press 4 to delete record in table")
    
    user_input=int(input())

    if user_input==0:
        print()
        print("EXITING FROM DATABASE")

        break

    elif user_input==1:
        insert()
        
    elif user_input==2:
        display()
        
    elif user_input==3:
        display()
        id=int(input("ENTER ID YOU WANT TO APLLLY UPDATE :  "))
        update(id)
        
    elif user_input==4:
        id=int(input("ENTER ID YOU WANT TO APLLLY DELITION :  "))
        delete(id)

    else:print('invalid input ')

conn.close()