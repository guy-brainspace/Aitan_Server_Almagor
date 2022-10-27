from Models.Models import Market_packing_mat


class Market_packing_mat_DAL():
    def __init__(self):
        pass

    def get_all_market_packing_mat(self):
        packingMats = Market_packing_mat.query.all()
        return packingMats

    def add_market_packing_mat(self, data):
        new_record = Market_packing_mat(
            marketPackingType=data['marketPackingType'], isActive=data['isActive'])
        return new_record

    def delete_market_packing_mat(self, id):
        status = Market_packing_mat.query.filter(
            Market_packing_mat.id == id).delete()
        return status

    def update_market_packing_mat(self, packingid, data):
        record = Market_packing_mat.query.filter_by(id=packingid).first()
        record.marketPackingType = data['marketPackingType']
        record.isActive = data['isActive']
        return ('market packing material was updated!')
