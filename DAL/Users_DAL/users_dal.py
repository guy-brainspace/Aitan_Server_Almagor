import mysql.connector


class Users_DAL():
    def __init__(self):
        pass

    def get_all_users(self):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MayanAsifOno8",
            database="aitan_users"
        )

        mycursor = mydb.cursor()

        sql = '''select id, userName, password from aitan_users.users '''

        mycursor.execute(sql)
        usersData = mycursor.fetchall()

        usersList = []
        for record in usersData:
            dictRecord = {}
            dictRecord['id'] = record[0]
            dictRecord['userName'] = record[1]
            dictRecord['password'] = record[2]

            usersList.append(dictRecord)

        return usersList
