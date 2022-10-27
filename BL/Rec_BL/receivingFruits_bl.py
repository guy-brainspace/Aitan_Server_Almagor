from DAL.Rec_DAL.receivingFruits_dal import ReceivingFruits_DAL
import datetime


class ReceivingFruits_BL:
    def __init__(self):
        self.receivingFruits_dal = ReceivingFruits_DAL()
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

    def get_receivingFruits(self, filteredSeason):
        receivingFruits = self.receivingFruits_dal.get_all_receiving_fruits(
            filteredSeason)
        receivingFruits_list = []
        for rec_fruit in receivingFruits:
            d = {}
            d['id'] = rec_fruit.id
            d['receivingDate'] = rec_fruit.receivingDate
            d['season'] = rec_fruit.season
            d['growerID'] = rec_fruit.growerID
            d['growerName'] = rec_fruit.growers.growerName
            d['deliverNote'] = rec_fruit.deliverNote
            d['packingHouseID'] = rec_fruit.packingHouseID
            d['packingHouseName'] = rec_fruit.packinghouse.packingHouseName
            d['packingHouselocation'] = rec_fruit.packinghouse.location
            d['plotID'] = rec_fruit.plotID
            d['plotName'] = rec_fruit.plots.plotName
            d['fruitTypeID'] = rec_fruit.fruitTypeID
            d['fruitName'] = rec_fruit.fruits.fruitName
            d['fruitType'] = rec_fruit.fruits.fruitType
            d['dealNameID'] = rec_fruit.dealNameID
            d['dealName'] = rec_fruit.dealNames.dealName
            d['packingMaterialID'] = rec_fruit.packingMaterialID
            d['packingType'] = rec_fruit.packing_mat.packingType
            d['qtyInPacking'] = rec_fruit.qtyInPacking
            d['weightBruto'] = rec_fruit.weightBruto
            receivingFruits_list.append(d)

        return receivingFruits_list

    def add_receivingFruit(self, data):
        if "month" not in data:
            # data['receivingDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
            data['day'] = int(data['receivingDate'][5:7])
            data['month'] = self.monthToNum[(data['receivingDate'][8:11])]
            data['year'] = int(data['receivingDate'][12:16])
        data['receivingDate'] = datetime.datetime(
            data['year'], data['month'], data['day'])

        if data['qtyInPacking'] == '':
            data['qtyInPacking'] = 0
        else:
            data['qtyInPacking'] = data['qtyInPacking']

        if data['weightBruto'] == '':
            data['weightBruto'] = 0
        else:
            data['weightBruto'] = data['weightBruto']

        add_record = self.receivingFruits_dal.add_receivingFruit(data)
        return add_record

    def delete_receivingFruit(self, id):
        status = self.receivingFruits_dal.delete_receivingFruit(id)
        return status

    def update_receivingFruit(self, id, data):
        # in case the user didnt want to update the receiving date - so we didnt receive a new one from the client
        if "month" not in data:
            # data['receivingDate'] ='Thu, 01 Sep 2022 00:00:00 GMT'
            data['day'] = int(data['receivingDate'][5:7])
            data['month'] = self.monthToNum[(data['receivingDate'][8:11])]
            data['year'] = int(data['receivingDate'][12:16])

        if data['qtyInPacking'] == '':
            data['qtyInPacking'] = 0

        if data['weightBruto'] == '':
            data['weightBruto'] = 0

        status = self.receivingFruits_dal.update_receivingFruit(id, data)
        return status
