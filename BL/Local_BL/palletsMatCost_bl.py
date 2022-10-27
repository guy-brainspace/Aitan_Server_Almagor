from DAL.Local_DAL.palletsMatCost_dal import PalletsMatCost_DAL
import datetime


class PalletsMatCost_BL:
    def __init__(self):
        self.palletsMatCost_dal = PalletsMatCost_DAL()

    def get_dates(self, data):
        if data['year_from'] != 0:
            data['fromDate'] = datetime.datetime(
                int(data['year_from']), int(data['month_from']), int(data['day_from']))
        else:
            data['fromDate'] = datetime.date.today()

        if data['year_to'] != 0:
            data['toDate'] = datetime.datetime(
                int(data['year_to']), int(data['month_to']), int(data['day_to']))
        else:
            data['toDate'] = datetime.date.today()

        return data

    def get_palletsMatCost(self, palletsMatID):
        pallets = self.palletsMatCost_dal.get_all_palletsMatCostperMatID(
            palletsMatID)
        pallets_list = []
        for p in pallets:
            d = {}
            d['id'] = p.id
            d['palletMatID'] = p.palletMatID
            d['palletMatType'] = p.palletsmat.palletType
            d['fromDate'] = p.fromDate
            d['toDate'] = p.toDate
            d['palletMatCost'] = p.palletMatCost
            pallets_list.append(d)

        return pallets_list

    def add_palletMatCost(self, data):
        data_to_add = self.get_dates(data)
        new_record = self.palletsMatCost_dal.add_palletMatCost(data_to_add)
        return new_record

    def delete_palletMatCost(self, id):
        status = self.palletsMatCost_dal.delete_palletMatCost(id)
        return status

    def update_palletMatCost(self, id, data):
        data_to_update = self.get_dates(data)
        status = self.palletsMatCost_dal.update_palletMatCost(
            id, data_to_update)
        return status
