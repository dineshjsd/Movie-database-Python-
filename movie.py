import collections
from select import select
import pymongo;

# connect database 
myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['movies']

# creating collection
mycol = mydb['movie']

# inserting into collection
mylist = [
    {"name": "RRR", "actor":'Ram Charan'},
    {"name": "Arvind Sametha", "actor":'Junior NTR'},
    {"name": "Bahubali", "actor":'Prabhash'},
    {"name": "KGF", "actor":'Yash'},
    {"name": "Geetha Govindam", "actor":'Vijay Deverkonda'}
]

x = mycol.insert_many(mylist)

# select all movies from database 
for i in mycol.find():
    print(i)
    

# finding specefic movie name 
myquery = {"actor": "Prabhash"}

mydoc = mycol.find(myquery)

for j in mydoc:
    print(j)