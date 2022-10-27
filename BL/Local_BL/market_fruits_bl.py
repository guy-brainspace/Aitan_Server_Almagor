from DAL.Local_DAL.market_fruits_dal import Market_fruits_DAL


class Market_fruits_BL:
    def __init__(self):
        self.market_fruits_dal = Market_fruits_DAL()

    def get_marketFruits(self):
        fruits = self.market_fruits_dal.get_all_marketFruits()
        fruits_list = []
        for f in fruits:
            d = {}
            d['id'] = f.id
            d['fruitsID'] = f.fruitID
            d['fruitName'] = f.fruits.fruitName
            d['fruitType'] = f.fruits.fruitType
            d['fruitSizeID'] = f.sizeID
            d['size'] = f.fruitsize.size
            d['quality'] = f.quality
            d['isActive'] = f.isActive
            fruits_list.append(d)

        return fruits_list

    def add_marketFruit(self, data):
        record = {'fruitID': data['fruitsID'],
                  'sizeID': data['fruitSizeID'],
                  'quality': data['quality'],
                  'isActive': data['isActive']
                  }

        if (record['isActive'] == ''):
            record['isActive'] = False
        new_record = self.market_fruits_dal.add_marketFruit(record)
        return new_record

    def delete_marketFruit(self, id):
        status = self.market_fruits_dal.delete_marketFruit(id)
        return status

    def update_marketFruit(self, id, data):
        status = self.market_fruits_dal.update_marketFruit(id, data)
        return status
