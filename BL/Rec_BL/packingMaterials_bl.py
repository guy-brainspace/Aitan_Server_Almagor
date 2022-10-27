from DAL.Rec_DAL.packingMaterials_dal import PackingMaterials_DAL


class PackingMaterials_BL:
    def __init__(self):
        self.packingMaterial_dal = PackingMaterials_DAL()

    def get_packingMaterials(self):
        packingMaterials = self.packingMaterial_dal.get_all_packingMaterials()
        packingMaterials_list = []
        for mat in packingMaterials:
            d = {}
            d['id'] = mat.id
            d['packingType'] = mat.packingType
            d['weight'] = mat.weight
            d['isActive'] = mat.isActive
            packingMaterials_list.append(d)

        return packingMaterials_list

    def add_packingMaterial(self, data):
        record = {'packingType': data['packingType'],
                  'weight': data['weight'],  'isActive': data['isActive']}
        if (record['isActive'] == ''):
            record['isActive'] = False
        new_record = self.packingMaterial_dal.add_packingMaterial(record)
        return new_record

    def delete_packingMaterial(self, id):
        status = self.packingMaterial_dal.delete_packingMaterial(id)
        return status

    def update_packingMaterial(self, id, data):
        status = self.packingMaterial_dal.update_packingMaterial(id, data)
        return status
