import psycopg2
from django import db

username = input("Enter username: ")
password = input("Enter password: ")

#print(db.connections.databases)

conn = psycopg2.connect("dbname ='newdb1' user='postgres' host='localhost' password='p3ngu1n'")
cur = conn.cursor()
cur.execute("""SELECT report_title from report_report""")
titles = cur.fetchall()

for title in titles:
    print(title[0])

wanted = input("Type the name of the report you would like to view:")
print("Title: ", wanted)
cur.execute("SELECT report_short_description from report_report where report_title = %s", [wanted])
shortdes = cur.fetchall()
print("Short Description: ", shortdes[0][0])

cur.execute("SELECT report_long_description from report_report where report_title = %s", [wanted])
longdes = cur.fetchall()
print("Long Description: ", longdes[0][0])

cur.execute("SELECT report_file from report_report where report_title = %s", [wanted])
file = cur.fetchall()
print("File: ", file[0][0])


