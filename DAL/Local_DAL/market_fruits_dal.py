from Models.Models import Market_fruits


class Market_fruits_DAL():
    def __init__(self):
        pass

    def get_all_marketFruits(self):
        fruits = Market_fruits.query.all()
        return fruits

    def add_marketFruit(self, data):
        new_record = Market_fruits(
            fruitID=data['fruitID'],
            sizeID=data['sizeID'],
            quality=data['quality'],
            isActive=data['isActive']
        )

        return new_record

    def delete_marketFruit(self, id):
        status = Market_fruits.query.filter(Market_fruits.id == id).delete()
        return status

    def update_marketFruit(self,  marketFruitID, data):
        record = Market_fruits.query.filter_by(id=marketFruitID).first()
        record.fruitID = data['fruitsID']
        record.sizeID = data['fruitSizeID']
        record.quality = data['quality']
        record.isActive = data['isActive']
        return ('marketFruit was updated!')
