from tabulate import tabulate
import mysql.connector;

con = mysql.connector.connect(host='localhost', user='santhosh', password='123098', database='pydb')


class santhosh:
    ID = ""
    NAME = ""
    ROLE = ""

    def insert(self, name, role):
        self.NAME = name
        self.ROLE = role
        res = con.cursor()
        q = "insert into details(NAME,ROLE) values(%s,%s)"
        res.execute(q, (self.NAME, self.ROLE))
        con.commit()
        print("Successfully Inserted!")

    def update(self, id, name, role):
        self.ID = id
        self.NAME = name
        self.ROLE = role
        res = con.cursor()
        q = "update details set NAME=%s, ROLE=%s where ID=%s"
        res.execute(q, (self.NAME, self.ROLE, self.ID))
        con.commit()
        print("Successfully Updated!")

    def delete(self, id):
        self.ID = id
        res = con.cursor()
        q = "delete from details where ID=%s"
        res.execute(q, self.ID)
        con.commit()
        print("Successfully Deleted!")

    def display(self):
        res = con.cursor()
        q = "select * from details"
        res.execute(q)
        fetch = res.fetchall()
        print(tabulate(fetch, headers=['ID', 'NAME', 'ROLE']))


s = santhosh()
while True:
    print("Choices:-----")
    print("1.Insert data")
    print("2.Update data")
    print("3.Delete data")
    print("4.Display data")
    print("5.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        name = input("Enter the name:")
        role = input("Enter the role:")
        s.insert(name, role)
    elif choice == 2:
        id = input("Enter the id:")
        name = input("enter the name:")
        role = input("Enter the role:")
        s.update(id, name, role)
    elif choice == 3:
        id = input("Enter the id:")
        s.delete(id)
    elif choice == 4:
        s.display()
    elif choice == 5:
        break
    else:
        print("Invalid operations")
