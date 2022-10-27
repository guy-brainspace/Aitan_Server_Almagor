from Models.Models import Growers


class Growers_DAL():
    def __init__(self):
        pass

    def get_all_growers(self):
        growers = Growers.query.all()
        return growers

    def add_grower(self, data):
        new_record = Growers(
            growerName=data['growerName'], isActive=data['isActive'])
        return new_record

    def delete_grower(self, id):
        status = Growers.query.filter(Growers.id == id).delete()
        return status

    def update_grower(self,  growerid, data):
        record = Growers.query.filter_by(id=growerid).first()
        record.growerName = data['growerName']
        record.isActive = data['isActive']
        return ('grower was updated!')
