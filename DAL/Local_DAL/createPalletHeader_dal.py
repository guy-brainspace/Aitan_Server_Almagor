from Models.Models import FruitPalletCreation_header as FPCH
import datetime


class FruitPalletCreation_header_DAL():
    def __init__(self):
        pass

    def get_all_FPCH(self, filteredSeason):

        palletsCreations = FPCH.query.filter(
            FPCH.season == filteredSeason).all()
        return palletsCreations

    def add_FPCH(self, data):
        new_record = FPCH(
            season=data['season'],
            palletNum=data['palletNum'],
            palletMatID=data['palletMatID'],
            packingDate=data['packingDate'],
            palletRemarks=data['palletRemarks']
        )
        return new_record

    def delete_FPCH(self, id):
        status = FPCH.query.filter(FPCH.id == id).delete()
        return status

    def update_FPCH(self,  palletID, data):
        record = FPCH.query.filter_by(id=palletID).first()
        record.season = data['season']
        record.palletNum = data['palletNum'],
        record.palletMatID = data['palletMatID'],
        record.packingDate = datetime.datetime(
            int(data['year']), int(data['month']), int(data['day']))
        record.palletRemarks = data['palletRemarks'],
        return ('pallet creation header was updated!')
