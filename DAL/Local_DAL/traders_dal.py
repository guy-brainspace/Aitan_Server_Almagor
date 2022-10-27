from Models.Models import Traders


class Traders_DAL():
    def __init__(self):
        pass

    def get_all_traders(self):
        traders = Traders.query.all()
        return traders

    def add_trader(self, data):
        new_record = Traders(
            traderName=data['traderName'], area=data['area'], isActive=data['isActive'])
        return new_record

    def delete_trader(self, id):
        status = Traders.query.filter(Traders.id == id).delete()
        return status

    def update_trader(self,  Traderid, data):
        record = Traders.query.filter_by(id=Traderid).first()
        record.traderName = data['traderName']
        record.area = data['area'],
        record.isActive = data['isActive']
        return ('trader was updated!')
