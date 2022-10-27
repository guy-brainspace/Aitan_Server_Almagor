from DAL.Local_DAL.palletsMat_dal import PalletsMat_DAL


class PalletsMat_BL:
    def __init__(self):
        self.palletsMat_dal = PalletsMat_DAL()

    def get_palletsMat(self):
        pallets = self.palletsMat_dal.get_all_palletsMat()
        pallets_list = []
        for p in pallets:
            d = {}
            d['id'] = p.id
            d['palletType'] = p.palletType
            d['palletWeight'] = p.palletWeight
            d['isActive'] = p.isActive
            pallets_list.append(d)

        return pallets_list

    def add_palletMat(self, data):
        if data['palletWeight'] == '':
            data['palletWeight'] = 0
        record = {'palletType': data['palletType'],
                  'palletWeight': data['palletWeight'],  'isActive': data['isActive']}
        if (record['isActive'] == ''):
            record['isActive'] = False
        new_record = self.palletsMat_dal.add_palletMat(record)
        return new_record

    def delete_palletMat(self, id):
        status = self.palletsMat_dal.delete_palletMat(id)
        return status

    def update_palletMat(self, id, data):
        if data['palletWeight'] == '':
            data['palletWeight'] = 0
        status = self.palletsMat_dal.update_palletMat(id, data)
        return status
