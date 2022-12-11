import json
import os

from BL.Users_BL.auth_bl import Auth_BL

from BL.Rec_BL.packingMaterials_bl import PackingMaterials_BL
# from BL.Rec_BL.plots_bl import Plots_BL
from BL.Rec_BL.plotsDunam_bl import PlotsDunam_BL
from BL.Rec_BL.fruits_bl import Fruits_BL
from BL.Rec_BL.packingHouse_bl import PackingHouse_BL
from BL.Rec_BL.growers_bl import Growers_BL
from BL.Rec_BL.dealNames_bl import DealNames_BL
from BL.Rec_BL.receivingFruits_bl import ReceivingFruits_BL
from BL.Rec_BL.deals_bl import Deals_BL

from BL.Rec_BL.Reports_BL.monthly_report_bl import Monthly_report_BL
from BL.Rec_BL.Reports_BL.daily_report_bl import Daily_report_BL
from BL.Rec_BL.Reports_BL.season_report_bl import Season_report_BL
from BL.Rec_BL.Reports_BL.summary_report_bl import Summary_report_BL
from BL.Rec_BL.Reports_BL.plot_report_bl import Plot_report_BL

from BL.Local_BL.fixedInfo_bl import FixedInfo_BL
from BL.Local_BL.fruitSize_bl import FruitSize_BL
from BL.Local_BL.traders_bl import Traders_BL
from BL.Local_BL.palletsMat_bl import PalletsMat_BL
from BL.Local_BL.palletsMatCost_bl import PalletsMatCost_BL
from BL.Local_BL.market_packing_mat_bl import Market_packing_mat_bl
from BL.Local_BL.market_fruits_bl import Market_fruits_BL
from BL.Local_BL.createPalletHeader_bl import FruitPalletCreation_header_BL
from BL.Local_BL.createPalletLines_bl import FruitPalletCreation_lines_BL
from BL.Local_BL.deliveryNoteHeader_bl import DeliveryNote_header_BL
from BL.Local_BL.deliveryNoteLines_bl import DeliveryNote_lines_BL
from BL.Local_BL.manufacturer_invoice_bl import Manufacturer_invoice_BL
from BL.Local_BL.closingData_bl import ClosingData_BL
from BL.Local_BL.invoiceHeader_bl import Invoice_header_BL
from BL.Local_BL.invoiceLines_bl import Invoice_lines_BL
from BL.Local_BL.receiptHeader_bl import Receipt_header_BL
from BL.Local_BL.receiptLines_bl import Receipt_lines_BL


from BL.Local_BL.Reports_BL.deliveryNote_report_bl import DeliveryNote_report_BL
from BL.Local_BL.Reports_BL.invoice_report_bl import Invoice_report_BL

from BL.Local_BL.Reports_BL.palletsWOinvoices_report_bl import Pallets_wo_invoices_BL

from confdb import db
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # init the DB
db.app = app
db.init_app(app)

auth_bl = Auth_BL()


growers_bl = Growers_BL()
packingHouse_bl = PackingHouse_BL()
fruits_bl = Fruits_BL()
# plots_bl = Plots_BL()
plotsDunam_bl = PlotsDunam_BL()
packingMaterials_bl = PackingMaterials_BL()
dealNames_bl = DealNames_BL()
receivingFruits_bl = ReceivingFruits_BL()
deals_bl = Deals_BL()

monthlyReport_bl = Monthly_report_BL()
dailyReport_bl = Daily_report_BL()
seasonReport_bl = Season_report_BL()
summaryReport_bl = Summary_report_BL()
plot_report_BL = Plot_report_BL()

fixedInfo_bl = FixedInfo_BL()
fruitSize_bl = FruitSize_BL()
traders_bl = Traders_BL()
palletsMat_bl = PalletsMat_BL()
palletsMatCost_bl = PalletsMatCost_BL()
market_packing_mat_bl = Market_packing_mat_bl()
market_fruits_bl = Market_fruits_BL()
palletCreation_header_bl = FruitPalletCreation_header_BL()
palletCreation_lines_bl = FruitPalletCreation_lines_BL()
deliveryNote_header_bl = DeliveryNote_header_BL()
deliveryNote_lines_bl = DeliveryNote_lines_BL()
manufacturer_invoice_bl = Manufacturer_invoice_BL()
closingData_bl = ClosingData_BL()
invoice_header_bl = Invoice_header_BL()
invoice_lines_bl = Invoice_lines_BL()
receipt_header_bl = Receipt_header_BL()
receipt_lines_bl = Receipt_lines_BL()


deliveryNote_report_bl = DeliveryNote_report_BL()
invoice_report_bl = Invoice_report_BL()
pallets_wo_invoices_bl = Pallets_wo_invoices_BL()

# =================================================================================================
#          L o g i n
# =================================================================================================


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data["userName"]
    passowrd = data["password"]
    token = auth_bl.get_token(username, passowrd)
    if token != -1:
        return token
    else:
        return jsonify(-1)


@app.route('/login', methods=['GET'])
def get_login():
    userData = auth_bl.token_verification()
    if userData == "not authorized":
        return jsonify("you are not authorized")
    else:
        return jsonify(userData)


# =================================================================================================
#          R e c e i v i n g     F r u i t s    t a b l e s
# =================================================================================================


# =======================================================
# =============== growers ===============================


@app.route('/growers', methods=['GET'])
def get_growers():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        data = growers_bl.get_growers()
        return jsonify(data)


@app.route('/growers', methods=['POST'])
def add_grower():
    data = request.json
    if (data['growerName'] == ''):
        return jsonify("issueWithFieldData")
    else:
        new_record = growers_bl.add_grower(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/growers/<string:id>', methods=['PUT'])
def update_grower(id):
    data = request.json
    if (data['growerName'] == ''):
        return jsonify("issueWithFieldData")
    else:
        try:
            growers_bl.update_grower(id, data)
            db.session.commit()
            return jsonify("updated grower")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/growers/<string:id>', methods=['DELETE'])
def delete_grower_data(id):
    growers_bl.delete_grower(id)
    db.session.commit()
    return jsonify("deleted grower")

# =======================================================
# =============== packingHouse ==========================


@app.route('/packingHouse', methods=['GET'])
def get_packingHouse():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        data = packingHouse_bl.get_packingHouses()
        return jsonify(data)


@app.route('/packingHouse', methods=['POST'])
def add_packingHouse():
    data = request.json
    if (data['packingHouseName'] == ''):
        return jsonify("issueWithFieldData")
    else:
        new_record = packingHouse_bl.add_packingHouse(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/packingHouse/<string:id>', methods=['PUT'])
def update_packingHouse(id):
    data = request.json
    if (data['packingHouseName'] == ''):
        return jsonify("issueWithFieldData")
    else:
        packingHouse_bl.update_packingHouse(id, data)
        try:
            db.session.commit()
            return jsonify("updated packingHouse")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/packingHouse/<string:id>', methods=['DELETE'])
def delete_packingHouse(id):
    packingHouse_bl.delete_packingHouse(id)
    db.session.commit()
    return jsonify("deleted packingHouse")


# =======================================================
# =============== fruits ================================

@app.route('/fruits', methods=['GET'])
def get_fruit():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        data = fruits_bl.get_fruits()
        return jsonify(data)


@app.route('/fruits', methods=['POST'])
def add_fruit():
    data = request.json
    if (data['fruitName'] == 'בחר פרי' or data['fruitName'] == ''):
        return jsonify("issueWithFieldData")
    else:
        new_record = fruits_bl.add_fruit(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/fruits/<string:id>', methods=['PUT'])
def update_fruit(id):
    data = request.json
    if (data['fruitName'] == 'בחר פרי'):
        return jsonify("issueWithFieldData")
    else:
        fruits_bl.update_fruit(id, data)
        try:
            db.session.commit()
            return jsonify("updated fruit")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/fruits/<string:id>', methods=['DELETE'])
def delete_fruit(id):
    fruits_bl.delete_fruit(id)
    db.session.commit()
    return jsonify("deleted fruit")


# =======================================================
# =============== plots =================================


# @app.route('/plots', methods=['GET'])
# def get_plots():
#     resp = auth_bl.token_verification()
#     if resp == "not authorized":
#         return jsonify("The user is not autorized")
#     else:
#         data = plots_bl.get_plots()
#         return jsonify(data)


# @app.route('/plots', methods=['POST'])
# def add_plot():
#     data = request.json
#     if (data['plotName'] == ''):
#         return jsonify("issueWithFieldData")
#     else:
#         new_record = plots_bl.add_plot(data)
#         db.session.add(new_record)
#         try:
#             db.session.commit()
#             return jsonify(new_record.id)  # return the id of the added item
#         except:
#             db.session.rollback()
#             return jsonify("issueWithRecord")


# @app.route('/plots/<string:id>', methods=['PUT'])
# def update_plot(id):
#     data = request.json
#     if (data['plotName'] == ''):
#         return jsonify("issueWithFieldData")
#     else:
#         plots_bl.update_plot(id, data)
#         try:
#             db.session.commit()
#             return jsonify("updated plot")
#         except:
#             db.session.rollback()
#             return jsonify("issueWithRecord")


# @app.route('/plots/<string:id>', methods=['DELETE'])
# def delete_plot(id):
#     plots_bl.delete_plot(id)
#     db.session.commit()
#     return jsonify("deleted plot")

    
# =======================================================
# =============== plotsdunam =================================


@app.route('/plots', methods=['GET'])
def get_plots():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        # data = plots_bl.get_plots()
        filteredSeason = int(request.args.get('season2filter'))
        data = plotsDunam_bl.get_plots(filteredSeason)
        return jsonify(data)


@app.route('/plots/<string:filteredPrevSeason>', methods=['POST'])
def copy_prev_years_plots(filteredPrevSeason):
    new_record=plotsDunam_bl.copy_prev_years_plots(filteredPrevSeason)
    db.session.add_all(new_record)
    try:
        db.session.commit()
        return jsonify("copy all plots from prev year")
    except:
        db.session.rollback()
        return jsonify("issueWithRecord")


@app.route('/plots', methods=['POST'])
def add_plot():
    data = request.json
    #if (data['plotName'] == '':
    if (data['plotName'] == '' or data['season'] == '' or data['fruitTypeID']=='' or data['plantYear']==''):
        return jsonify("issueWithFieldData")
    else:
        # new_record = plots_bl.add_plot(data)
        new_record = plotsDunam_bl.add_plot(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/plots/<string:id>', methods=['PUT'])
def update_plot(id):
    data = request.json
    #if (data['plotName'] == '':
    if (data['plotName'] == '' or data['season'] == '' or data['fruitTypeID']=='' or data['plantYear']==''):
        return jsonify("issueWithFieldData")
    else:
        plotsDunam_bl.update_plot(id, data)
        try:
            db.session.commit()
            return jsonify("updated plot")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/plots/<string:id>', methods=['DELETE'])
def delete_plot(id):
    # plots_bl.delete_plot(id)
    plotsDunam_bl.delete_plot(id)
    db.session.commit()
    return jsonify("deleted plot")


# =======================================================
# =============== packingMaterials ======================


@app.route('/packingMaterials', methods=['GET'])
def get_packingMaterials():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        data = packingMaterials_bl.get_packingMaterials()
        return jsonify(data)


@app.route('/packingMaterials', methods=['POST'])
def add_packingMaterial():
    data = request.json
    if (data['packingType'] == ''):
        return jsonify("issueWithFieldData")
    else:
        new_record = packingMaterials_bl.add_packingMaterial(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/packingMaterials/<string:id>', methods=['PUT'])
def update_packingMaterial(id):
    data = request.json
    if (data['packingType'] == ''):
        return jsonify("issueWithFieldData")
    else:
        packingMaterials_bl.update_packingMaterial(id, data)
        try:
            db.session.commit()
            return jsonify("updated packingMaterial")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/packingMaterials/<string:id>', methods=['DELETE'])
def delete_packingMaterial(id):
    packingMaterials_bl.delete_packingMaterial(id)
    db.session.commit()
    return jsonify("deleted packingMaterial")


# =======================================================
# =============== dealNames =============================


@app.route('/dealNames', methods=['GET'])
def get_dealNames():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        data = dealNames_bl.get_dealNames()
        return jsonify(data)


@app.route('/dealNames', methods=['POST'])
def add_dealName():
    data = request.json
    if (data['dealName'] == ''):
        return jsonify("issueWithFieldData")
    else:
        new_record = dealNames_bl.add_dealName(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/dealNames/<string:id>', methods=['PUT'])
def update_dealName(id):
    data = request.json
    if (data['dealName'] == ''):
        return jsonify("issueWithFieldData")
    else:
        dealNames_bl.update_dealName(id, data)
        try:
            db.session.commit()
            return jsonify("updated dealName")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/dealNames/<string:id>', methods=['DELETE'])
def delete_dealName_data(id):
    dealNames_bl.delete_dealName(id)
    db.session.commit()
    return jsonify("deleted dealName")

# =======================================================
# =============== receivingFruits =======================


@app.route('/receivingFruits', methods=['GET'])
def get_receivingFruits():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        filteredSeason = int(request.args.get('season2filter'))
        data = receivingFruits_bl.get_receivingFruits(filteredSeason)
        return jsonify(data)


@app.route('/receivingFruits', methods=['POST'])
def add_receivingFruit():
    data = request.json

    # in case not all fields were filled
    # or data['fruitTypeID'] == 'בחר'
    if data['season'] == '' or data['growerID'] == 'בחר' or data['packingHouseID'] == 'בחר' or data['plotID'] == 'בחר'  or data['packingMaterialID'] == 'בחר':
        return jsonify("issueWithFieldData")
    new_record = receivingFruits_bl.add_receivingFruit(data)
    db.session.add(new_record)
    try:
        db.session.commit()
        return jsonify(new_record.id)  # return the id of the added item
    except:
        db.session.rollback()
        return jsonify("issueWithRecord")


@app.route('/receivingFruits/<string:id>', methods=['PUT'])
def update_receivingFruit(id):
    data = request.json
    receivingFruits_bl.update_receivingFruit(id, data)
    try:
        db.session.commit()
        return jsonify("updated receivingFruit")
    except:
        db.session.rollback()
        return jsonify("issueWithRecord")


@app.route('/receivingFruits/<string:id>', methods=['DELETE'])
def delete_receivingFruit_data(id):
    receivingFruits_bl.delete_receivingFruit(id)
    db.session.commit()
    return jsonify("deleted receivingFruits")


# =======================================================
# =============== deals =================================


@app.route('/deals', methods=['GET'])
def get_deals():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        filteredSeason = int(request.args.get('season2filter'))
        data = deals_bl.get_deals(filteredSeason)
        return jsonify(data)


@app.route('/deals', methods=['POST'])
def add_deal():
    data = request.json

    # in case not all fields were filled
    if data['filtered'] == 'בחר' or ('season' not in data):
        return jsonify("issueWithFieldData")
    new_record = deals_bl.add_deal(data)

    #  there is a price without date
    if new_record == ("missingData"):
        return jsonify("issueWithFieldData")
    db.session.add(new_record)
    try:
        db.session.commit()
        return jsonify(new_record.id)  # return the id of the added item
    except:
        db.session.rollback()
        return jsonify("issueWithRecord")


@app.route('/deals/<string:id>', methods=['PUT'])
def update_deal(id):
    data = request.json
    # if there is a case where the
    if (float(data['price1']) != 0 and int(data['year_price1']) == 0) or (float(data['price2']) != 0 and int(data['year_price2']) == 0) or (float(data['price3']) != 0 and int(data['year_price3']) == 0):
        return jsonify("issueWithFieldData")
    deals_bl.update_deal(id, data)
    try:
        db.session.commit()
        return jsonify("updated deal")
    except:
        db.session.rollback()
        return jsonify("issueWithRecord")


@app.route('/deals/<string:id>', methods=['DELETE'])
def delete_deal_data(id):
    deals_bl.delete_deal(id)
    db.session.commit()
    return jsonify("deleted deal")

# =================================================================================================
#              l o ca l   m a r k e t   t a b l e s
# =================================================================================================

# =======================================================
# =============== FixedInfo =============================


@app.route('/fixedInfo', methods=['GET'])
def get_fixedInfos():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        data = fixedInfo_bl.get_info()
        return jsonify(data)


@app.route('/fixedInfo/<string:name>', methods=['PUT'])
def update_info(name):
    data = request.json
    if (name == '' or data['name_hebrew'] == ''):
        return jsonify("issueWithFieldData")
    else:
        try:
            fixedInfo_bl.update_info(name, data)
            db.session.commit()
            return jsonify("updated info")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


# =======================================================
# =============== fruitSize =============================


@app.route('/fruitSize', methods=['GET'])
def get_fruitSize():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        data = fruitSize_bl.get_fruitSize()
        return jsonify(data)


@app.route('/fruitSize', methods=['POST'])
def add_fruitSizer():
    data = request.json
    if (data['size'] == ''):
        return jsonify("issueWithFieldData")
    else:
        new_record = fruitSize_bl.add_fruitSize(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/fruitSize/<string:id>', methods=['PUT'])
def update_fruitSize(id):
    data = request.json
    if (data['size'] == ''):
        return jsonify("issueWithFieldData")
    else:
        try:
            fruitSize_bl.update_fruitSize(id, data)
            db.session.commit()
            return jsonify("updated fruitSize")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/fruitSize/<string:id>', methods=['DELETE'])
def delete_fruitSize_data(id):
    fruitSize_bl.delete_fruitSize(id)
    db.session.commit()
    return jsonify("deleted fruitSize")

# =======================================================
# =============== Traders ===============================


@app.route('/traders', methods=['GET'])
def get_traders():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        data = traders_bl.get_traders()
        return jsonify(data)


@app.route('/traders', methods=['POST'])
def add_trader():
    data = request.json
    if (data['traderName'] == ''):
        return jsonify("issueWithFieldData")
    else:
        new_record = traders_bl.add_trader(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/traders/<string:id>', methods=['PUT'])
def update_trader(id):
    data = request.json
    if (data['traderName'] == ''):
        return jsonify("issueWithFieldData")
    else:
        try:
            traders_bl.update_trader(id, data)
            db.session.commit()
            return jsonify("updated trader")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/traders/<string:id>', methods=['DELETE'])
def delete_trader_data(id):
    traders_bl.delete_trader(id)
    db.session.commit()
    return jsonify("deleted trader")


# =======================================================
# =============== palletsMat ============================

@app.route('/palletsMat', methods=['GET'])
def get_palletsMat():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        data = palletsMat_bl.get_palletsMat()
        return jsonify(data)


@app.route('/palletsMat', methods=['POST'])
def add_palletMat():
    data = request.json
    if (data['palletType'] == ''):
        return jsonify("issueWithFieldData")
    else:
        new_record = palletsMat_bl.add_palletMat(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/palletsMat/<string:id>', methods=['PUT'])
def update_palletMat(id):
    data = request.json
    if (data['palletType'] == ''):
        return jsonify("issueWithFieldData")
    else:
        try:
            palletsMat_bl.update_palletMat(id, data)
            db.session.commit()
            return jsonify("updated palletsMat")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/palletsMat/<string:id>', methods=['DELETE'])
def delete_palletMat_data(id):
    palletsMat_bl.delete_palletMat(id)
    db.session.commit()
    return jsonify("deleted palletsMat")


# =======================================================
# =============== palletsMatCost ========================

@app.route('/palletsMatCost', methods=['GET'])
def get_palletsMatCost():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        palletsMatID = int(request.args.get('palletsMatID2filter'))
        data = palletsMatCost_bl.get_palletsMatCost(palletsMatID)
        return jsonify(data)


@app.route('/palletsMatCost', methods=['POST'])
def add_palletMatCost():
    data = request.json
    # if (data['palletType']  == ''):
    #      return jsonify("issueWithFieldData")
    # else:
    new_record = palletsMatCost_bl.add_palletMatCost(data)
    db.session.add(new_record)
    try:
        db.session.commit()
        return jsonify(new_record.id)  # return the id of the added item
    except:
        db.session.rollback()
        return jsonify("issueWithRecord")


@app.route('/palletsMatCost/<string:id>', methods=['PUT'])
def update_palletMatCost(id):
    data = request.json
    # if (data['palletType']  == ''):
    #      return jsonify("issueWithFieldData")
    # else:
    try:
        palletsMatCost_bl.update_palletMatCost(id, data)
        db.session.commit()
        return jsonify("updated palletsMat")
    except:
        db.session.rollback()
        return jsonify("issueWithRecord")


@app.route('/palletsMatCost/<string:id>', methods=['DELETE'])
def delete_palletMatCost_data(id):
    palletsMatCost_bl.delete_palletMatCost(id)
    db.session.commit()
    return jsonify("deleted palletsMat")

# =======================================================
# =============== market_packing_mat ====================


@app.route('/marketPackingMat', methods=['GET'])
def get_market_packing_mat():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        data = market_packing_mat_bl.get_market_packing_mat()
        return jsonify(data)


@app.route('/marketPackingMat', methods=['POST'])
def add_market_packing_mat():
    data = request.json
    if (data['marketPackingType'] == ''):
        return jsonify("issueWithFieldData")
    else:
        new_record = market_packing_mat_bl.add_market_packing_mat(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/marketPackingMat/<string:id>', methods=['PUT'])
def update_market_packing_mat(id):
    data = request.json
    if (data['marketPackingType'] == ''):
        return jsonify("issueWithFieldData")
    else:
        try:
            market_packing_mat_bl.update_market_packing_mat(id, data)
            db.session.commit()
            return jsonify("updated market packing mat")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/marketPackingMat/<string:id>', methods=['DELETE'])
def delete_market_packing_mat(id):
    market_packing_mat_bl.delete_market_packing_mat(id)
    db.session.commit()
    return jsonify("deleted market packing mat")


# =======================================================
# =============== market_fruits =========================

@app.route('/marketFruits', methods=['GET'])
def get_marketFruits():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        data = market_fruits_bl.get_marketFruits()
        return jsonify(data)


@app.route('/marketFruits', methods=['POST'])
def add_marketFruit():
    data = request.json
    if (data['fruitName'] == '' or data['size'] == '' or data['quality'] == ''):
        return jsonify("issueWithFieldData")
    else:
        new_record = market_fruits_bl.add_marketFruit(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/marketFruits/<string:id>', methods=['PUT'])
def update_marketFruit(id):
    data = request.json
    if (data['fruitName'] == '' or data['size'] == '' or data['quality'] == ''):
        return jsonify("issueWithFieldData")
    else:
        try:
            market_fruits_bl.update_marketFruit(id, data)
            db.session.commit()
            return jsonify("updated marketFruit")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/marketFruits/<string:id>', methods=['DELETE'])
def delete_marketFruit(id):
    market_fruits_bl.delete_marketFruit(id)
    db.session.commit()
    return jsonify("deleted marketFruit")


# =======================================================
# =============== PalletCreation_header =================

@app.route('/palletCreation_header', methods=['GET'])
def get_palletCreation_header():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        filteredSeason = int(request.args.get('season2filter'))
        data = palletCreation_header_bl.get_fpchs(filteredSeason)
        return jsonify(data)


@app.route('/palletCreation_header/<string:season>', methods=['GET'])
def get_distinctPalletsWithLines(season):
    data = palletCreation_header_bl.get_PalletsNumWithLines(season)
    return jsonify(data)


@app.route('/palletCreation_header', methods=['POST'])
def add_palletCreation_header():
    data = request.json
    if (data['palletMatID'] == 'בחר' or data['palletNum'] == 'בחר'):
        return jsonify("issueWithFieldData")
    else:
        new_record = palletCreation_header_bl.add_fpch(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/palletCreation_header/<string:id>', methods=['PUT'])
def update_palletCreation_header(id):
    data = request.json
    if (data['palletMatID'] == '' or data['palletNum'] == ''):
        return jsonify("issueWithFieldData")
    else:
        try:
            palletCreation_header_bl.update_fpch(id, data)
            db.session.commit()
            return jsonify("updated market packing mat")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/palletCreation_header/<string:id>', methods=['DELETE'])
def delete_palletCreation_header(id):
    palletCreation_header_bl.delete_fpch(id)
    db.session.commit()
    return jsonify("deleted palletCreation header")


# =======================================================
# =============== PalletCreation_lines ==================

@app.route('/palletCreation_lines', methods=['GET'])
def get_palletCreation_lines():
    if (request.args.get('palletID2filter') == None):
        palletId = 0
    else:
        palletId = int(request.args.get('palletID2filter'))
    data = palletCreation_lines_bl.get_fpcls(palletId)
    return jsonify(data)


@app.route('/palletCreation_lines', methods=['POST'])
def add_palletCreation_line():
    data = request.json
    if (data['matketFruitID'] == 'בחר' or data['marketPackingMatTypeID'] == 'בחר' or data['deliveryNoteNum'] != '-'):
        return jsonify("issueWithFieldData")
    else:
        new_record = palletCreation_lines_bl.add_fpcl(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/palletCreation_lines/<string:id>', methods=['PUT'])
def update_palletCreation_line(id):
    data = request.json
    if (data['matketFruitID'] == '' or data['marketPackingMatTypeID'] == ''):
        return jsonify("issueWithFieldData")
    else:
        try:
            palletCreation_lines_bl.update_fpcl(id, data)
            db.session.commit()
            return jsonify("updated palletCreation line")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/palletCreation_lines/<string:id>', methods=['DELETE'])
def delete_palletCreation_line(id):
    palletCreation_lines_bl.delete_fpcl(id)
    db.session.commit()
    return jsonify("deleted palletCreation line")


@app.route('/palletCreation_lines', methods=['DELETE'])
def delete_palletCreation_AllLines():
    palletId = int(request.args.get('palletID2filter'))
    palletCreation_lines_bl.delete_Allfpcl(palletId)
    db.session.commit()
    return jsonify("deleted all lines in palletCreation headerID")


# =======================================================
# =============== deliveryNote_header_bl ================

@app.route('/deliveryNote_header', methods=['GET'])
def get_deliveryNote_header():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        filteredSeason = int(request.args.get('season2filter'))
        data = deliveryNote_header_bl.get_dnhs(filteredSeason)
        return jsonify(data)


@app.route('/deliveryNote_header/<string:season>', methods=['GET'])
def get_distinctdeliveryNoteWithLines(season):
    data = deliveryNote_header_bl.get_distinctdeliveryNoteWithLines(season)
    return jsonify(data)


@app.route('/deliveryNote_header', methods=['POST'])
def add_deliveryNote_header():
    data = request.json
    if (data['deliveryNoteNum'] == '-' or data['traderID'] == 'בחר'):
        return jsonify("issueWithFieldData")
    else:
        new_record = deliveryNote_header_bl.add_dnh(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/deliveryNote_header/<string:id>', methods=['PUT'])
def update_deliveryNote_header(id):
    data = request.json
    if (data['deliveryNoteNum'] == '-' or data['deliveryNoteNum'] == 0 or data['traderID'] == ''):
        return jsonify("issueWithFieldData")
    else:
        try:
            deliveryNote_header_bl.update_dnh(id, data)
            db.session.commit()
            return jsonify("updated deliveryNote header")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/deliveryNote_header/<string:id>', methods=['DELETE'])
def delete_deliveryNote_header(id):
    deliveryNote_header_bl.delete_dnh(id)
    db.session.commit()
    return jsonify("deleted deliveryNote header")


# =======================================================
# =============== deliveryNote_lines ====================


@app.route('/deliveryNote_lines', methods=['GET'])
def get_deliveryNote_lines():
    if (request.args.get('deliveryNoteHeaderID2filter') == None):
        deliveryNoteHeaderID = 0
    else:
        deliveryNoteHeaderID = int(
            request.args.get('deliveryNoteHeaderID2filter'))
    data = deliveryNote_lines_bl.get_dnls(deliveryNoteHeaderID)
    return jsonify(data)


@app.route('/deliveryNote_lines', methods=['POST'])
def add_deliveryNote_line():
    data = request.json
    if (data['palletNum'] == 'בחר' or data.get("fruitPalletCreation_headerID") == 'בחר'):
        return jsonify("issueWithFieldData")
    else:
        new_record = deliveryNote_lines_bl.add_dnl(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/deliveryNote_lines/<string:id>', methods=['PUT'])
def update_deliveryNote_line(id):
    data = request.json
    if (data['deliveryNote_headerID'] == '' or data['fruitPalletCreation_headerID'] == '' or data['palletNum'] == 'בחר'):
        return jsonify("issueWithFieldData")
    else:
        try:
            deliveryNote_lines_bl.update_dnl(id, data)
            db.session.commit()
            return jsonify("updated deliveryNote line")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/deliveryNote_lines/<string:id>', methods=['DELETE'])
def delete_deliveryNote_line(id):
    deliveryNote_lines_bl.delete_dnl(id)
    db.session.commit()
    return jsonify("deleted deliveryNote line")


@app.route('/deliveryNote_lines', methods=['DELETE'])
def delete_deliveryNote_AllLines():
    deliveryNoteHeaderID = int(request.args.get('deliveryNoteHeaderID2filter'))
    deliveryNote_lines_bl.delete_Alldnl(deliveryNoteHeaderID)
    db.session.commit()
    return jsonify("deleted all lines in deliveryNote headerID")


# =======================================================
# =============== manufacturer_invoice ==================

@app.route('/manufacturer_invoice', methods=['GET'])
def get_manufacturer_invoices():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        filteredSeason = int(request.args.get('season2filter'))
        data = manufacturer_invoice_bl.get_all_manufacturer_invoices(
            filteredSeason)
        return jsonify(data)


@app.route('/manufacturer_invoice', methods=['POST'])
def add_manufacturer_invoice():
    data = request.json
    if (data['ManufacturerInvNum'] == ''):
        return jsonify("issueWithFieldData")
    else:
        new_record = manufacturer_invoice_bl.add_manufacturer_invoice(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/manufacturer_invoice/<string:id>', methods=['PUT'])
def update_manufacturer_invoice(id):
    data = request.json
    if (data['ManufacturerInvNum'] == ''):
        return jsonify("issueWithFieldData")
    else:
        try:
            manufacturer_invoice_bl.update_manufacturer_invoice(id, data)
            db.session.commit()
            return jsonify("updated manufacturer_invoice")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/manufacturer_invoice/<string:id>', methods=['DELETE'])
def delete_manufacturer_invoice(id):
    manufacturer_invoice_bl.delete_manufacturer_invoice(id)
    db.session.commit()
    return jsonify("deleted manufacturer_invoice")


# =======================================================
# =============== closingData ===========================

@app.route('/closingData', methods=['GET'])
def get_closingData():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        filteredSeason = int(request.args.get('season2filter'))
        data = closingData_bl.get_all_closingData(filteredSeason)
        return jsonify(data)


@app.route('/closingData', methods=['POST'])
def add_closingData():
    data = request.json
    new_record = closingData_bl.add_closingData(data)
    db.session.add(new_record)
    try:
        db.session.commit()
        return jsonify(new_record.id)  # return the id of the added item
    except:
        db.session.rollback()
        return jsonify("issueWithRecord")


@app.route('/closingData/<string:id>', methods=['PUT'])
def update_closingData(id):
    data = request.json
    if id != 'null':  # which means that we need to update
        try:
            closingData_bl.update_closingData(id, data)
            db.session.commit()
            return jsonify("updated closingData")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")

    else:  # which means that we need to add
        new_record = closingData_bl.add_closingData(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/closingData/<string:id>', methods=['DELETE'])
def delete_closingData(id):
    closingData_bl.delete_closingData(id)
    db.session.commit()
    return jsonify("deleted closingData")

# =======================================================
# =============== invoice_header ========================


@app.route('/invoice_header', methods=['GET'])
def get_invoice_headers():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        filteredSeason = int(request.args.get('season2filter'))
        data = invoice_header_bl.get_invoice_headers(filteredSeason)
        return jsonify(data)


@app.route('/invoice_header', methods=['POST'])
def add_invoice_header():
    data = request.json
    if (data['invoiceNum'] == '-' or data['traderID'] == 'בחר'):
        return jsonify("issueWithFieldData")
    else:
        new_record = invoice_header_bl.add_invoice_header(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/invoice_header/<string:id>', methods=['PUT'])
def update_invoice_header(id):
    data = request.json
    if (data['invoiceNum'] == '-' or data['invoiceNum'] == 0 or data['traderID'] == ''):
        return jsonify("issueWithFieldData")
    else:
        try:
            invoice_header_bl.update_invoice_header(id, data)
            db.session.commit()
            return jsonify("updated invoice header")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/invoice_header/<string:id>', methods=['DELETE'])
def delete_invoice_header(id):
    invoice_header_bl.delete_invoice_header(id)
    db.session.commit()
    return jsonify("deleted invoice header")


@app.route('/invoice_header', methods=['PUT'])
def update_invoiceStatus():
    data = request.json
    receiptHeaderData = data['params']['receiptHeaderData2filter']
    invoiceID = receiptHeaderData['invoiceHeaderID']
    invoiceStatus = receiptHeaderData['invoiceStatus']
    try:
        invoice_header_bl.update_invoiceStatus(invoiceID, invoiceStatus)
        db.session.commit()
        return jsonify("updated invoice status")
    except:
        db.session.rollback()
        return jsonify("issueWithRecord")

# =======================================================
# =============== invoice_lines =========================


@app.route('/invoice_lines', methods=['GET'])
def get_invoice_lines():
    if (request.args.get('invoiceHeaderID2filter') == None):
        invoiceHeaderID = 0
    else:
        invoiceHeaderID = int(request.args.get('invoiceHeaderID2filter'))
    data = invoice_lines_bl.get_invoice_lines(invoiceHeaderID)
    return jsonify(data)


@app.route('/invoice_lines', methods=['POST'])
def add_invoice_line():
    data = request.json
    if (data['deliveryNoteNum'] == '-' or data['deliveryNoteNum'] == 'בחר'):
        return jsonify("issueWithFieldData")
    else:
        new_record = invoice_lines_bl.add_invoice_line(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/invoice_lines/<string:id>', methods=['PUT'])
def update_invoice_line(id):
    data = request.json
    if (data['deliveryNote_headerID'] == '' or data['deliveryNote_headerID'] == '' or data['deliveryNoteNum'] == 'בחר' or data['deliveryNoteNum'] == '-'):
        return jsonify("issueWithFieldData")
    else:
        try:
            invoice_lines_bl.update_invoice_line(id, data)
            db.session.commit()
            return jsonify("updated invoice line")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/invoice_lines/<string:id>', methods=['DELETE'])
def delete_invoice_line(id):
    invoice_lines_bl.delete_invoice_line(id)
    db.session.commit()
    return jsonify("deleted invoice line")


@app.route('/invoice_lines', methods=['DELETE'])
def delete_AllInvoice_lines():
    invoiceHeaderID = int(request.args.get('invoiceHeaderID2filter'))
    invoice_lines_bl.delete_AllInvoice_lines(invoiceHeaderID)
    db.session.commit()
    return jsonify("deleted all lines in invoice headerID")


# =======================================================
# =============== receipt_header ========================

@app.route('/receipt_header', methods=['GET'])
def get_receipt_headers():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        filteredSeason = int(request.args.get('season2filter'))
        data = receipt_header_bl.get_receipt_headers(filteredSeason)
        return jsonify(data)


@app.route('/receipt_header', methods=['POST'])
def add_receipt_header():
    data = request.json
    invoiceID = data['invoiceHeaderID']
    invoiceStatus = data['invoiceStatus']
    if (data['receiptNum'] == '' or data['invoiceHeaderID'] == 'בחר'):
        return jsonify("issueWithFieldData")
    else:
        new_record = receipt_header_bl.add_receipt_header(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            try:
                invoice_header_bl.update_invoiceStatus(
                    invoiceID, invoiceStatus)
                db.session.commit()
                # return the id of the added item
                return jsonify(new_record.id)
            except:
                db.session.rollback()
                return jsonify("issueWithRecord")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/receipt_header/<string:id>', methods=['PUT'])
def update_receipt_header(id):
    data = request.json
    if (data['receiptNum'] == '' or data['receiptNum'] == 0 or data['invoiceHeaderID'] == ''):
        return jsonify("issueWithFieldData")
    else:
        try:
            receipt_header_bl.update_receipt_header(id, data)
            db.session.commit()
            return jsonify("updated receipt header")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/receipt_header/<string:id>', methods=['DELETE'])
def delete_receipt_header(id):
    deletedrecrod = receipt_header_bl.delete_receipt_header(id)
    invoiceID = deletedrecrod.invoiceHeaderID
    invoiceStatus = 'סגורה'
    db.session.commit()
    try:
        invoice_header_bl.update_invoiceStatus(invoiceID, invoiceStatus)
        db.session.commit()
        return jsonify("deleted receipt header")
    except:
        db.session.rollback()
        return jsonify("issueWithRecord")


# =======================================================
# =============== receipt_lines =========================

@app.route('/receipt_lines', methods=['GET'])
def get_receipt_lines():
    if (request.args.get('receiptHeaderID2filter') == None):
        receiptHeaderID = 0
    else:
        receiptHeaderID = int(request.args.get('receiptHeaderID2filter'))
    data = receipt_lines_bl.get_receipt_lines(receiptHeaderID)
    return jsonify(data)


@app.route('/receipt_lines', methods=['POST'])
def add_receipt_line():
    data = request.json
    if (data['paymentType'] == 'בחר'
            or (data['paymentType'] == 'צק' and (data['checkNum'] == '' or data['bankName'] == ''))
        ):
        return jsonify("issueWithFieldData")
    else:
        new_record = receipt_lines_bl.add_receipt_line(data)
        db.session.add(new_record)
        try:
            db.session.commit()
            return jsonify(new_record.id)  # return the id of the added item
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/receipt_lines/<string:id>', methods=['PUT'])
def update_receipt_line(id):
    data = request.json
    if (data['paymentType'] == 'בחר' or (data['paymentType'] == 'צק' and (data['checkNum'] == '' or data['bankName'] == ''))):
        return jsonify("issueWithFieldData")
    else:
        try:
            receipt_lines_bl.update_receipt_line(id, data)
            db.session.commit()
            return jsonify("updated receipt line")
        except:
            db.session.rollback()
            return jsonify("issueWithRecord")


@app.route('/receipt_lines/<string:id>', methods=['DELETE'])
def delete_receipt_line(id):
    receipt_lines_bl.delete_receipt_line(id)
    db.session.commit()
    return jsonify("deleted receipt line")


@app.route('/receipt_lines', methods=['DELETE'])
def delete_AllReceipt_lines():
    receiptHeaderID = int(request.args.get('receiptHeaderID2filter'))
    receipt_lines_bl.delete_AllReceipt_lines(receiptHeaderID)
    db.session.commit()
    return jsonify("deleted all lines in receipt headerID")


# =================================================================================================
#               R e c e i v i n g     F r u i t     R e p o r t s
# =================================================================================================

# =======================================================
# =============== monthly report ========================


@app.route('/receive_reports/monthlyReport', methods=['GET'])
def monthly_report_data():
    reportFilter = request.args.get('reportFilter')
    season2filter = int(request.args.get('season2filter'))
    grower2filter = int(request.args.get('grower2filter'))
    month2filter = int(request.args.get('month2filter'))
    if (reportFilter == 'זן'):
        monthlyData = monthlyReport_bl.get_monthly_per_FruitType(
            season2filter, grower2filter, month2filter)
    if (reportFilter == 'מגדל-זן-עסקה'):
        monthlyData = monthlyReport_bl.get_monthly_per_Deal(
            season2filter, grower2filter, month2filter)
    return jsonify(monthlyData)


# =======================================================
# =============== daily report ==========================


@app.route('/receive_reports/dailyReport', methods=['GET'])
def daily_report_data():
    dateFilter = request.args.get('date2filter')
    dateFilter_dict = json.loads(dateFilter)
    grower2filter = int(request.args.get('grower2filter'))

    dailyData = dailyReport_bl.get_daily_per_FruitName(
        dateFilter_dict, grower2filter)

    return jsonify(dailyData)


# =======================================================
# =============== season report =========================


@app.route('/receive_reports/seasonReport', methods=['GET'])
def season_report_data():
    season2filter = int(request.args.get('season2filter'))
    grower2filter = int(request.args.get('grower2filter'))

    seasonData = seasonReport_bl.get_season_per_FruitName(
        season2filter, grower2filter)

    return jsonify(seasonData)


# =======================================================
# =============== summary report ========================

@app.route('/receive_reports/summaryReport', methods=['GET'])
def summary_report_data():
    resp = auth_bl.token_verification()
    if resp == "not authorized":
        return jsonify("The user is not autorized")
    else:
        reportFilter = request.args.get('reportFilter')
        season2filter = int(request.args.get('season2filter'))
        month2filter = int(request.args.get('month2filter'))

        if (reportFilter == 'מרכז חודשי'):
            summaryData = summaryReport_bl.get_summary_monthly(
                season2filter, month2filter)
        elif (reportFilter == 'מרכז אריזות חודשי'):
            summaryData = summaryReport_bl.get_summary_monthly_packingMat(
                season2filter, month2filter)
        elif (reportFilter == 'מרכז עונתי'):
            summaryData = summaryReport_bl.get_summary_season(season2filter)
        elif (reportFilter == 'מרכז עונתי מגדל'):
            summaryData = summaryReport_bl.get_summary_season_growers(
                season2filter)
        elif (reportFilter == 'מרכז עונתי בית אריזה'):
            summaryData = summaryReport_bl.get_summary_packingHouse(
                season2filter)

        return jsonify(summaryData)


# =======================================================
# =============== plot report ===========================

@app.route('/receive_reports/plotReport', methods=['GET'])
def plot_per_dates():
    reportFilter = request.args.get('reportFilter')
    plotName2Filter = int(request.args.get('plotName2Filter'))

    fromDateFilter = request.args.get('fromDate2Filter')
    fromDateFilter_dict = json.loads(fromDateFilter)

    toDateFilter = request.args.get('toDate2Filter')
    toDateFilter_dict = json.loads(toDateFilter)

    if (reportFilter == 'צובר חלקה'):
        plotData = plot_report_BL.get_plot_per_dates(
            plotName2Filter,  fromDateFilter_dict,  toDateFilter_dict)
    elif (reportFilter == 'צובר חלקות'):
        plotData = plot_report_BL.get_plots_per_dates(
            fromDateFilter_dict,  toDateFilter_dict)

    return jsonify(plotData)


# =================================================================================================
#             L O C A L    M A R K E T    R e p o r t s
# =================================================================================================


# =======================================================
# =============== deliveryNote report ===================


@app.route('/local_reports/deliveryNote', methods=['GET'])
def deliveryNote_report_data():
    reportFilter = request.args.get('reportType2Filter')
    deliveryNoteNum2filter = request.args.get('deliveryNum2Filetr')
    season2filter = int(request.args.get('season2Filter'))

    if (reportFilter == 'all'):
        deliveryNoteData = deliveryNote_report_bl.get_deliveryNote(
            reportFilter, deliveryNoteNum2filter, season2filter)
    if (reportFilter == '2prct'):
        deliveryNoteData = deliveryNote_report_bl.get_deliveryNote2prct(
            reportFilter, deliveryNoteNum2filter, season2filter)

    return jsonify(deliveryNoteData)


# =======================================================
# =============== invoice report ========================

@app.route('/local_reports/invoice', methods=['GET'])
def invoice_report_data():
    invoiceHeaderID = int(request.args.get('invoiceHeaderID2Filter'))
    invoiceLines = invoice_report_bl.get_invoiceLines(invoiceHeaderID)
    palletCost = invoice_report_bl.get_palletCost(invoiceHeaderID)
    resellerInfo = invoice_report_bl.get_resellerInfo(invoiceHeaderID)

    
    dict = {'invoiceLines': invoiceLines,
            'palletCost': palletCost, 'resellerInfo': resellerInfo}

    return jsonify(dict)


# =======================================================
# =============== palletsWOinvoices report ==============

@app.route('/local_reports/palletsWOinvoices', methods=['GET'])
def palletsWOinvoices_report_data():
    traderID = int(request.args.get('traderID2Filter'))

    fromDateFilter = request.args.get('fromData2Filter')
    fromDateFilter_dict = json.loads(fromDateFilter)

    toDateFilter = request.args.get('toData2Filter')
    toDateFilter_dict = json.loads(toDateFilter)

    palletsWOinvoices = pallets_wo_invoices_bl.get_palletsWOinvoices(
        fromDateFilter_dict, toDateFilter_dict, traderID)
    return jsonify(palletsWOinvoices)


# =======================================================
# =======================================================
if __name__ == '__main__':
    app.run(port=1000)
