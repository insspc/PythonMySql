#Python code

import mysql.connector

spcdatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="    "
    )

spccur=spcdatabase.cursor()
databasename=input("Enter a name for the database to be created ")
spccur.execute("create database {}".format(databasename))
spccur.execute("show databases")
for x in spccur:
    print(x)


spcdatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="    ",
    database=databasename
    )

spccur=spcdatabase.cursor()

tablename=input("Enter a name for the SQL table ")
nooffields=int(input("Enter no of fields "))
i=1
while(i<=nooffields):
    field=input("Enter the field name ")
    typeorsize=input("Enter type for int, float or size for varchar ")
    print(field,"   ",typeorsize)
    i+=1


spccur.execute("create table {} ({} {})".format(tablename,field,typeorsize))
spccur.execute("show tables")


