from DAL.Rec_DAL.Reports_DAL.daily_report_dal import Daily_report_DAL
import datetime


class Daily_report_BL:
    def __init__(self):
        self.dailyReport_dal = Daily_report_DAL()

    def get_daily_per_FruitName(self, date2filter, grower2filter):
        dateFilter = datetime.datetime(
            date2filter['year'], date2filter['month'], date2filter['day'])
        dailylData = self.dailyReport_dal.get_daily_per_fruitName(
            dateFilter, grower2filter)
        recrodsList = []
        for record in dailylData:
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
