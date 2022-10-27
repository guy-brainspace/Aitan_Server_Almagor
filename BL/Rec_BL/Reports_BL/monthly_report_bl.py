from DAL.Rec_DAL.Reports_DAL.monthly_report_dal import Monthly_report_DAL


class Monthly_report_BL:
    def __init__(self):
        self.monthlyReport_dal = Monthly_report_DAL()

    def get_monthly_per_FruitType(self, season2filter, grower2filter, month2filter):
        monthylData = self.monthlyReport_dal.get_monthly_per_FruitType(
            season2filter, grower2filter, month2filter)
        recrodsList = []
        for record in monthylData:
            dictRecord = {}
            dictRecord['fruitName'] = record[0]
            dictRecord['fruitType'] = record[1]
            dictRecord['packingType'] = record[2]
            dictRecord['qtyInPacking'] = record[3]
            dictRecord['weightBruto'] = record[4]
            dictRecord['weightNeto'] = record[5]
            dictRecord['total_weight_to_pay'] = record[6]
            dictRecord['payment'] = record[7]

            recrodsList.append(dictRecord)

        return recrodsList

    def get_monthly_per_Deal(self, season2filter, grower2filter, month2filter):
        monthylData = self.monthlyReport_dal.get_monthly_per_Deal(
            season2filter, grower2filter, month2filter)
        recrodsList = []
        for record in monthylData:
            dictRecord = {}
            dictRecord['fruitName'] = record[0]
            dictRecord['fruitType'] = record[1]
            dictRecord['dealName'] = record[2]
            dictRecord['price1'] = record[3]
            dictRecord['price2'] = record[4]
            dictRecord['price3'] = record[5]
            dictRecord['packingType'] = record[6]
            dictRecord['qtyInPacking'] = record[7]
            dictRecord['weightBruto'] = record[8]
            dictRecord['weightNeto'] = record[9]
            dictRecord['total_weight_to_pay'] = record[10]
            dictRecord['payment'] = record[11]

            recrodsList.append(dictRecord)

        return recrodsList
