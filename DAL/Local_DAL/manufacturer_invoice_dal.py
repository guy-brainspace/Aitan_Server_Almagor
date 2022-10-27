from Models.Models import Manufacturer_Invoice
import datetime


class Manufacturer_invoice_DAL():
    def __init__(self):
        pass

    def get_all_manufacturer_invoices(self, filteredSeason):
        invoices = Manufacturer_Invoice.query.filter(
            Manufacturer_Invoice.season == filteredSeason).all()
        return invoices

    def add_manufacturer_invoice(self, data):

        new_record = Manufacturer_Invoice(
            season=data['season'],
            ManufacturerInvNum=data['ManufacturerInvNum'],
            invoiceTotal=data['invoiceTotal'],
            invoiceDate=data['invoiceDate'],
            invoiceRemarks=data['invoiceRemarks']
        )
        return new_record

    def delete_manufacturer_invoice(self, id):
        status = Manufacturer_Invoice.query.filter(
            Manufacturer_Invoice.id == id).delete()
        return status

    def update_manufacturer_invoice(self, invoideid, data):
        record = Manufacturer_Invoice.query.filter_by(id=invoideid).first()
        record.season = data['season']
        record.ManufacturerInvNum = data['ManufacturerInvNum']
        record.invoiceTotal = data['invoiceTotal']
        record.invoiceDate = datetime.datetime(
            int(data['year']), int(data['month']), int(data['day']))
        record.invoiceRemarks = data['invoiceRemarks']
        return ('invoice was updated!')
