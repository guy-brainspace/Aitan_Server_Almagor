from Models.Models import Deals


class Deals_DAL():
    def __init__(self):
        pass

    def get_all_deals(self, filteredSeason):
        deals = Deals.query.filter(Deals.season == filteredSeason).all()
        return deals

    def add_deal(self, data):
        new_record = Deals(
            fromDate=data['fromDate'],
            toDate=data['toDate'],
            season=data['season'],
            dealNameID=data['dealNameID'],
            fruitTypeID=data['fruitTypeID'],
            price1=data['price1'],
            price1Date=data['price1Date'],
            price2=data['price2'],
            price2Date=data['price2Date'],
            price3=data['price3'],
            price3Date=data['price3Date']
        )

        return new_record

    def delete_deal(self, id):
        status = Deals.query.filter(Deals.id == id).delete()
        return status

    def update_deal(self,  dealID, data):
        record = Deals.query.filter_by(id=dealID).first()
        record.fromDate = data['fromDate']
        record.toDate = data['toDate']
        record.season = data['season']
        record.dealNameID = data['dealNameID']
        record.fruitTypeID = data['fruitTypeID']
        record.price1 = data['price1']
        record.price1Date = data['price1Date']
        record.price2 = data['price2']
        record.price2Date = data['price2Date']
        record.price3 = data['price3']
        record.price3Date = data['price3Date']
        return ('deal was updated!')
