
from Models.Models import Fruits


class Fruits_DAL():
    def __init__(self):
        pass

    def get_all_fruits(self):
        fruits = Fruits.query.all()
        return fruits

    def add_fruit(self, data):
        new_record = Fruits(
            fruitName=data['fruitName'], fruitType=data['fruitType'], isActive=data['isActive'])
        return new_record

    def delete_fruit(self, id):
        status = Fruits.query.filter(Fruits.id == id).delete()
        return status

    def update_fruit(self, fruitid, data):
        record = Fruits.query.filter_by(id=fruitid).first()
        record.fruitName = data['fruitName']
        record.fruitType = data['fruitType']
        record.isActive = data['isActive']
        return ('fruit was updated!')
