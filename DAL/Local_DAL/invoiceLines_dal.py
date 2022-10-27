from Models.Models import Invoice_lines


class Invoice_lines_DAL():
    def __init__(self):
        pass

    def get_all_invoice_lines(self, invoiceHeaderID):
        invoice_lines = Invoice_lines.query.filter(
            Invoice_lines.invoiceHeaderID == invoiceHeaderID).all()
        return invoice_lines

    def add_invoice_line(self, data):
        new_record = Invoice_lines(invoiceHeaderID=data['invoiceHeaderID'],
                                   deliveryNote_headerID=data['deliveryNote_headerID']
                                   )
        return new_record

    def delete_invoice_line(self, id):
        status = Invoice_lines.query.filter(Invoice_lines.id == id).delete()
        return status

    def delete_AllInvoice_lines(self, invoiceHeaderID):
        status = Invoice_lines.query.filter(
            Invoice_lines.invoiceHeaderID == invoiceHeaderID).delete()
        return status

    def update_invoice_line(self,  lineID, data):
        record = Invoice_lines.query.filter_by(id=lineID).first()
        record.invoiceHeaderID = data['invoiceHeaderID']
        record.deliveryNote_headerID = data['deliveryNote_headerID']

        return ('invoice was updated!')
