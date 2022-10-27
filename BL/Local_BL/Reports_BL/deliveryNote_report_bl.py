from DAL.Local_DAL.Reports_DAL.deliveryNote_report_dal import DeliveryNote_report_DAL


class DeliveryNote_report_BL:
    def __init__(self):
        self.deliveryNote_report_dal = DeliveryNote_report_DAL()

    def get_deliveryNote(self, reportFilter, deliveryNoteNum2filter, season2filter):
        deliveryData = self.deliveryNote_report_dal.get_deliveryNote(
            reportFilter, deliveryNoteNum2filter, season2filter)
        recrodsList = []
        for record in deliveryData:
            dictRecord = {}
            dictRecord['palletNum'] = record[0]
            dictRecord['fruitName'] = record[1]
            dictRecord['fruitType'] = record[2]
            dictRecord['size'] = record[3]
            dictRecord['quality'] = record[4]
            dictRecord['marketPackingType'] = record[5]
            dictRecord['packMatQty'] = record[6]
            dictRecord['weightNeto'] = record[7]

            recrodsList.append(dictRecord)

        return recrodsList

    def get_deliveryNote2prct(self, reportFilter, deliveryNoteNum2filter, season2filter):
        deliveryData = self.deliveryNote_report_dal.get_deliveryNote(
            reportFilter, deliveryNoteNum2filter, season2filter)
        recrodsList = []
        for record in deliveryData:
            dictRecord = {}
            dictRecord['palletNum'] = record[0]
            dictRecord['fruitName'] = record[1]
            dictRecord['fruitType'] = record[2]
            dictRecord['size'] = record[3]
            dictRecord['quality'] = record[4]
            dictRecord['marketPackingType'] = record[5]
            dictRecord['packMatQty'] = record[6]
            dictRecord['weightNeto'] = record[7]
            dictRecord['weightNetoLess2prct'] = record[8]

            recrodsList.append(dictRecord)

        return recrodsList
