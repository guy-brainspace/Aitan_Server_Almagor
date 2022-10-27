import mysql.connector
from DAL.Rec_DAL.Reports_DAL.SQLReports.Summary.summaryMonthly import sql_query
from DAL.Rec_DAL.Reports_DAL.SQLReports.Summary.SummarySeasonFruitPackhouse import sql_packingHouse_query
from DAL.Rec_DAL.Reports_DAL.SQLReports.Summary.summarySeasson import sql_summarySeason
from DAL.Rec_DAL.Reports_DAL.SQLReports.Summary.summarySeasnGrowers import sql_summarySeasonGrowers
from DAL.Rec_DAL.Reports_DAL.SQLReports.Summary.summaryMonthlyPackingMat import sql_MonthlyPackingMat_query


class Summary_report_DAL():
    def __init__(self):
        pass

    def get_summary_monthly(self, season2filter, month2filter):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MayanAsifOno8",
            database="aitan_roni"
        )

        mycursor = mydb.cursor()

        sql = sql_query

        params = [season2filter, month2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult

    def get_summary_packingHouse(self, season2filter):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MayanAsifOno8",
            database="aitan_roni"
        )

        mycursor = mydb.cursor()

        sql = sql_packingHouse_query

        params = [season2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult

    def get_summary_season(self, season2filter):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MayanAsifOno8",
            database="aitan_roni"
        )

        mycursor = mydb.cursor()

        sql = sql_summarySeason

        params = [season2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult

    def get_summary_season_growers(self, season2filter):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MayanAsifOno8",
            database="aitan_roni"
        )

        mycursor = mydb.cursor()

        sql = sql_summarySeasonGrowers

        params = [season2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult

    def get_summary_monthly_packingMat(self, season2filter, month2filter):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MayanAsifOno8",
            database="aitan_roni"
        )

        mycursor = mydb.cursor()

        sql = sql_MonthlyPackingMat_query

        params = [season2filter, month2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult
