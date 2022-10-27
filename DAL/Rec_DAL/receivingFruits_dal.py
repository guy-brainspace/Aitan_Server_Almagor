from Models.Models import Receiving_fruits
import datetime


class ReceivingFruits_DAL():
    def __init__(self):
        pass

    def get_all_receiving_fruits(self, filteredSeason):
        receivingFruits = Receiving_fruits.query.filter(
            Receiving_fruits.season == filteredSeason).all()
        return receivingFruits

    def add_receivingFruit(self, data):
        new_record = Receiving_fruits(
            receivingDate=data['receivingDate'],
            season=data['season'],
            growerID=data['growerID'],
            deliverNote=data['deliverNote'],
            packingHouseID=data['packingHouseID'],
            plotID=data['plotID'],
            fruitTypeID=data['fruitTypeID'],
            dealNameID=data['dealNameID'],
            packingMaterialID=data['packingMaterialID'],
            qtyInPacking=data['qtyInPacking'],
            weightBruto=data['weightBruto']
        )

        return new_record

    def delete_receivingFruit(self, id):
        status = Receiving_fruits.query.filter(
            Receiving_fruits.id == id).delete()
        return status

    def update_receivingFruit(self, receivingFruitid, data):
        record = Receiving_fruits.query.filter_by(id=receivingFruitid).first()
        record.receivingDate = datetime.datetime(
            int(data['year']), int(data['month']), int(data['day']))
        record.season = data['season']
        record.growerID = data['growerID']
        record.deliverNote = data['deliverNote']
        record.packingHouseID = data['packingHouseID']
        record.plotID = data['plotID']
        record.fruitTypeID = data['fruitTypeID']
        record.dealNameID = data['dealNameID']
        record.packingMaterialID = data['packingMaterialID']
        record.qtyInPacking = data['qtyInPacking']
        record.weightBruto = data['weightBruto']

        return (record)
