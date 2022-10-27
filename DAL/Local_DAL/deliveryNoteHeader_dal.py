from Models.Models import DeliveryNote_header as DNH
import datetime


class DeliveryNote_header_DAL():
    def __init__(self):
        pass

    def get_all_DNH(self, filteredSeason):
        deliveryNotes = DNH.query.filter(DNH.season == filteredSeason).all()
        return deliveryNotes

    def add_DNH(self, data):
        new_record = DNH(
            season=data['season'],
            deliveryNoteNum=data['deliveryNoteNum'],
            deliveryDate=data['deliveryDate'],
            traderID=data['traderID'],
            traderPrcnt=data['traderPrcnt'],
            distributerPrcnt=data['distributerPrcnt'],
            VAT=data['VAT']
        )
        return new_record

    def delete_DNH(self, id):
        status = DNH.query.filter(DNH.id == id).delete()
        return status

    def update_DNH(self,  palletID, data):
        record = DNH.query.filter_by(id=palletID).first()
        record.season = data['season']
        record.deliveryNoteNum = data['deliveryNoteNum'],
        record.deliveryDate = datetime.datetime(
            int(data['year']), int(data['month']), int(data['day'])),
        record.traderID = data['traderID'],
        record.traderPrcnt = data['traderPrcnt'],
        record.distributerPrcnt = data['distributerPrcnt'],
        record.VAT = data['VAT']
        return ('pallet creation header was updated!')
