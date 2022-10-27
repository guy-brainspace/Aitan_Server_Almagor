from DAL.Local_DAL.deliveryNoteHeader_dal import DeliveryNote_header_DAL as DNH_DAL
import datetime


class DeliveryNote_header_BL:
    def __init__(self):
        self.dnh_dal = DNH_DAL()
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

    def get_dnhs(self, filteredSeason):
        deliveryNotes = self.dnh_dal.get_all_DNH(filteredSeason)
        deliveryNotes_list = []
        for dn in deliveryNotes:
            d = {}
            d['id'] = dn.id
            d['season'] = dn.season
            d['deliveryNoteNum'] = dn.deliveryNoteNum
            d['deliveryDate'] = dn.deliveryDate
            d['traderID'] = dn.traderID
            d['traderName'] = dn.traders.traderName
            d['traderPrcnt'] = dn.traderPrcnt
            d['distributerPrcnt'] = dn.distributerPrcnt
            d['VAT'] = dn.VAT
            d['closingData'] = []
            d['invoiceNum'] = '-'  # []

            if len(dn.deliveryNote_header_rels) != 0:
                for i in dn.deliveryNote_header_rels:
                    if len(i.fruitPalletCreation.fruitPalletCreation_header_rels) != 0:
                        for t in i.fruitPalletCreation.fruitPalletCreation_header_rels:
                            if len(t.fruitPallet_lines_rels) != 0:
                                for closingDatarecord in t.fruitPallet_lines_rels:
                                    d['closingData'].append(
                                        closingDatarecord.id)

            if len(dn.invoice_header_deliveryNote_rels) != 0:
                d['invoiceNum'] = dn.invoice_header_deliveryNote_rels[0].invoice_header.invoiceNum

            deliveryNotes_list.append(d)

        return deliveryNotes_list

    def add_dnh(self, data):
        if "month" not in data:
            # data['deliveryDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
            data['day'] = int(data['deliveryDate'][5:7])
            data['month'] = self.monthToNum[(data['deliveryDate'][8:11])]
            data['year'] = int(data['deliveryDate'][12:16])
        data['deliveryDate'] = datetime.datetime(
            data['year'], data['month'], data['day'])
        new_record = self.dnh_dal.add_DNH(data)
        return new_record

    def delete_dnh(self, id):
        status = self.dnh_dal.delete_DNH(id)
        return status

    def update_dnh(self, id, data):
        if "month" not in data:
            # data['deliveryDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
            data['day'] = int(data['deliveryDate'][5:7])
            data['month'] = self.monthToNum[(data['deliveryDate'][8:11])]
            data['year'] = int(data['deliveryDate'][12:16])

        status = self.dnh_dal.update_DNH(id, data)
        return status

    # provide all the deliveryNotes that have lines

    def get_distinctdeliveryNoteWithLines(self, season):
        deliveryNoteHeaders = self.dnh_dal.get_all_DNH(season)
        deliveryNotesWithLines_list = []
        for d in deliveryNoteHeaders:
            if len(d.deliveryNote_header_rels) != 0:
                dict = {}
                dict['id'] = d.id
                dict['deliveryNoteID'] = d.id
                dict['deliveryNoteNum'] = d.deliveryNoteNum
                dict['traderName'] = d.traders.traderName
                if len(d.invoice_header_deliveryNote_rels) != 0:
                    dict['invoiceNum'] = d.invoice_header_deliveryNote_rels[0].invoice_header.invoiceNum
                else:
                    dict['invoiceNum'] = '-'

                deliveryNotesWithLines_list.append(dict)

        return deliveryNotesWithLines_list
