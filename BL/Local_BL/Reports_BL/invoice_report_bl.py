from DAL.Local_DAL.Reports_DAL.invoice_report_dal import Invoice_report_DAL


class Invoice_report_BL:
    def __init__(self):
        self.invoice_report_dal = Invoice_report_DAL()

    def get_invoiceLines(self, invoiceHeaderID):
        linesData = self.invoice_report_dal.get_invoiceLines(invoiceHeaderID)
        recrodsList = []
        for record in linesData:
            dictRecord = {}
            dictRecord['fruitName'] = record[0]
            dictRecord['fruitType'] = record[1]
            dictRecord['size'] = record[2]
            dictRecord['quality'] = record[3]
            dictRecord['palletNum'] = record[4]
            dictRecord['deliveryDate'] = record[5]
            dictRecord['deliveryNoteNum'] = record[6]
            dictRecord['closePrice'] = record[7]
            dictRecord['closeWeight'] = record[8]
            dictRecord['total'] = record[9]

            recrodsList.append(dictRecord)

        return recrodsList

    def get_palletCost(self, invoiceHeaderID):
        linesData = self.invoice_report_dal.get_palletCost(invoiceHeaderID)
        recrodsList = []
        for record in linesData:
            dictRecord = {}
            dictRecord['palletType'] = record[0]
            dictRecord['palletNum'] = record[1]
            dictRecord['palletMatCost'] = record[2]
            dictRecord['VAT'] = record[3]
            dictRecord['total'] = record[4]

            recrodsList.append(dictRecord)

        return recrodsList

    def get_resellerInfo(self, invoiceHeaderID):
        linesData = self.invoice_report_dal.get_resellerInfo(invoiceHeaderID)
        recrodsList = []
        for record in linesData:
            dictRecord = {}
            dictRecord['reseller_prct'] = record[0]
            dictRecord['total_reseller_fee'] = record[1]
            dictRecord['total_vat_cost'] = record[2]
            dictRecord['total_reduction_fee'] = record[3]

            recrodsList.append(dictRecord)

        return recrodsList
