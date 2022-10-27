from DAL.Local_DAL.createPalletHeader_dal import FruitPalletCreation_header_DAL as FPCH_DAL
import datetime


class FruitPalletCreation_header_BL:
    def __init__(self):
        self.fpch_dal = FPCH_DAL()
        self.monthToNum = {
            'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7,
            'Aug': 8,
            'Sep': 9,
            'Oct': 10,
            'Nov': 11,
            'Dec': 12
        }

    def get_fpchs(self, filteredSeason):
        palletsCreations = self.fpch_dal.get_all_FPCH(filteredSeason)
        palletsCreations_list = []
        for p in palletsCreations:
            if p.palletRemarks == None:
                p.palletRemarks = ''
            if len(p.fruitDeliveryNote_rels) != 0:
                delivery_Note = p.fruitDeliveryNote_rels[0].deliveryNote_header.id
                deliveryNoteNum = p.fruitDeliveryNote_rels[0].deliveryNote_header.deliveryNoteNum
            else:
                delivery_Note = ''
                deliveryNoteNum = '-'

            d = {}
            d['id'] = p.id
            d['season'] = p.season
            d['palletNum'] = p.palletNum
            d['palletMatID'] = p.palletMatID
            d['palletMatType'] = p.palletsmat.palletType
            d['packingDate'] = p.packingDate
            d['palletRemarks'] = p.palletRemarks
            d['deliveryNote_headerID'] = delivery_Note
            d['deliveryNoteNum'] = deliveryNoteNum
            palletsCreations_list.append(d)

        return palletsCreations_list

    def add_fpch(self, data):
        if "month" not in data:
            # data['receivingDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
            data['day'] = int(data['packingDate'][5:7])
            data['month'] = self.monthToNum[(data['packingDate'][8:11])]
            data['year'] = int(data['packingDate'][12:16])
        data['packingDate'] = datetime.datetime(
            data['year'], data['month'], data['day'])
        new_record = self.fpch_dal.add_FPCH(data)
        return new_record

    def delete_fpch(self, id):
        status = self.fpch_dal.delete_FPCH(id)
        return status

    def update_fpch(self, id, data):
        if "month" not in data:
            # data['packingDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
            data['day'] = int(data['packingDate'][5:7])
            data['month'] = self.monthToNum[(data['packingDate'][8:11])]
            data['year'] = int(data['packingDate'][12:16])

        status = self.fpch_dal.update_FPCH(id, data)
        return status

    # provide all the pallets that have lines
    def get_PalletsNumWithLines(self, season):
        palletsHeaders = self.fpch_dal.get_all_FPCH(season)
        palletsWithLines_list = []
        for p in palletsHeaders:

            if len(p.fruitPalletCreation_header_rels) != 0:
                if len(p.fruitDeliveryNote_rels) != 0:
                    delivery_Note = p.fruitDeliveryNote_rels[0].deliveryNote_header.id
                    deliveryNoteNum = p.fruitDeliveryNote_rels[0].deliveryNote_header.deliveryNoteNum
                else:
                    delivery_Note = ''
                    deliveryNoteNum = '-'
                d = {}
                d['id'] = p.id
                d['fruitPalletCreation_headerID'] = p.id
                d['palletNum'] = p.palletNum
                d['deliveryNote_headerID'] = delivery_Note
                d['deliveryNoteNum'] = deliveryNoteNum
                palletsWithLines_list.append(d)

        # remove duplications from palletsWithLines_list
        seen = set()
        distinct_list = []
        for d in palletsWithLines_list:
            t = tuple(d.items())
            if t not in seen:
                seen.add(t)
                distinct_list.append(d)

        return distinct_list
