from Models.Models import Receipt_lines
import datetime


class Receipt_lines_DAL():
    def __init__(self):
        pass

    def get_all_receipt_lines(self, receiptHeaderID):
        receipt_lines = Receipt_lines.query.filter(
            Receipt_lines.receiptHeaderID == receiptHeaderID).all()
        return receipt_lines

    def add_receipt_line(self, data):
        new_record = Receipt_lines(
            receiptHeaderID=data['receiptHeaderID'],
            paymentType=data['paymentType'],
            checkNum=data['checkNum'],
            bankName=data['bankName'],
            paymentDueDate=data['paymentDueDate'],
            sumPayment=data['sumPayment']
        )
        return new_record

    def delete_receipt_line(self, id):
        status = Receipt_lines.query.filter(Receipt_lines.id == id).delete()
        return status

    def delete_AllReceipt_lines(self, receiptHeaderID):
        status = Receipt_lines.query.filter(
            Receipt_lines.receiptHeaderID == receiptHeaderID).delete()
        return status

    def update_receipt_line(self,  lineID, data):
        record = Receipt_lines.query.filter_by(id=lineID).first()
        record.receiptHeaderID = data['receiptHeaderID']
        record.paymentType = data['paymentType']
        record.checkNum = data['checkNum']
        record.bankName = data['bankName']
        record.paymentDueDate = datetime.datetime(
            int(data['year']), int(data['month']), int(data['day']))
        record.sumPayment = data['sumPayment']

        return ('receipt was updated!')
