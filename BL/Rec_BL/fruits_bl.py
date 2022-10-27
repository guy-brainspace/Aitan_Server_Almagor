from DAL.Rec_DAL.fruits_dal import Fruits_DAL


class Fruits_BL:
    def __init__(self):
        self.fruits_dal = Fruits_DAL()

    def get_fruits(self):
        fruits = self.fruits_dal.get_all_fruits()
        fruits_list = []
        for fruit in fruits:
            d = {}
            d['id'] = fruit.id
            d['fruitName'] = fruit.fruitName
            d['fruitType'] = fruit.fruitType
            d['isActive'] = fruit.isActive
            fruits_list.append(d)

        return fruits_list

    def add_fruit(self, data):
        record = {'fruitName': data['fruitName'],
                  'fruitType': data['fruitType'], 'isActive': data['isActive']}

        if (record['isActive'] == ''):
            record['isActive'] = False
        new_record = self.fruits_dal.add_fruit(record)
        return new_record

    def delete_fruit(self, id):
        status = self.fruits_dal.delete_fruit(id)
        return status

    def update_fruit(self, id, data):
        status = self.fruits_dal.update_fruit(id, data)
        return status
