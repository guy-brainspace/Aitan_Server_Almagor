from DAL.Rec_DAL.dealNames_dal import DealNames_DAL


class DealNames_BL:
    def __init__(self):
        self.dealNames_dal = DealNames_DAL()

    def get_dealNames(self):
        dealNames = self.dealNames_dal.get_all_dealNames()
        dealName_list = []
        for name in dealNames:
            d = {}
            d['id'] = name.id
            d['dealName'] = name.dealName
            d['isActive'] = name.isActive
            dealName_list.append(d)

        return dealName_list

    def add_dealName(self, data):
        record = {'dealName': data['dealName'], 'isActive': data['isActive']}
        if (record['isActive'] == ''):
            record['isActive'] = False
        new_record = self.dealNames_dal.add_dealName(record)
        return new_record

    def delete_dealName(self, id):
        status = self.dealNames_dal.delete_dealName(id)
        return status

    def update_dealName(self, id, data):
        status = self.dealNames_dal.update_dealName(id, data)
        return status
