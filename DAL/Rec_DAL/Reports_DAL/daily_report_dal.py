import mysql.connector
from DAL.Rec_DAL.Reports_DAL.SQLReports.Daily.perFruitName import sql_query_perFruitName


class Daily_report_DAL():
    def __init__(self):
        pass

    def get_daily_per_fruitName(self, date2filter, grower2filter):

        # return dailyData
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MayanAsifOno8",
            database="aitan_roni"
        )

        mycursor = mydb.cursor()

        sql = sql_query_perFruitName

        params = [date2filter, grower2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult
