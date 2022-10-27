from DAL.Local_DAL.closingData_dal import ClosingData_DAL
import datetime


class ClosingData_BL:
    def __init__(self):
        self.closingData_dal = ClosingData_DAL()
        self.monthToNum = {
            'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7,
            'Aug': 8,
            'Sep': 9,
            'Oct': 10,
            'Nov': 11,
            'Dec': 12
        }

    def get_all_closingData(self,  filteredSeason):
        closeData = self.closingData_dal.get_all_closingData(filteredSeason)
        recrodsList = []
        for record in closeData:
            dictRecord = {}
            dictRecord['id'] = record[0]
            dictRecord['season'] = record[1]
            dictRecord['deliveryNoteNum'] = record[2]
            dictRecord['fruitPalletCreationLineID'] = record[3]
            dictRecord['traderName'] = record[4]
            dictRecord['palletNum'] = record[5]
            dictRecord['fruitName'] = record[6]
            dictRecord['fruitType'] = record[7]
            dictRecord['size'] = record[8]
            dictRecord['quality'] = record[9]
            dictRecord['marketPackingType'] = record[10]
            dictRecord['packMatQty'] = record[11]
            dictRecord['weightNeto'] = record[12]
            dictRecord['closeWeight'] = record[13]
            dictRecord['closePrice'] = record[14]
            dictRecord['closeDate'] = record[15]
            dictRecord['closeRemarks'] = record[16]

            if dictRecord['closePrice'] == None:
                dictRecord['closePrice'] = ''
            if dictRecord['closeWeight'] == None:
                dictRecord['closeWeight'] = ''
            if dictRecord['closeRemarks'] == None:
                dictRecord['closeRemarks'] = ''

            recrodsList.append(dictRecord)

        return recrodsList

    def add_closingData(self, data):
        if data['closeDate'] != None:
            if "month" not in data:
                # data['closeDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
                data['day'] = int(data['closeDate'][5:7])
                data['month'] = self.monthToNum[(data['closeDate'][8:11])]
                data['year'] = int(data['closeDate'][12:16])

        else:
            today = datetime.datetime.now()
            data['day'] = today.day
            data['month'] = today.month
            data['year'] = today.year

        data['closeDate'] = datetime.datetime(
            data['year'], data['month'], data['day'])
        new_record = self.closingData_dal.add_closingData(data)
        return new_record

    def delete_closingData(self, id):
        status = self.closingData_dal.delete_closingData(id)
        return status

    def update_closingData(self, id, data):
        if "month" not in data:
            # data['closingDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
            data['day'] = int(data['closeDate'][5:7])
            data['month'] = self.monthToNum[(data['closeDate'][8:11])]
            data['year'] = int(data['closeDate'][12:16])
        status = self.closingData_dal.update_closingData(id, data)
        return status
