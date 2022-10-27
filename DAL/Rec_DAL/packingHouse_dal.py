from Models.Models import PackingHouse


class PackingHouse_DAL():
    def __init__(self):
        pass

    def get_all_packingHouses(self):
        houses = PackingHouse.query.all()
        return houses

    def add_packingHouse(self, data):
        new_record = PackingHouse(
            packingHouseName=data['packingHouseName'], location=data['location'], isActive=data['isActive'])
        return new_record

    def delete_packingHouse(self, id):
        status = PackingHouse.query.filter(PackingHouse.id == id).delete()
        return status

    def update_packingHouse(self, packingHouseID, data):
        record = PackingHouse.query.filter_by(id=packingHouseID).first()
        record.packingHouseName = data['packingHouseName']
        record.location = data['location']
        record.isActive = data['isActive']
        return ('packing house was updated!')
