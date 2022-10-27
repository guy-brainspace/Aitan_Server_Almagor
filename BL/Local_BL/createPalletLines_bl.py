from DAL.Local_DAL.createPalletLines_dal import FruitPalletCreation_lines_DAL as FPCL_DAL


class FruitPalletCreation_lines_BL:
    def __init__(self):
        self.fpcl_dal = FPCL_DAL()

    def get_fpcls(self, palletId):
        palletsCreations_lines = self.fpcl_dal.get_all_FPCL(palletId)
        palletsCreations_lines_list = []

        for pl in palletsCreations_lines:
            if len(pl.fruitPalletCreation_header.fruitDeliveryNote_rels) != 0:
                delivery_Note = pl.fruitPalletCreation_header.fruitDeliveryNote_rels[
                    0].deliveryNote_header.id
                deliveryNoteNum = pl.fruitPalletCreation_header.fruitDeliveryNote_rels[
                    0].deliveryNote_header.deliveryNoteNum
            else:
                delivery_Note = ''
                deliveryNoteNum = '-'

            d = {}
            d['id'] = pl.id
            d['fruitPalletCreation_headerID'] = pl.fruitPalletCreation_header.id
            d['season'] = pl.fruitPalletCreation_header.season
            d['palletNum'] = pl.fruitPalletCreation_header.palletNum
            d['matketFruitID'] = pl.market_fruits.id
            d['fruitName'] = pl.market_fruits.fruits.fruitName
            d['fruitType'] = pl.market_fruits.fruits.fruitType
            d['size'] = pl.market_fruits.fruitsize.size
            d['quality'] = pl.market_fruits.quality
            d['marketPackingMatType'] = pl.Market_packing_mat.marketPackingType
            d['marketPackingMatTypeID'] = pl.marketPackingMatTypeID
            d['packMatQty'] = pl.packMatQty
            d['weightNeto'] = pl.weightNeto
            d['deliveryNote_headerID'] = delivery_Note
            d['deliveryNoteNum'] = deliveryNoteNum
            palletsCreations_lines_list.append(d)

        return palletsCreations_lines_list

    def add_fpcl(self, data):
        new_record = self.fpcl_dal.add_FPCL(data)
        return new_record

    def delete_fpcl(self, id):
        status = self.fpcl_dal.delete_FPCL(id)
        return status

    def update_fpcl(self, id, data):
        status = self.fpcl_dal.update_FPCL(id, data)
        return status

    def delete_Allfpcl(self, palletID):
        status = self.fpcl_dal.delete_AllFPCL(palletID)
        return status
