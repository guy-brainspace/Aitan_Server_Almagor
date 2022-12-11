import mysql.connector
import os
from DAL.Local_DAL.SQL_DAL.Reports.sql_palletsWOinvoices import sql_query_palletsWOinvoices


class Pallets_wo_invoices_DAL():
    def __init__(self):
        pass

    def get_palletsWOinvoices(self, deliveryFromDate, deliveryToDate, traderID):

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

        sql = sql_query_palletsWOinvoices

        params = [deliveryFromDate, deliveryToDate, traderID]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult
