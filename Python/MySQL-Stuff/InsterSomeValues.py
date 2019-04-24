"""
This script is to play a bit with MySQL
some notes:
tutorials_tbl(
   tutorial_id INT NOT NULL AUTO_INCREMENT,
   tutorial_title VARCHAR(100) NOT NULL,
   tutorial_author VARCHAR(40) NOT NULL,
   submission_date DATE,
   PRIMARY KEY ( tutorial_id )
);



CREATE TABLE alfred( id INT NOT NULL AUTO_INCREMENT, title VARCHAR(100) NOT NULL, author VARCHAR(40) NOT NULL, submission_date DATE, PRIMARY KEY ( id ));


"""
import pymysql

#value1 = input("Title: ")
#value2 = input("Author: ")

db = pymysql.connect("172.16.172.251","alfred","foobar","alfred")

cursor = db.cursor()
# cursor.execute("select * from alfred")
# data = cursor.fetchall()
# db.close()

#print (data)

#sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('%s', '%s', '%d', '%c', '%d' )" % ('Mac', 'Mohan', 20, 'M', 2000)

def db_insert():
    cursor.execute('truncate alfred')
    print("done")





print ("start with static statement...")
cursor.execute('insert into alfred set title=\'Title 1\', author = \'Ich 1\'')
db.commit()
print ("end.")

print("start with var-statement ...")
sql = ('insert into alfred set title=\'var sql 3\', author = \'var sql 9\'')
cursor.execute(sql)
db.commit()
print("end.")

print("What's in there ?")
cursor.execute("select * from alfred")
data = cursor.fetchall()
# print(data)

ask = input('Shall I truncate the table ? Y/N? ').upper()
print(ask)


if ask == "Y":
    print("truncate table ...")
    db_insert()

print("Weiter geht's")


db.close()
#print (data)

