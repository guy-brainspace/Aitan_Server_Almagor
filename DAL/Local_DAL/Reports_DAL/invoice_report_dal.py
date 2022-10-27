import mysql.connector
from DAL.Local_DAL.SQL_DAL.Invoices.sql_query_invoiceLines import sql_query_invoiceLines
from DAL.Local_DAL.SQL_DAL.Invoices.sql_query_palletCost import sql_query_palletCost
from DAL.Local_DAL.SQL_DAL.Invoices.sql_query_resellerInfo import sql_query_resellerInfo


class Invoice_report_DAL():
    def __init__(self):
        pass

       
    def get_reportData(self, sql, id):
        
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MayanAsifOno8",
            database="aitan_roni"
        )

        mycursor = mydb.cursor()
        params = [id]
        mycursor.execute(sql, params)
        Results = mycursor.fetchall()

        return Results

    def get_invoiceLines(self, invoiceHeaderID):
        invoiceLines_results = self.get_reportData(
            sql_query_invoiceLines, invoiceHeaderID)
        return invoiceLines_results

    def get_palletCost(self, invoiceHeaderID):
        palletCost_results = self.get_reportData(
            sql_query_palletCost, invoiceHeaderID)
        return palletCost_results

    def get_resellerInfo(self, invoiceHeaderID):
        resellerInfo_results = self.get_reportData(
            sql_query_resellerInfo, invoiceHeaderID)
        return resellerInfo_results
