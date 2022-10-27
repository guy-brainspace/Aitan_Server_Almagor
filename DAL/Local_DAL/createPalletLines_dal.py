from Models.Models import FruitPalletCreation_lines as FPCL


class FruitPalletCreation_lines_DAL():
    def __init__(self):
        pass

    def get_all_FPCL(self, palletId):
        palletsCreations_line = FPCL.query.filter(
            FPCL.fruitPalletCreation_headerID == palletId).all()
        return palletsCreations_line

    def add_FPCL(self, data):
        new_record = FPCL(fruitPalletCreation_headerID=data['fruitPalletCreation_headerID'],
                          # fruitPalletLine= data['fruitPalletLine'],
                          matketFruitID=data['matketFruitID'],
                          marketPackingMatTypeID=data['marketPackingMatTypeID'],
                          packMatQty=data['packMatQty'],
                          weightNeto=data['weightNeto']
                          )
        return new_record

    def delete_FPCL(self, id):
        status = FPCL.query.filter(FPCL.id == id).delete()
        return status

    def delete_AllFPCL(self, palletID):
        status = FPCL.query.filter(
            FPCL.fruitPalletCreation_headerID == palletID).delete()
        return status

    def update_FPCL(self,  lineID, data):
        record = FPCL.query.filter_by(id=lineID).first()
        record.fruitPalletCreation_headerID = data['fruitPalletCreation_headerID']
        record.matketFruitID = data['matketFruitID'],
        record.marketPackingMatTypeID = data['marketPackingMatTypeID'],
        record.packMatQty = data['packMatQty'],
        record.weightNeto = data['weightNeto']

        return ('palletcreationLine was updated!')
