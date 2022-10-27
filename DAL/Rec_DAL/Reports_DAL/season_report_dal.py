import mysql.connector
from DAL.Rec_DAL.Reports_DAL.SQLReports.Season.seasonPerFruitName import sql_query_perFruitName


class Season_report_DAL():
    def __init__(self):
        pass

    def get_season_per_fruitName(self, season2filter, grower2filter):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MayanAsifOno8",
            database="aitan_roni"
        )

        mycursor = mydb.cursor()

        sql = sql_query_perFruitName

        params = [season2filter, grower2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult
