from DAL.Local_DAL.invoiceHeader_dal import Invoice_header_DAL
import datetime


class Invoice_header_BL:
    def __init__(self):
        self.invoice_header_dal = Invoice_header_DAL()
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

    def get_invoice_headers(self, filteredSeason):
        invoices = self.invoice_header_dal.get_all_invoice_headers(
            filteredSeason)
        invocies_list = []
        for i in invoices:
            d = {}
            d['id'] = i.id
            d['season'] = i.season
            d['invoiceNum'] = i.invoiceNum
            d['invoiceDate'] = i.invoiceDate
            d['traderID'] = i.traderID
            d['traderName'] = i.traders.traderName
            d['manufacturerInvoiceID'] = i.manufacturerInvoiceID
            d['invoiceStatus'] = i.invoiceStatus
            if i.manufacturerInvoiceID != None:
                d['ManufacturerInvNum'] = i.manufacturer_Invoice.ManufacturerInvNum
            else:
                d['ManufacturerInvNum'] = ''
                d['manufacturerInvoiceID'] = 0

            d['receiptNum'] = []

            if len(i.invoiceReceipt_header_rels) != 0:
                for receipt in i.invoiceReceipt_header_rels:
                    d['receiptNum'].append(receipt.receiptNum)

            invocies_list.append(d)

        return invocies_list

    def add_invoice_header(self, data):
        if "month" not in data:
            # data['invoiceDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
            data['day'] = int(data['invoiceDate'][5:7])
            data['month'] = self.monthToNum[(data['invoiceDate'][8:11])]
            data['year'] = int(data['invoiceDate'][12:16])
        data['invoiceDate'] = datetime.datetime(
            data['year'], data['month'], data['day'])
        if data['manufacturerInvoiceID'] == 0:
            data['manufacturerInvoiceID'] = None
        new_record = self.invoice_header_dal.add_invoice_header(data)
        return new_record

    def delete_invoice_header(self, id):
        status = self.invoice_header_dal.delete_invoice_header(id)
        return status

    def update_invoice_header(self, id, data):
        if "month" not in data:
            # data['invoiceDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
            data['day'] = int(data['invoiceDate'][5:7])
            data['month'] = self.monthToNum[(data['invoiceDate'][8:11])]
            data['year'] = int(data['invoiceDate'][12:16])
        if data['manufacturerInvoiceID'] == 0:
            data['manufacturerInvoiceID'] = None
        status = self.invoice_header_dal.update_invoice_header(id, data)
        return status

    def update_invoiceStatus(self, invoiceID, invoiceStatus):
        if invoiceStatus == 'פתוחה':
            invoiceStatus = 'סגורה'
        else:
            invoiceStatus = 'פתוחה'
        status = self.invoice_header_dal.update_invoiceStatus(
            invoiceID, invoiceStatus)
        return status
