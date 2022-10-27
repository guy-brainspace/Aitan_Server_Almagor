from DAL.Local_DAL.Reports_DAL.palletsWOinvoices_report_dal import Pallets_wo_invoices_DAL
import datetime


class Pallets_wo_invoices_BL:
    def __init__(self):
        self.pallets_wo_invoices_dal = Pallets_wo_invoices_DAL()

    def get_palletsWOinvoices(self, fromDateFilter_dict, toDateFilter_dict, traderID):
        fromDate = datetime.datetime(
            fromDateFilter_dict['year'], fromDateFilter_dict['month'], fromDateFilter_dict['day'])
        toDate = datetime.datetime(
            toDateFilter_dict['year'], toDateFilter_dict['month'], toDateFilter_dict['day'])
        palletsList = self.pallets_wo_invoices_dal.get_palletsWOinvoices(
            fromDate, toDate, traderID)
        recrodsList = []
        for record in palletsList:
            dictRecord = {}
            dictRecord['deliveryDate'] = record[0]
            dictRecord['deliveryNoteNum'] = record[1]
            dictRecord['palletNum'] = record[2]
            dictRecord['fruitName'] = record[3]
            dictRecord['fruitType'] = record[4]
            dictRecord['size'] = record[5]
            dictRecord['quality'] = record[6]

            recrodsList.append(dictRecord)

        return recrodsList
