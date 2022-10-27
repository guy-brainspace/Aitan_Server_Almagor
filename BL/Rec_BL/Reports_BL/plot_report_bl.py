from DAL.Rec_DAL.Reports_DAL.plot_report_dal import Plot_report_DAL
import datetime


class Plot_report_BL:
    def __init__(self):
        self.plot_report_DAL = Plot_report_DAL()

    def get_plot_per_dates(self,  plotName2Filter, fromDate2filter, toDate2filter):
        fromDate = datetime.datetime(
            fromDate2filter['year'], fromDate2filter['month'], fromDate2filter['day'])
        toDate = datetime.datetime(
            toDate2filter['year'], toDate2filter['month'], toDate2filter['day'])
        plotData = self.plot_report_DAL.get_plot_per_dates(
            plotName2Filter, fromDate, toDate)
        recrodsList = []
        for record in plotData:
            dictRecord = {}
            dictRecord['plotName'] = record[0]
            dictRecord['packingType'] = record[1]
            dictRecord['fruitName'] = record[2]
            dictRecord['fruitType'] = record[3]
            dictRecord['receivingDate'] = record[4]
            dictRecord['qtyInPacking'] = record[5]
            dictRecord['weightBruto'] = record[6]
            dictRecord['weightNeto'] = record[7]
            dictRecord['total_weight_to_pay'] = record[8]

            recrodsList.append(dictRecord)

        return recrodsList

    def get_plots_per_dates(self, fromDate2filter, toDate2filter):
        fromDate = datetime.datetime(
            fromDate2filter['year'], fromDate2filter['month'], fromDate2filter['day'])
        toDate = datetime.datetime(
            toDate2filter['year'], toDate2filter['month'], toDate2filter['day'])
        plotsData = self.plot_report_DAL.get_plots_per_dates(fromDate, toDate)
        recrodsList = []
        for record in plotsData:
            dictRecord = {}
            dictRecord['plotName'] = record[0]
            dictRecord['packingType'] = record[1]
            dictRecord['fruitName'] = record[2]
            dictRecord['fruitType'] = record[3]
            dictRecord['receivingDate'] = record[4]
            dictRecord['qtyInPacking'] = record[5]
            dictRecord['weightBruto'] = record[6]
            dictRecord['weightNeto'] = record[7]
            dictRecord['total_weight_to_pay'] = record[8]

            recrodsList.append(dictRecord)

        return recrodsList
