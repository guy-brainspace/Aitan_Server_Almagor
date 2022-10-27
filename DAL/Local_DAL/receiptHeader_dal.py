from Models.Models import Receipt_header
import datetime


class Receipt_header_DAL():
    def __init__(self):
        pass

    def get_all_receipt_headers(self, filteredSeason):
        receipts = Receipt_header.query.filter(
            Receipt_header.season == filteredSeason).all()
        return receipts

    def add_receipt_header(self, data):
        new_record = Receipt_header(
            season=data['season'],
            receiptNum=data['receiptNum'],
            receiptDate=data['receiptDate'],
            invoiceHeaderID=data['invoiceHeaderID'],
            receiptRemarks=data['receiptRemarks']
        )
        return new_record

    def delete_receipt_header(self, id):
        deleted_record = Receipt_header.query.filter(
            Receipt_header.id == id).first()
        Receipt_header.query.filter(Receipt_header.id == id).delete()
        return deleted_record

    def update_receipt_header(self,  headerID, data):
        record = Receipt_header.query.filter_by(id=headerID).first()
        record.season = data['season']
        record.receiptNum = data['receiptNum'],
        record.receiptDate = datetime.datetime(
            int(data['year']), int(data['month']), int(data['day'])),
        record.invoiceHeaderID = data['invoiceHeaderID'],
        record.receiptRemarks = data['receiptRemarks'],
        return ('receipt header was updated!')
