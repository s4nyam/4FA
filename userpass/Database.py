import sqlite3

def createTable():
    connection = sqlite3.connect('login.db')

    connection.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL,PASSWORD TEXT)")

    connection.execute("INSERT INTO USERS VALUES(?,?)",('sanyam','skinnysamy'))

    connection.commit()

    result = connection.execute("SELECT * FROM USERS")
    
    for data in result:
        print("Username : ",data[0])
        print("Password :",data[1])

    connection.close()

createTable()
        
    
