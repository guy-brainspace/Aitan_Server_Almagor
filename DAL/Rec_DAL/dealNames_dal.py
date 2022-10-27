
from Models.Models import DealNames


class DealNames_DAL():
    def __init__(self):
        pass

    def get_all_dealNames(self):
        dealNames = DealNames.query.all()
        return dealNames

    def add_dealName(self, data):
        new_record = DealNames(
            dealName=data['dealName'], isActive=data['isActive'])
        return new_record

    def delete_dealName(self, id):
        status = DealNames.query.filter(DealNames.id == id).delete()
        return status

    def update_dealName(self,  dealNameid, data):
        record = DealNames.query.filter_by(id=dealNameid).first()
        record.dealName = data['dealName']
        record.isActive = data['isActive']
        return ('dealName was updated!')
