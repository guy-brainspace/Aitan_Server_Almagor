import mysql.connector
from DAL.Rec_DAL.Reports_DAL.SQLReports.PlotSummary.plotSummary import plotSummaryperDates
from DAL.Rec_DAL.Reports_DAL.SQLReports.PlotSummary.allPlotSummary import allPlotSummaryperDates


class Plot_report_DAL():
    def __init__(self):
        pass

    def get_plot_per_dates(self, plotName2Filter, fromDate2filter, toDate2filter):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MayanAsifOno8",
            database="aitan_roni"
        )

        mycursor = mydb.cursor()

        sql = plotSummaryperDates

        params = [plotName2Filter, fromDate2filter, toDate2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult

    def get_plots_per_dates(self, fromDate2filter, toDate2filter):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MayanAsifOno8",
            database="aitan_roni"
        )

        mycursor = mydb.cursor()

        sql = allPlotSummaryperDates

        params = [fromDate2filter, toDate2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult
