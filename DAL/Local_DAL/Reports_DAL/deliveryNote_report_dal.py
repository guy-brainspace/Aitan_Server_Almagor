import mysql.connector
import os
from DAL.Local_DAL.SQL_DAL.DeliveryNote.perDeliveryNote import sql_query_deliveryNote
from DAL.Local_DAL.SQL_DAL.DeliveryNote.sql_query_deliveryNote2prct import sql_query_deliveryNote2prct


class DeliveryNote_report_DAL():
    def __init__(self):
        pass

    def get_deliveryNote(self, reportFilter, deliveryNoteNum2filter, season2filter):

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

        if (reportFilter == 'all'):
            sql = sql_query_deliveryNote
        if (reportFilter == '2prct'):
            sql = sql_query_deliveryNote2prct

        params = [deliveryNoteNum2filter, season2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult
