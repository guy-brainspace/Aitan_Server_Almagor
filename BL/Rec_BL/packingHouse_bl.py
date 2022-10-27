from DAL.Rec_DAL.packingHouse_dal import PackingHouse_DAL


class PackingHouse_BL:
    def __init__(self):
        self.packingHouse_dal = PackingHouse_DAL()

    def get_packingHouses(self):
        packingHouses = self.packingHouse_dal.get_all_packingHouses()
        packingHouses_list = []
        for house in packingHouses:
            d = {}
            d['id'] = house.id
            d['packingHouseName'] = house.packingHouseName
            d['location'] = house.location
            d['isActive'] = house.isActive
            packingHouses_list.append(d)

        return packingHouses_list

    def add_packingHouse(self, data):
        record = {'packingHouseName': data['packingHouseName'],
                  'location': data['location'], 'isActive': data['isActive']}
        if (record['isActive'] == ''):
            record['isActive'] = False
        new_record = self.packingHouse_dal.add_packingHouse(record)
        return new_record

    def delete_packingHouse(self, id):
        status = self.packingHouse_dal.delete_packingHouse(id)
        return status

    def update_packingHouse(self, id, data):
        status = self.packingHouse_dal.update_packingHouse(id, data)
        return status
