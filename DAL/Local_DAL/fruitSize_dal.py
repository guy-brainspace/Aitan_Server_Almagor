from Models.Models import FruitSize


class FruitSize_DAL():
    def __init__(self):
        pass

    def get_all_fruitSize(self):
        fruitSize = FruitSize.query.all()
        return fruitSize

    def add_fruitSize(self, data):
        new_record = FruitSize(size=data['size'], isActive=data['isActive'])
        return new_record

    def delete_fruitSize(self, id):
        status = FruitSize.query.filter(FruitSize.id == id).delete()
        return status

    def update_fruitSize(self,  fruitSizeid, data):
        record = FruitSize.query.filter_by(id=fruitSizeid).first()
        record.size = data['size']
        record.isActive = data['isActive']
        return ('size was updated!')
