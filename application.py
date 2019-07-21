from flask import Flask
import pyodbc
import time

server='pythonsqltest.database.windows.net'
database='pythonsqltest'
username='username@pythonsqltest'
password='Password1'

app = Flask(__name__)

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor=conn.cursor()

@app.route("/")
def hello():
    SQLCommand = ("INSERT INTO dbo.employee "
                 "(name, age, place) "
                 "VALUES (?,?,?)")
    Values = ['test','1','us']
    cursor.execute(SQLCommand,Values)
    conn.commit()
    return "Hello World!"    

if __name__ == "__main__":
    app.run() 
   
