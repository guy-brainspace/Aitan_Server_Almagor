from Models.Models import Invoice_header
import datetime


class Invoice_header_DAL():
    def __init__(self):
        pass

    def get_all_invoice_headers(self, filteredSeason):
        deliveryNotes = Invoice_header.query.filter(
            Invoice_header.season == filteredSeason).all()
        return deliveryNotes

    def add_invoice_header(self, data):
        new_record = Invoice_header(
            season=data['season'],
            invoiceNum=data['invoiceNum'],
            invoiceDate=data['invoiceDate'],
            traderID=data['traderID'],
            manufacturerInvoiceID=data['manufacturerInvoiceID']
        )
        return new_record

    def delete_invoice_header(self, id):
        status = Invoice_header.query.filter(Invoice_header.id == id).delete()
        return status

    def update_invoice_header(self,  palletID, data):
        record = Invoice_header.query.filter_by(id=palletID).first()
        record.season = data['season']
        record.invoiceNum = data['invoiceNum'],
        record.invoiceDate = datetime.datetime(
            int(data['year']), int(data['month']), int(data['day'])),
        record.traderID = data['traderID'],
        record.manufacturerInvoiceID = data['manufacturerInvoiceID'],
        record.invoiceStatus = data['invoiceStatus']
        return ('invoice header was updated!')

    def update_invoiceStatus(self, invoiceID, status):
        record = Invoice_header.query.filter_by(id=invoiceID).first()
        record.invoiceStatus = status
        return ('invoice status was updated!')
