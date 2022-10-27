from DAL.Rec_DAL.Reports_DAL.season_report_dal import Season_report_DAL

class Season_report_BL:
    def __init__(self):
        self.SeasonReport_dal = Season_report_DAL()

    def get_season_per_FruitName(self, season2filter, grower2filter):
        seasonData = self.SeasonReport_dal.get_season_per_fruitName(
            season2filter, grower2filter)
        recrodsList = []
        for record in seasonData:
            dictRecord = {}
            dictRecord['fruitName'] = record[0]
            dictRecord['fruitType'] = record[1]
            dictRecord['dealName'] = record[2]
            dictRecord['packingType'] = record[3]
            dictRecord['qtyInPacking'] = record[4]
            dictRecord['total_weight_to_pay'] = record[5]
            dictRecord['price1'] = record[6]
            dictRecord['price2'] = record[7]
            dictRecord['price3'] = record[8]
            dictRecord['total_price'] = record[9]
            dictRecord['payment1'] = record[10]
            dictRecord['payment2'] = record[11]
            dictRecord['payment3'] = record[12]
            dictRecord['payment'] = record[13]

            recrodsList.append(dictRecord)

        return recrodsList
