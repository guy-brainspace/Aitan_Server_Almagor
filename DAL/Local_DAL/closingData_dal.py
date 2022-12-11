import mysql.connector
from DAL.Local_DAL.SQL_DAL.ClosingData.closingData import sql_query_closingData
from Models.Models import ClosingData
import datetime
import os

class ClosingData_DAL():
    def __init__(self):
        pass

    def get_all_closingData(self, filteredSeason):

        # mydb = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     password="MayanAsifOno8",
        #     database="aitan_roni"
        # )
        # mydb = mysql.connector.connect(
        #     host="aitan2.cwlotalknksl.us-east-1.rds.amazonaws.com",
        #     user="root",
        #     password="$$brain.space$$88",
        #     database="aitan_roni"
        # )
        mydb = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_DATABASE")
        )

        mycursor = mydb.cursor()

        sql = sql_query_closingData

        params = [filteredSeason]
        mycursor.execute(sql, params)
        closingInvoicedata = mycursor.fetchall()
        return closingInvoicedata

    def add_closingData(self, data):
        new_record = ClosingData(
            fruitPalletCreationLineID=data['fruitPalletCreationLineID'],
            closeWeight=data['closeWeight'],
            closePrice=data['closePrice'],
            closeDate=data['closeDate'],
            closeRemarks=data['closeRemarks']
        )
        return new_record

    def delete_closingData(self, id):
        status = ClosingData.query.filter(ClosingData.id == id).delete()
        return status

    def update_closingData(self, closingid, data):
        record = ClosingData.query.filter_by(id=closingid).first()
        record.fruitPalletCreationLineID = data['fruitPalletCreationLineID']
        record.closeWeight = data['closeWeight']
        record.closePrice = data['closePrice']
        record.closeDate = datetime.datetime(
            int(data['year']), int(data['month']), int(data['day']))
        record.closeRemarks = data['closeRemarks']
        return ('closingData was updated!')
