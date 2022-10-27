from Models.Models import PalletsMat


class PalletsMat_DAL():
    def __init__(self):
        pass

    def get_all_palletsMat(self):
        palletsMat = PalletsMat.query.all()
        return palletsMat

    def add_palletMat(self, data):
        new_record = PalletsMat(
            palletType=data['palletType'], palletWeight=data['palletWeight'],   isActive=data['isActive'])
        return new_record

    def delete_palletMat(self, id):
        status = PalletsMat.query.filter(PalletsMat.id == id).delete()
        return status

    def update_palletMat(self,  palletid, data):
        record = PalletsMat.query.filter_by(id=palletid).first()
        record.palletType = data['palletType']
        record.palletWeight = data['palletWeight']
        record.isActive = data['isActive']
        return ('pallet was updated!')
