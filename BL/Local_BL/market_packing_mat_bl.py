from DAL.Local_DAL.market_packing_mat_dal import Market_packing_mat_DAL


class Market_packing_mat_bl:
    def __init__(self):
        self.market_packing_mat_dal = Market_packing_mat_DAL()

    def get_market_packing_mat(self):
        packings = self.market_packing_mat_dal.get_all_market_packing_mat()
        packings_list = []
        for p in packings:
            d = {}
            d['id'] = p.id
            d['marketPackingType'] = p.marketPackingType
            d['isActive'] = p.isActive
            packings_list.append(d)

        return packings_list

    def add_market_packing_mat(self, data):
        record = {
            'marketPackingType': data['marketPackingType'], 'isActive': data['isActive']}

        if (record['isActive'] == ''):
            record['isActive'] = False
        new_record = self.market_packing_mat_dal.add_market_packing_mat(record)
        return new_record

    def delete_market_packing_mat(self, id):
        status = self.market_packing_mat_dal.delete_market_packing_mat(id)
        return status

    def update_market_packing_mat(self, id, data):
        status = self.market_packing_mat_dal.update_market_packing_mat(
            id, data)
        return status
