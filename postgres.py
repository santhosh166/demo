import psycopg2
from tabulate import tabulate

class san:
    con=psycopg2.connect(host='localhost', user='postgres', password='123098', database='just')

    def connection(self):

        if self.con:
             return True
        else:
            return False 

    def insert(self, id, name, dept):
        
        res = self.con.cursor()
        q = "insert into details(id,name,dept) values(%s,%s,%s)"
        res.execute(q, (id,name,dept))
        self.con.commit()
        print("Successfully Inserted!")
        print("="*100)

    def update(self,id,name,dept):

        res=self.con.cursor()
        q="update details set name=%s,dept=%s where id=%s"
        res.execute(q,(name,dept,id))
        self.con.commit()
        print("Updated Successfully!")

    def delete(self,id):
        res=self.con.cursor()
        q="delete from details where id=%s"
        res.execute(q,[id])
        self.con.commit()
        print("Deleted Successfully!")

    def display(self,c):

        res=self.con.cursor()

        if c=='all':
            q="select * from details"
            res.execute(q)
            fetch=res.fetchall()
            print(tabulate(fetch,headers=['id','name','dept']))
        else:
            q="select * from details where id=%s"
            res.execute(q,[c])
            fetch=res.fetchall()
            print(fetch)
            print(tabulate(fetch,headers=['id','name','dept']))
        



#first create database name as just and create table name as details then execute this
s=san()
if s.connection:

    while True:
        print("--------------------Choices:-----------------")
        print("1.Insert data")
        print("2.Update data By Id")
        print("3.Delete data By Id")
        print("4.Display data")
        print("5.Exit")

        choice = int(input("Enter your choice:"))

        if choice==1:
            id=int(input("Enter the id:"))
            name=input("Enter the name:")
            dept=input("Enter the department:")
            s.insert(id,name,dept)
            print("="*100)
        
        elif choice==2:
            id=int(input("Enter the id:"))
            name=input("Enter the new name:")
            dept=input("Enter the new dept name:")
            s.update(id,name,dept)
            print("="*100)

        elif choice==3:
            id =int(input("Enter the id:"))
            s.delete(id)
            print("="*100)

        elif choice==4:
            print('if you want to see all details type "all" other wise enter the "id" to see certain details')
            c=input("Enter:")
            if c.isnumeric():
                i=int(c)
                c=i
            s.display(c)
            print("="*100)
        
        elif choice==5:
            print("\t\t\t\t\t\tThank You!")
            print("="*100)
            break

        else:
            print("Invalid Input!")

else:
    print("Connection Error try again!")
