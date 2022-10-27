from DAL.Rec_DAL.Reports_DAL.summary_report_dal import Summary_report_DAL


class Summary_report_BL:
    def __init__(self):
        self.summaryReport_dal = Summary_report_DAL()

    def get_summary_monthly(self, season2filter, month2filter):
        summaryMonthlyData = self.summaryReport_dal.get_summary_monthly(
            season2filter, month2filter)
        recrodsList = []
        for record in summaryMonthlyData:
            dictRecord = {}
            dictRecord['fruitName'] = record[0]
            dictRecord['growerName'] = record[1]
            dictRecord['weightNeto'] = record[2]
            dictRecord['total_weight_to_pay'] = record[3]
            dictRecord['payment'] = record[4]

            recrodsList.append(dictRecord)

        return recrodsList

    def get_summary_packingHouse(self, season2filter):
        summaryPackingHouseData = self.summaryReport_dal.get_summary_packingHouse(
            season2filter)
        recrodsList = []
        for record in summaryPackingHouseData:
            dictRecord = {}
            dictRecord['fruitName'] = record[0]
            dictRecord['fruitType'] = record[1]
            dictRecord['packingHouseName'] = record[2]
            dictRecord['weightNeto'] = record[3]
            dictRecord['total_weight_to_pay'] = record[4]
            dictRecord['payment'] = record[5]

            recrodsList.append(dictRecord)

        return recrodsList

    def get_summary_season(self, season2filter):
        summarySeasonData = self.summaryReport_dal.get_summary_season(
            season2filter)
        recrodsList = []
        for record in summarySeasonData:
            dictRecord = {}
            dictRecord['fruitName'] = record[0]
            dictRecord['fruitType'] = record[1]
            dictRecord['weightNeto'] = record[2]
            dictRecord['total_weight_to_pay'] = record[3]
            dictRecord['payment'] = record[4]

            recrodsList.append(dictRecord)

        return recrodsList

    def get_summary_season_growers(self, season2filter):
        summarySeasonGrowersData = self.summaryReport_dal.get_summary_season_growers(
            season2filter)
        recrodsList = []
        for record in summarySeasonGrowersData:
            dictRecord = {}
            dictRecord['growerName'] = record[0]
            dictRecord['fruitName'] = record[1]
            dictRecord['fruitType'] = record[2]
            dictRecord['weightNeto'] = record[3]
            dictRecord['total_weight_to_pay'] = record[4]
            dictRecord['payment'] = record[5]

            recrodsList.append(dictRecord)

        return recrodsList

    def get_summary_monthly_packingMat(self, season2filter, month2filter):
        summaryMonthlyPackingMatData = self.summaryReport_dal.get_summary_monthly_packingMat(
            season2filter, month2filter)
        recrodsList = []
        for record in summaryMonthlyPackingMatData:
            dictRecord = {}
            dictRecord['growerName'] = record[0]
            dictRecord['מיכל'] = record[1]
            dictRecord['ארגז'] = record[2]
            dictRecord['weightBruto'] = record[3]
            dictRecord['weightNeto'] = record[4]
            dictRecord['total_weight_to_pay'] = record[5]

            recrodsList.append(dictRecord)

        return recrodsList
