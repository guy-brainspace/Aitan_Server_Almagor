from Models.Models import Packing_mat


class PackingMaterials_DAL():
    def __init__(self):
        pass

    def get_all_packingMaterials(self):
        packingMaterials = Packing_mat.query.all()
        return packingMaterials

    def add_packingMaterial(self, data):
        new_record = Packing_mat(
            packingType=data['packingType'], weight=data['weight'], isActive=data['isActive'])
        return new_record

    def delete_packingMaterial(self, id):
        status = Packing_mat.query.filter(Packing_mat.id == id).delete()
        return status

    def update_packingMaterial(self,  packingMaterial_id, data):
        record = Packing_mat.query.filter_by(id=packingMaterial_id).first()
        record.packingType = data['packingType']
        record.weight = data['weight']
        record.isActive = data['isActive']
        return ('packingMaterial was updated!')
