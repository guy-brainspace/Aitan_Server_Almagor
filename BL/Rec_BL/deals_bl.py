from DAL.Rec_DAL.deals_dal import Deals_DAL
import datetime
import calendar


class Deals_BL:
    def __init__(self):
        self.deals_dal = Deals_DAL()

    def get_deals(self, season):
        deals = self.deals_dal.get_all_deals(season)
        deal_list = []
        for deal in deals:
            d = {}
            d['id'] = deal.id
            d['fromDate'] = deal.fromDate
            d['toDate'] = deal.toDate
            d['season'] = deal.season
            d['dealNameID'] = deal.dealNameID
            d['dealName'] = deal.dealnames.dealName
            d['fruitTypeID'] = deal.fruitTypeID
            d['fruitName'] = deal.fruits.fruitName
            d['fruitType'] = deal.fruits.fruitType
            d['price1'] = deal.price1
            d['price1Date'] = deal.price1Date
            d['price2'] = deal.price2
            d['price2Date'] = deal.price2Date
            d['price3'] = deal.price3
            d['price3Date'] = deal.price3Date
            deal_list.append(d)

        return deal_list

    def get_dates(self, data):
        if data['year_from'] != 0:
            data['fromDate'] = datetime.datetime(
                int(data['year_from']), int(data['month_from']), int(data['day_from']))
        else:
            data['fromDate'] = datetime.date.today()

        # get the last day of the month
        if data['year_from'] != 0:
            currentDate = data['fromDate']
        else:
            currentDate = datetime.date.today()

        data['toDate'] = datetime.date(currentDate.year, currentDate.month, calendar.monthrange(
            currentDate.year, currentDate.month)[1])

        if 'price1Date' not in data:
            data['price1Date'] = 0
            if 'price1' not in data:
                data['price1'] = 0
        if (int(data['month_price1']) == 0):
            data['price1Date'] = None
        else:
            data['price1Date'] = datetime.datetime(int(data['year_price1']), int(
                data['month_price1']), int(data['day_price1']))

        if 'price2Date' not in data:
            data['price2Date'] = 0
            if 'price2' not in data:
                data['price2'] = 0
        if (int(data['month_price2']) == 0):
            data['price2Date'] = None
        else:
            data['price2Date'] = datetime.datetime(int(data['year_price2']), int(
                data['month_price2']), int(data['day_price2']))

        if 'price3Date' not in data:
            data['price3Date'] = 0
            if 'price3' not in data:
                data['price3'] = 0
        if (int(data['month_price3']) == 0):
            data['price3Date'] = None
        else:
            data['price3Date'] = datetime.datetime(int(data['year_price3']), int(
                data['month_price3']), int(data['day_price3']))

        return data

    def add_deal(self, data):
        data_to_add = self.get_dates(data)
        if (float(data['price1']) != 0 and data['price1Date'] == None) or (float(data['price2']) != 0 and data['price2Date'] == None) or (float(data['price3']) != 0 and data['price3Date'] == None):
            return ("missingData")

        new_record = self.deals_dal.add_deal(data_to_add)
        return new_record

    def delete_deal(self, id):
        status = self.deals_dal.delete_deal(id)
        return status

    def update_deal(self, id, data):

        data_to_update = self.get_dates(data)
        status = self.deals_dal.update_deal(id, data_to_update)
        return status
