import mysql.connector
import os
from DAL.Rec_DAL.Reports_DAL.SQLReports.Season.seasonPerFruitName import sql_query_perFruitName


class Season_report_DAL():
    def __init__(self):
        pass

    def get_season_per_fruitName(self, season2filter, grower2filter):

        mydb = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_DATABASE")
        )


        mycursor = mydb.cursor()

        sql = sql_query_perFruitName

        params = [season2filter, grower2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult
