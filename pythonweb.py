#!C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10n
print("Content-Type:text/html")
print()


import cgi

print("<h1>Welcome to python Python Web Mysql Application</h1>")
print("<hr/>")
print("<body bgcolor='red'>")

form = cgi.FieldStorage()


id = form.getvalue("id")
username = form.getvalue("name")
address = form.getvalue("address")
email = form.getvalue("email")
mobile = form.getvalue("phonenumber")
gender = form.getvalue("gender")
select = form.getvalue("select")


import mysql.connector

con = mysql.connector.connect(user='root', password='', host='localhost', database='webpython')
cur=con.cursor()

cur.execute("INSERT INTO web VALUES(% s, % s, % s, % s, % s, % s, % s)", (id, username, address, gender, email, select, mobile))
cur.close()
con.close()
print("<h3>Record Inserted Successfully!</h3>")
print("<a href ='http://localhost/extra/index.html'>Click here to go back </a>")