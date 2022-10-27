from DAL.Local_DAL.fruitSize_dal import FruitSize_DAL


class FruitSize_BL:
    def __init__(self):
        self.fruitSize_dal = FruitSize_DAL()

    def get_fruitSize(self):
        fruitSize = self.fruitSize_dal.get_all_fruitSize()
        fruitSize_list = []
        for fSize in fruitSize:
            d = {}
            d['id'] = fSize.id
            d['size'] = fSize.size
            d['isActive'] = fSize.isActive
            fruitSize_list.append(d)

        return fruitSize_list

    def add_fruitSize(self, data):
        record = {'size': data['size'], 'isActive': data['isActive']}

        if (record['isActive'] == ''):
            record['isActive'] = False
        new_record = self.fruitSize_dal.add_fruitSize(record)
        return new_record

    def delete_fruitSize(self, id):
        status = self.fruitSize_dal.delete_fruitSize(id)
        return status

    def update_fruitSize(self, id, data):
        status = self.fruitSize_dal.update_fruitSize(id, data)
        return status
