from DAL.Local_DAL.receiptLines_dal import Receipt_lines_DAL
import datetime


class Receipt_lines_BL:
    def __init__(self):
        self.receiptLine_dal = Receipt_lines_DAL()

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

    def get_receipt_lines(self, receiptHeaderID):
        receipt_lines = self.receiptLine_dal.get_all_receipt_lines(
            receiptHeaderID)
        receiptLines_list = []
        for r in receipt_lines:
            if r.checkNum == None:
                r.checkNum = ''
            if r.bankName == None:
                r.bankName = ''
            d = {}
            d['id'] = r.id
            d['receiptHeaderID'] = r.receiptHeaderID
            d['paymentType'] = r.paymentType
            d['checkNum'] = r.checkNum
            d['bankName'] = r.bankName
            d['paymentDueDate'] = r.paymentDueDate
            d['sumPayment'] = r.sumPayment

            receiptLines_list.append(d)

        return receiptLines_list

    def add_receipt_line(self, data):
        if "month" not in data:
            # data['paymentDueDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
            data['day'] = int(data['paymentDueDate'][5:7])
            data['month'] = self.monthToNum[(data['paymentDueDate'][8:11])]
            data['year'] = int(data['paymentDueDate'][12:16])
        data['paymentDueDate'] = datetime.datetime(
            data['year'], data['month'], data['day'])

        new_record = self.receiptLine_dal.add_receipt_line(data)
        return new_record

    def delete_receipt_line(self, id):
        status = self.receiptLine_dal.delete_receipt_line(id)
        return status

    def update_receipt_line(self, id, data):
        if "month" not in data:
            # data['paymentDueDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
            data['day'] = int(data['paymentDueDate'][5:7])
            data['month'] = self.monthToNum[(data['paymentDueDate'][8:11])]
            data['year'] = int(data['paymentDueDate'][12:16])

        status = self.receiptLine_dal.update_receipt_line(id, data)
        return status

    def delete_AllReceipt_lines(self, receiptHeaderID):
        status = self.receiptLine_dal.delete_AllReceipt_lines(receiptHeaderID)
        return status
