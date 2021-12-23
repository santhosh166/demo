import pymongo

class santhosh:
    connection = pymongo.MongoClient("mongodb://localhost:27017/")

    def valid(self):
        if self.connection:return True
        else:return False

    def Insert(self,db_name,collection_name,student_id,name,department):
         data={'stud_id':student_id,'name':name,'dept':department}
         self.connection[db_name][collection_name].insert_one(data)
         print("Inserted Successfully...!")
        
    def View(self,db_name,collection_name):
        for info in self.connection[db_name][collection_name].find():
           print("Student_Id:{}  Student_Name:{}  Student_Department:{}".format(info['stud_id'],info['name'],info['dept']))
        
    
    def Update(self,db_name,collection_name,stud_id):
           name=input("Enter the  new name:")
           dep=input("Enter the new dep name:")
           self.connection[db_name][collection_name].update_one({'stud_id':stud_id},{"$set":{'name':name,'dep':dep}})
           print("Updated Successfully....!")
    
    def Delete(self,db_name,collection_name,stud_id):
        self.connection[db_name][collection_name].delete_one({'stud_id':stud_id})
        print("Deleted Successfully..!")

s=santhosh()
if s.valid():
    while True:
        print("-------------------------------Choices---------------------------------------------------------")
        print("1.Insert\n2.View\n3.Update\n4.Delete\n0.Exit")
        n=int(input("Enter Your Choices:"))
        if n==0:
            print("\t\t\t\tThank You!\n") 
            break
        elif n==1:
            stud_id=int(input("Enter the Student Id:"))
            stud_name=input("Enter the Name:")
            dep=input("Enter the Department Name:")
            s.Insert('demo','stud',stud_id,stud_name,dep)
        elif n==2:
            s.View('demo','stud')
        elif n==3:
            stud_id=int(input("Enter the Student Id:"))
            s.Update('demo','stud',stud_id)
        elif n==4:
             stud_id=int(input("Enter the Student Id:"))
             s.Delete('demo','stud',stud_id)
        else:print("\t\t\t\tInvalid\n")
else:print("Connection Error!")
