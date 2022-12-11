import mysql.connector
import os
from DAL.Rec_DAL.Reports_DAL.SQLReports.PlotSummary.plotSummary import plotSummaryperDates
from DAL.Rec_DAL.Reports_DAL.SQLReports.PlotSummary.allPlotSummary import allPlotSummaryperDates


class Plot_report_DAL():
    def __init__(self):
        pass

    def get_plot_per_dates(self, plotName2Filter, fromDate2filter, toDate2filter):
        mydb = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_DATABASE")
        )


        mycursor = mydb.cursor()

        sql = plotSummaryperDates

        params = [plotName2Filter, fromDate2filter, toDate2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult

    def get_plots_per_dates(self, fromDate2filter, toDate2filter):
        mydb = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_DATABASE")
        )


        mycursor = mydb.cursor()

        sql = allPlotSummaryperDates

        params = [fromDate2filter, toDate2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult
