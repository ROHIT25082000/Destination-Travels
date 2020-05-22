import psycopg2
import sys
import subprocess as sp
import time 

conn = psycopg2.connect(
    database ="postgres", user = "postgres", password ="postgres", host ="localhost", port = "5432"
)

conn.autocommit = True
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
#Preparing query to create a database
#cursor.execute("DROP DATABASE IF EXISTS taxidatabase")
try:
    sql = '''CREATE database taxidatabase'''
    #Creating a database
    cursor.execute(sql)
    print("Database created successfully........")
    fp = open("meta.dat","w")
    fp.write("123450,543210,10000,50000,404")
    fp.close()
except:
    print("Your was ready previously Ready :->",sys.exc_info()[0])

finally:
    print("Processing ...")
    print("Checking Schema ...")
conn.close()
try:
    import schema
    time.sleep(5)
except:
    print("Schema already utilized ...",sys.exc_info()[0])
finally:
    print("Processing further...")
    time.sleep(1)
    print("Starting application ... ")
    time.sleep(1)
    tmp = sp.call('clear',shell=True)









