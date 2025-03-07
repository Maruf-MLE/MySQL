import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            self.conn= mysql.connector.connect(host='localhost',
user='root',password='',database='hit_db-demo1',connect_timeout=5)
            self.mycursor=self.conn.cursor()
            print('some error occurred.could not connect to data base')

        except:
            print('connected to database')



