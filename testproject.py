import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user= "root",
    password="Vinceramirezpogi1",
    database="testdatabase",
)
mycursor = db.cursor()
#
# mycursor.execute("CREATE TABLE Person (name VARCHAR(50) , "
#                  "age int UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

print("WELCOME TO MY DATABASE PYTHON TEST!")
print("Just simply type your first name and age so we can register you in our database")


def first_name():
    personname = input("What is your name? ")
    if personname.isalpha():
        return personname
    else:
        print("You must enter letters only")
    exit()


def age():
    try:
        person_age = int(input("What is your age? "))
        return person_age
    except ValueError:
        print("You entered invalid keyword")
    exit()


firstname = first_name()
age_input = age()

mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)", (firstname,age_input))
db.commit()


