from Models.Models import PalletsMatCost


class PalletsMatCost_DAL():
    def __init__(self):
        pass

    def get_all_palletsMatCostperMatID(self, palletsMatTypeID):
        palletsMatdata = PalletsMatCost.query.filter(
            PalletsMatCost.palletMatID == palletsMatTypeID).all()
        return palletsMatdata

    def add_palletMatCost(self, data):
        new_record = PalletsMatCost(
            palletMatID=data['palletMatID'],
            fromDate=data['fromDate'],
            toDate=data['toDate'],
            palletMatCost=data['palletMatCost']
        )

        return new_record

    def delete_palletMatCost(self, id):
        status = PalletsMatCost.query.filter(PalletsMatCost.id == id).delete()
        return status

    def update_palletMatCost(self,  palletid, data):
        record = PalletsMatCost.query.filter_by(id=palletid).first()
        record.palletMatID = data['palletMatID']
        record.fromDate = data['fromDate']
        record.toDate = data['toDate']
        record.palletMatCost = data['palletMatCost']
        return ('palletMatCost was updated!')
