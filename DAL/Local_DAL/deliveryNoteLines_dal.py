from Models.Models import DeliveryNote_lines as DNL


class DeliveryNote_lines_DAL():
    def __init__(self):
        pass

    def get_all_DNLs(self, deliveryNoteHeaderId):
        deliveryNotes_line = DNL.query.filter(
            DNL.deliveryNote_headerID == deliveryNoteHeaderId).all()
        return deliveryNotes_line

    def add_DNL(self, data):
        new_record = DNL(deliveryNote_headerID=data['deliveryNote_headerID'],
                         fruitPalletCreation_headerID=data['fruitPalletCreation_headerID']
                         )
        return new_record

    def delete_DNL(self, id):
        status = DNL.query.filter(DNL.id == id).delete()
        return status

    def delete_AllDNL(self, deliveryNoteHeaderId):
        status = DNL.query.filter(
            DNL.deliveryNote_headerID == deliveryNoteHeaderId).delete()
        return status

    def update_DNL(self,  lineID, data):
        record = DNL.query.filter_by(id=lineID).first()
        record.deliveryNote_headerID = data['deliveryNote_headerID']
        record.fruitPalletCreation_headerID = data['fruitPalletCreation_headerID']

        return ('deliveryNote line was updated!')
