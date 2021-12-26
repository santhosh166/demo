import requests

import pymongo

class san:

    url="https://fruityvice.com/api/fruit/all"
    connection = pymongo.MongoClient("mongodb://localhost:27017/")

    def url_json(self):
        response=requests.get(self.url)
        data=response.json()
        return data

    def collections(self,db,col):
        if self.connection:
            db_name=self.connection[db]
            col_name=db_name[col]
    
    def Insert(self,db,col,genus,name,id,family,order,nutritions):
        if self.collections:
            data = {'genus':genus,'name': name, 'id': id,'family': family, 'order': order,'nutritions':nutritions}
            self.connection[db][col].insert_one(data)
            print("SUCCESS : Data Inserted !")

    
s=san()
s.collections('demo','datas')
details=s.url_json()
print(details[0])
for i in details:
    s.Insert('demo','datas',i['genus'],i['name'],i['id'],i['family'],i['order'],i['nutritions'])
    
