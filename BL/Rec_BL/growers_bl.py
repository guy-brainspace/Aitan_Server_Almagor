from DAL.Rec_DAL.growers_dal import Growers_DAL


class Growers_BL:
    def __init__(self):
        self.growers_dal = Growers_DAL()

    def get_growers(self):
        growers = self.growers_dal.get_all_growers()
        grower_list = []
        for grower in growers:
            d = {}
            d['id'] = grower.id
            d['growerName'] = grower.growerName
            d['isActive'] = grower.isActive
            grower_list.append(d)

        return grower_list

    def add_grower(self, data):
        record = {'growerName': data['growerName'],
                  'isActive': data['isActive']}

        if (record['isActive'] == ''):
            record['isActive'] = False
        new_record = self.growers_dal.add_grower(record)
        return new_record

    def delete_grower(self, id):
        status = self.growers_dal.delete_grower(id)
        return status

    def update_grower(self, id, data):
        status = self.growers_dal.update_grower(id, data)
        return status
