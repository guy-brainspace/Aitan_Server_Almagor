from DAL.Local_DAL.manufacturer_invoice_dal import Manufacturer_invoice_DAL
import datetime


class Manufacturer_invoice_BL:
    def __init__(self):
        self.manufacturer_invoice_dal = Manufacturer_invoice_DAL()
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

    def get_all_manufacturer_invoices(self, filteredSeason):
        invoices = self.manufacturer_invoice_dal.get_all_manufacturer_invoices(
            filteredSeason)
        invoice_list = []
        for i in invoices:
            if i.invoiceRemarks == None:
                i.invoiceRemarks = ''
            d = {}
            d['id'] = i.id
            d['season'] = i.season
            d['ManufacturerInvNum'] = i.ManufacturerInvNum
            d['invoiceTotal'] = i.invoiceTotal
            d['invoiceDate'] = i.invoiceDate
            d['invoiceRemarks'] = i.invoiceRemarks
            invoice_list.append(d)

        return invoice_list

    def add_manufacturer_invoice(self, data):
        if "month" not in data:
            # data['invoiceDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
            data['day'] = int(data['invoiceDate'][5:7])
            data['month'] = self.monthToNum[(data['invoiceDate'][8:11])]
            data['year'] = int(data['invoiceDate'][12:16])
        data['invoiceDate'] = datetime.datetime(
            data['year'], data['month'], data['day'])
        new_record = self.manufacturer_invoice_dal.add_manufacturer_invoice(
            data)
        return new_record

    def delete_manufacturer_invoice(self, id):
        status = self.manufacturer_invoice_dal.delete_manufacturer_invoice(id)
        return status

    def update_manufacturer_invoice(self, id, data):
        if "month" not in data:
            # data['invoiceDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
            data['day'] = int(data['invoiceDate'][5:7])
            data['month'] = self.monthToNum[(data['invoiceDate'][8:11])]
            data['year'] = int(data['invoiceDate'][12:16])
        status = self.manufacturer_invoice_dal.update_manufacturer_invoice(
            id, data)
        return status
