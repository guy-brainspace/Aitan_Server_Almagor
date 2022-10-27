from DAL.Local_DAL.deliveryNoteLines_dal import DeliveryNote_lines_DAL as DNL_DAL


class DeliveryNote_lines_BL:
    def __init__(self):
        self.dnl_dal = DNL_DAL()

    def get_dnls(self, deliveryNoteHeaderId):
        deliveryNote_lines = self.dnl_dal.get_all_DNLs(deliveryNoteHeaderId)
        createPalletLines_List = []
        for dnl in deliveryNote_lines:
            if len(dnl.fruitPalletCreation.fruitPalletCreation_header_rels) != 0:
                for i in dnl.fruitPalletCreation.fruitPalletCreation_header_rels:
                    createPalletLine_dict = {}
                    createPalletLine_dict['id'] = dnl.id
                    createPalletLine_dict['deliveryNote_headerID'] = dnl.deliveryNote_headerID
                    createPalletLine_dict['deliveryNoteNum'] = dnl.deliveryNote_header.deliveryNoteNum
                    createPalletLine_dict['palletNum'] = i.fruitPalletCreation_header.palletNum
                    createPalletLine_dict['fruitPalletCreation_headerID'] = dnl.fruitPalletCreation_headerID
                    createPalletLine_dict['fruitName'] = i.market_fruits.fruits.fruitName
                    createPalletLine_dict['fruitType'] = i.market_fruits.fruits.fruitType
                    createPalletLine_dict['size'] = i.market_fruits.fruitsize.size
                    createPalletLine_dict['quality'] = i.market_fruits.quality
                    createPalletLine_dict['packingMat'] = i.Market_packing_mat.marketPackingType
                    createPalletLine_dict['packMatQty'] = i.packMatQty
                    createPalletLine_dict['weightNeto'] = i.weightNeto
                    if len(i.fruitPallet_lines_rels) != 0:
                        createPalletLine_dict['closingDataID'] = i.fruitPallet_lines_rels[0].id
                    else:
                        createPalletLine_dict['closingDataID'] = None
                    createPalletLine_dict['invoiceNum'] = '-'  # []
                    createPalletLines_List.append(createPalletLine_dict)

        # add the line with the deliveryLine title
        delievryNote_list = []
        for dnl in deliveryNote_lines:
            dict = {}
            dict['id'] = dnl.id
            dict['deliveryNote_headerID'] = dnl.deliveryNote_headerID
            dict['palletNum'] = dnl.fruitPalletCreation.palletNum
            dict['fruitPalletCreation_headerID'] = dnl.fruitPalletCreation_headerID
            dict['deliveryNoteNum'] = dnl.deliveryNote_header.deliveryNoteNum
            dict['closingData'] = []
            dict['invoiceNum'] = '-'  # []

            if len(dnl.fruitPalletCreation.fruitPalletCreation_header_rels) != 0:
                for i in dnl.fruitPalletCreation.fruitPalletCreation_header_rels:
                    if len(i.fruitPallet_lines_rels) != 0:
                        for closingDatarecord in i.fruitPallet_lines_rels:
                            dict['closingData'].append(closingDatarecord.id)

            if len(dnl.deliveryNote_header.invoice_header_deliveryNote_rels) != 0:
                dict['invoiceNum'] = dnl.deliveryNote_header.invoice_header_deliveryNote_rels[0].invoice_header.invoiceNum

            delievryNote_list.append(dict)

        createPalletLines_List_with_palletNum = []
        for i in delievryNote_list:
            i['fruitName'] = ''
            i['fruitType'] = ''
            i['size'] = ''
            i['quality'] = ''
            i['packingMat'] = ''
            i['packMatQty'] = ''
            i['weightNeto'] = ''
            # add the line with the deliveryLine title
            createPalletLines_List_with_palletNum.append(i)
            for y in createPalletLines_List:
                if (i['palletNum'] == y['palletNum']):
                    # add the all the deliveryNote line connected to this palletNumber
                    createPalletLines_List_with_palletNum.append(y)

        return createPalletLines_List_with_palletNum

    def add_dnl(self, data):
        new_record = self.dnl_dal.add_DNL(data)
        return new_record

    def delete_dnl(self, id):
        status = self.dnl_dal.delete_DNL(id)
        return status

    def update_dnl(self, id, data):
        status = self.dnl_dal.update_DNL(id, data)
        return status

    def delete_Alldnl(self, palletID):
        status = self.dnl_dal.delete_AllDNL(palletID)
        return status
