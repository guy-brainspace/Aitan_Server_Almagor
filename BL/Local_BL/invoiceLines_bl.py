from DAL.Local_DAL.invoiceLines_dal import Invoice_lines_DAL


class Invoice_lines_BL:
    def __init__(self):
        self.invoiceLine_dal = Invoice_lines_DAL()

    def get_invoice_lines(self, invoiceHeaderID):
        invoice_lines = self.invoiceLine_dal.get_all_invoice_lines(
            invoiceHeaderID)
        invoiceLines_List = []
        for line in invoice_lines:
            if len(line.deliveryNote_header.deliveryNote_header_rels) != 0:
                for i in line.deliveryNote_header.deliveryNote_header_rels:
                    if len(i.fruitPalletCreation.fruitPalletCreation_header_rels) != 0:
                        for record in i.fruitPalletCreation.fruitPalletCreation_header_rels:
                            invoice_dict = {}
                            invoice_dict['id'] = line.id
                            invoice_dict['invoiceHeaderID'] = line.invoiceHeaderID
                            invoice_dict['deliveryNoteNum'] = i.deliveryNote_header.deliveryNoteNum
                            invoice_dict['invoiceNum'] = line.invoice_header.invoiceNum
                            invoice_dict['palletNum'] = record.fruitPalletCreation_header.palletNum
                            invoice_dict['fruitName'] = record.market_fruits.fruits.fruitName
                            invoice_dict['fruitType'] = record.market_fruits.fruits.fruitType
                            invoice_dict['size'] = record.market_fruits.fruitsize.size
                            invoice_dict['quality'] = record.market_fruits.quality
                            if len(record.fruitPallet_lines_rels) != 0:
                                invoice_dict['closePrice'] = record.fruitPallet_lines_rels[0].closePrice
                                invoice_dict['closeWeight'] = record.fruitPallet_lines_rels[0].closeWeight
                            else:
                                invoice_dict['closePrice'] = '-'
                                invoice_dict['closeWeight'] = '-'
                            invoiceLines_List.append(invoice_dict)
                            if len(line.invoice_header.invoiceReceipt_header_rels) !=0:
                                invoice_dict['receiptNum'] = 'availableReceipt'
                            else:
                                invoice_dict['receiptNum'] = ''
        # add the line with the invoicesLine title
        lines_list = []
        for line in invoice_lines:
            if len(line.deliveryNote_header.deliveryNote_header_rels) != 0:
                dict = {}
                dict['id'] = line.id
                dict['invoiceHeaderID'] = line.invoiceHeaderID
                dict['deliveryNoteNum'] = line.deliveryNote_header.deliveryNoteNum
                dict['invoiceNum'] = line.invoice_header.invoiceNum
                if len(line.invoice_header.invoiceReceipt_header_rels) !=0:
                    dict['receiptNum'] = 'availableReceipt'
                else:
                    dict['receiptNum'] = ''
                lines_list.append(dict)

        #create a list with the titles and the actual lines
        lines_List_with_onlydeliveryNum = []
        for i in lines_list:
            i['palletNum'] = ''
            i['fruitName'] = ''
            i['fruitType'] = ''
            i['size'] = ''
            i['quality'] = ''
            i['closePrice'] = ''
            i['closeWeight'] = ''
            lines_List_with_onlydeliveryNum.append(i)
            for y in invoiceLines_List:
                if (i['deliveryNoteNum'] == y['deliveryNoteNum']):
                    lines_List_with_onlydeliveryNum.append(y)

        return lines_List_with_onlydeliveryNum

    def add_invoice_line(self, data):
        new_record = self.invoiceLine_dal.add_invoice_line(data)
        return new_record

    def delete_invoice_line(self, id):
        status = self.invoiceLine_dal.delete_invoice_line(id)
        return status

    def update_invoice_line(self, id, data):
        status = self.invoiceLine_dal.update_invoice_line(id, data)
        return status

    def delete_AllInvoice_lines(self, invoiceHeader):
        status = self.invoiceLine_dal.delete_AllInvoice_lines(invoiceHeader)
        return status
