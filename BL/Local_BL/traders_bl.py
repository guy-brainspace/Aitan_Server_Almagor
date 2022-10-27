from DAL.Local_DAL.traders_dal import Traders_DAL


class Traders_BL:
    def __init__(self):
        self.traders_dal = Traders_DAL()

    def get_traders(self):
        traders = self.traders_dal.get_all_traders()
        traders_list = []
        for t in traders:
            d = {}
            d['id'] = t.id
            d['traderName'] = t.traderName
            d['area'] = t.area
            d['isActive'] = t.isActive
            traders_list.append(d)

        return traders_list

    def add_trader(self, data):
        record = {'traderName': data['traderName'],
                  'area': data['area'], 'isActive': data['isActive']}

        if (record['isActive'] == ''):
            record['isActive'] = False
        new_record = self.traders_dal.add_trader(record)
        return new_record

    def delete_trader(self, id):
        status = self.traders_dal.delete_trader(id)
        return status

    def update_trader(self, id, data):
        status = self.traders_dal.update_trader(id, data)
        return status
