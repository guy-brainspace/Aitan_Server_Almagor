# from Models.Rec_models import Receiving_fruits, Deals
# from confdb import db
# from sqlalchemy import extract,  func

import mysql.connector
from DAL.Rec_DAL.Reports_DAL.SQLReports.Monthly.per_fruitType import sql_query
from DAL.Rec_DAL.Reports_DAL.SQLReports.Monthly.per_FruitType_Deal import sql_query_perDeal


class Monthly_report_DAL():
    def __init__(self):
        pass

    def get_monthly_per_FruitType(self, season2filter, grower2filter, month2filter):

        # monthData=db.session.query(Receiving_fruits, Deals)\
        #             .outerjoin(Deals,  (Receiving_fruits.fruitTypeID== Deals.fruitTypeID
        #                                     and  Receiving_fruits.dealNameID== Deals.dealNameID
        #                                     and (Receiving_fruits.receivingDate>=Deals.fromDate and
        #                     Receiving_fruits.receivingDate<Deals.toDate)
        #                                             # &  Receiving_fruits.receivingDate.between(Deals.fromDate, Deals.toDate)))\
        #                                            ))\
        #             .filter(

        #                     Receiving_fruits.season==season2filter,
        #                     Receiving_fruits.growerID == grower2filter,
        #                     extract('month', Receiving_fruits.receivingDate) == month2filter,

        #                     )\
        #             .all()

        # return monthData
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MayanAsifOno8",
            database="aitan_roni"
        )

        mycursor = mydb.cursor()

        sql = sql_query

        params = [season2filter, grower2filter, month2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult

    def get_monthly_per_Deal(self, season2filter, grower2filter, month2filter):

        # return monthData
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MayanAsifOno8",
            database="aitan_roni"
        )

        mycursor = mydb.cursor()

        sql = sql_query_perDeal

        params = [season2filter, grower2filter, month2filter]
        mycursor.execute(sql, params)
        myresult = mycursor.fetchall()
        return myresult
