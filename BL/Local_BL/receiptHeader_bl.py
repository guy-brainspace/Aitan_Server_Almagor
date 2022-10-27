from DAL.Local_DAL.receiptHeader_dal import Receipt_header_DAL
import datetime


class Receipt_header_BL:
    def __init__(self):
        self.receipt_header_dal = Receipt_header_DAL()
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

    def get_receipt_headers(self, filteredSeason):
        receipts = self.receipt_header_dal.get_all_receipt_headers(
            filteredSeason)
        receipts_list = []
        for i in receipts:
            if i.receiptRemarks == None:
                i.receiptRemarks = ''
            d = {}
            d['id'] = i.id
            d['season'] = i.season
            d['receiptNum'] = i.receiptNum
            d['receiptDate'] = i.receiptDate
            d['invoiceHeaderID'] = i.invoiceHeaderID
            d['invoiceNum'] = i.invoice_header.invoiceNum
            d['receiptRemarks'] = i.receiptRemarks
            d['invoiceStatus'] = i.invoice_header.invoiceStatus

            receipts_list.append(d)

        return receipts_list

    def add_receipt_header(self, data):
        if "month" not in data:
            # data['receiptDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
            data['day'] = int(data['receiptDate'][5:7])
            data['month'] = self.monthToNum[(data['receiptDate'][8:11])]
            data['year'] = int(data['receiptDate'][12:16])
        data['receiptDate'] = datetime.datetime(
            data['year'], data['month'], data['day'])

        new_record = self.receipt_header_dal.add_receipt_header(data)
        return new_record

    def delete_receipt_header(self, id):
        deletedrecrod = self.receipt_header_dal.delete_receipt_header(id)
        return deletedrecrod

    def update_receipt_header(self, id, data):
        if "month" not in data:
            # data['receiptDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
            data['day'] = int(data['receiptDate'][5:7])
            data['month'] = self.monthToNum[(data['receiptDate'][8:11])]
            data['year'] = int(data['receiptDate'][12:16])

        status = self.receipt_header_dal.update_receipt_header(id, data)
        return status
