import mysql.connector
import os
from DAL.Rec_DAL.Reports_DAL.SQLReports.Daily.perFruitName import sql_query_perFruitName


class Daily_report_DAL():
    def __init__(self):
        pass

    def get_daily_per_fruitName(self, date2filter, grower2filter):

        # return dailyData
        # mydb = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     password="MayanAsifOno8",
        #     database="aitan_roni"
        # )
        mydb = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_DATABASE")
        )

        mycursor = mydb.cursor()

        sql = sql_query_perFruitName

        params = [date2filter, grower2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult
