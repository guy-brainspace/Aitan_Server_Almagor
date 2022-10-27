
from confdb import db


# -------------------------------------------------------
#               Users Table
# -------------------------------------------------------

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=True, nullable=False)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())

# -------------------------------------------------------
#               Receiving Fruits Tables
# -------------------------------------------------------


class Growers(db.Model):
    __tablename__ = "growers"
    id = db.Column(db.Integer, primary_key=True)
    growerName = db.Column(db.String(30), unique=True, nullable=False)
    isActive = db.Column(db.Integer, server_default='1', nullable=False)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    receivingFruitID = db.relationship('Receiving_fruits', backref='growers')


# -------------------------------------------------------

class DealNames(db.Model):
    __tablename__ = "dealNames"
    id = db.Column(db.Integer, primary_key=True)
    dealName = db.Column(db.String(50), unique=True, nullable=False)
    isActive = db.Column(db.Integer, server_default='1', nullable=False)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    receivingFruitID = db.relationship('Receiving_fruits', backref='dealNames')
    dealNamesID = db.relationship('Deals', backref='dealNames')


# -------------------------------------------------------

class Plots(db.Model):
    __tablename__ = "plots"
    id = db.Column(db.Integer, primary_key=True)
    plotName = db.Column(db.String(30), unique=True, nullable=False)
    isActive = db.Column(db.Integer,  server_default='1',  nullable=False)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    receivingFruitID = db.relationship('Receiving_fruits', backref='plots')


# -------------------------------------------------------

class Packing_mat(db.Model):
    __tablename__ = "packing_mat"

    id = db.Column(db.Integer, primary_key=True)
    packingType = db.Column(db.String(30), unique=True, nullable=False)
    weight = db.Column(db.Numeric(precision=10, scale=2,
                       asdecimal=False, decimal_return_scale=None), nullable=False)
    isActive = db.Column(db.Integer,  server_default='1', nullable=False)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    receivingFruitID = db.relationship(
        'Receiving_fruits', backref='packing_mat')

# -------------------------------------------------------


class PackingHouse(db.Model):
    __tablename__ = "packinghouse"
    __table_args__ = (
        db.UniqueConstraint('packingHouseName', 'location'),
    )
    id = db.Column(db.Integer, primary_key=True)
    packingHouseName = db.Column(db.String(30),  nullable=False)
    location = db.Column(db.String(50),  nullable=False)
    isActive = db.Column(db.Integer,  server_default='1', nullable=False)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    receivingFruitID = db.relationship(
        'Receiving_fruits', backref='packinghouse')


# -------------------------------------------------------

class Deals(db.Model):
    __tablename__ = "deals"
    __table_args__ = (
        db.UniqueConstraint('fromDate', 'season', 'dealNameID', 'fruitTypeID'),
    )

    id = db.Column(db.Integer, primary_key=True)
    fromDate = db.Column(db.Date, nullable=False)
    toDate = db.Column(db.Date)
    season = db.Column(db.Integer, nullable=False)
    dealNameID = db.Column(db.Integer, db.ForeignKey(
        'dealNames.id'), nullable=False)
    fruitTypeID = db.Column(
        db.Integer, db.ForeignKey('fruits.id'), nullable=False)
    price1 = db.Column(db.Numeric(precision=10, scale=2, asdecimal=False,
                       decimal_return_scale=None), server_default='0')
    price1Date = db.Column(db.Date)
    price2 = db.Column(db.Numeric(precision=10, scale=2, asdecimal=False,
                       decimal_return_scale=None), server_default='0')
    price2Date = db.Column(db.Date)
    price3 = db.Column(db.Numeric(precision=10, scale=2, asdecimal=False,
                       decimal_return_scale=None), server_default='0')
    price3Date = db.Column(db.Date)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())


# -------------------------------------------------------

class Receiving_fruits(db.Model):
    __tablename__ = "receiving_fruits"

    id = db.Column(db.Integer, primary_key=True)
    receivingDate = db.Column(db.Date, nullable=False)
    season = db.Column(db.Integer, nullable=False)
    growerID = db.Column(db.Integer, db.ForeignKey(
        'growers.id'), nullable=False)
    deliverNote = db.Column(db.String(80), nullable=False)
    packingHouseID = db.Column(db.Integer, db.ForeignKey(
        'packinghouse.id'), nullable=False)
    plotID = db.Column(db.Integer, db.ForeignKey('plots.id'), nullable=False)
    fruitTypeID = db.Column(
        db.Integer, db.ForeignKey('fruits.id'), nullable=False)
    dealNameID = db.Column(db.Integer, db.ForeignKey(
        'dealNames.id'), nullable=False)
    packingMaterialID = db.Column(
        db.Integer, db.ForeignKey('packing_mat.id'), nullable=False)
    qtyInPacking = db.Column(db.Integer)
    weightBruto = db.Column(db.Numeric(
        precision=10, scale=2, asdecimal=False, decimal_return_scale=None))
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())


# -------------------------------------------------------

class Fruits(db.Model):
    __tablename__ = "fruits"
    __table_args__ = (
        db.UniqueConstraint('fruitName', 'fruitType'),
    )

    id = db.Column(db.Integer, primary_key=True)
    fruitName = db.Column(db.String(30),  nullable=False)
    fruitType = db.Column(db.String(30),  nullable=False)
    isActive = db.Column(db.Integer,  server_default='1', nullable=False)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    receivingFruitID = db.relationship('Receiving_fruits', backref='fruits')
    dealNamesID = db.relationship('Deals', backref='fruits')
    marketFruitName = db.relationship('Market_fruits', backref='fruits')

# -------------------------------------------------------
#               Local Market Tables
# -------------------------------------------------------


class FruitSize(db.Model):
    __tablename__ = "fruitsize"
    id = db.Column(db.Integer,  primary_key=True)
    size = db.Column(db.String(30), unique=True, nullable=False)
    isActive = db.Column(db.Integer,  server_default='1', nullable=False)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    size_rlsp = db.relationship('Market_fruits', backref='fruitsize')


class Market_fruits(db.Model):
    __tablename__ = "market_fruits"
    __table_args__ = (
        db.UniqueConstraint('fruitID', 'sizeID', 'quality'),
    )

    id = db.Column(db.Integer, primary_key=True)
    fruitID = db.Column(db.Integer, db.ForeignKey('fruits.id'), nullable=False)
    sizeID = db.Column(db.Integer, db.ForeignKey(
        'fruitsize.id'), nullable=False)
    quality = db.Column(db.String(10), nullable=False)
    isActive = db.Column(db.Integer,  server_default='1', nullable=False)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    market_fruits_rels = db.relationship(
        'FruitPalletCreation_lines', backref='market_fruits')


class PalletsMat(db.Model):
    __tablename__ = "palletsmat"

    id = db.Column(db.Integer, primary_key=True)
    palletType = db.Column(db.String(30), unique=True, nullable=False)
    palletWeight = db.Column(db.Numeric(
        precision=10, scale=2, asdecimal=False, decimal_return_scale=None))
    isActive = db.Column(db.Integer,  server_default='1', nullable=False)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    market_pallets_rels = db.relationship(
        'FruitPalletCreation_header', backref='palletsmat')
    palletsMatCost_rels = db.relationship(
        'PalletsMatCost', backref='palletsmat')


class PalletsMatCost(db.Model):
    __tablename__ = "palletsmatcost"
    __table_args__ = (
        db.UniqueConstraint('palletMatID', 'fromDate'),
    )

    id = db.Column(db.Integer, primary_key=True)
    palletMatID = db.Column(db.Integer, db.ForeignKey(
        'palletsmat.id'), nullable=False)
    fromDate = db.Column(db.Date, nullable=False)
    toDate = db.Column(db.Date, nullable=False)
    palletMatCost = db.Column(db.Numeric(
        precision=10, scale=2, asdecimal=False, decimal_return_scale=None))
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())


class Market_packing_mat(db.Model):
    __tablename__ = "market_packing_mat"

    id = db.Column(db.Integer, primary_key=True)
    marketPackingType = db.Column(db.String(30), unique=True, nullable=False)
    isActive = db.Column(db.Integer,  server_default='1', nullable=False)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    Market_packing_mat_rels = db.relationship(
        'FruitPalletCreation_lines', backref='Market_packing_mat')


# class FruitPalletCreation_header(db.Model):
#     __tablename__ = "fruitPalletCreation_header"
#     __table_args__ = (
#         db.UniqueConstraint('season', 'palletNum'),
#     )
#     id = db.Column(db.Integer,  primary_key=True)
#     season = db.Column(db.Integer,  nullable=False)
#     palletNum = db.Column(db.Integer,  nullable=False)
#     palletMatID = db.Column(db.Integer, db.ForeignKey('palletsmat.id'), nullable=False)
#     packingDate =  db.Column(db.Date, nullable=False)
#     palletRemarks=db.Column(db.String(120), nullable=True)
#     # delivertNoteID=db.Column(db.Integer,  nullable=True)
#     created_date = db.Column(db.DateTime, server_default=db.func.current_timestamp())
#     fruitPalletCreation_header_rels = db.relationship('FruitPalletCreation_lines', backref='fruitPalletCreation_header')


# class FruitPalletCreation_lines(db.Model):
#     __tablename__ = "fruitPalletCreation_lines"

#     id = db.Column(db.Integer,  primary_key=True)
#     fruitPalletCreation_headerID = db.Column(db.Integer, db.ForeignKey('fruitPalletCreation_header.id'), nullable=False)
#     matketFruitID = db.Column(db.Integer, db.ForeignKey('market_fruits.id'), nullable=False)
#     marketPackingMatTypeID = db.Column(db.Integer, db.ForeignKey('market_packing_mat.id'), nullable=False)
#     packMatQty = db.Column(db.Integer , server_default='0')
#     weightNeto = db.Column(db.Numeric(precision=10, scale=2, asdecimal=False, decimal_return_scale=None) , server_default='0')
#     created_date = db.Column(db.DateTime, server_default=db.func.current_timestamp())


class Fixedinfo(db.Model):
    __tablename__ = "fixedinfo"

    name = db.Column(db.String(30),  primary_key=True)
    name_hebrew = db.Column(db.String(30),  nullable=False)
    value = db.Column(db.Numeric(precision=10, scale=2, asdecimal=False,
                      decimal_return_scale=None), server_default='0')


class Traders(db.Model):
    __tablename__ = "traders"
    id = db.Column(db.Integer, primary_key=True)
    traderName = db.Column(db.String(30), unique=True, nullable=False)
    area = db.Column(db.String(30), nullable=False)
    isActive = db.Column(db.Integer,  server_default='1', nullable=False)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    tradersDeliveryNote_rels = db.relationship(
        'DeliveryNote_header', backref='traders')
    manufacturer_Invoice_rels = db.relationship(
        'Invoice_header', backref='traders')


class FruitPalletCreation_header(db.Model):
    __tablename__ = "fruitPalletCreation_header"
    __table_args__ = (
        db.UniqueConstraint('season', 'palletNum'),
    )
    id = db.Column(db.Integer,  primary_key=True)
    season = db.Column(db.Integer,  nullable=False)
    palletNum = db.Column(db.Integer,  nullable=False)
    palletMatID = db.Column(db.Integer, db.ForeignKey(
        'palletsmat.id'), nullable=False)
    packingDate = db.Column(db.Date, nullable=False)
    palletRemarks = db.Column(db.String(120), nullable=True)
    # delivertNoteID=db.Column(db.Integer,  nullable=True)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    fruitPalletCreation_header_rels = db.relationship(
        'FruitPalletCreation_lines', backref='fruitPalletCreation_header')
    fruitDeliveryNote_rels = db.relationship(
        'DeliveryNote_lines', backref='fruitPalletCreation')


class FruitPalletCreation_lines(db.Model):
    __tablename__ = "fruitPalletCreation_lines"

    id = db.Column(db.Integer,  primary_key=True)
    fruitPalletCreation_headerID = db.Column(db.Integer, db.ForeignKey(
        'fruitPalletCreation_header.id'), nullable=False)
    matketFruitID = db.Column(db.Integer, db.ForeignKey(
        'market_fruits.id'), nullable=False)
    marketPackingMatTypeID = db.Column(
        db.Integer, db.ForeignKey('market_packing_mat.id'), nullable=False)
    packMatQty = db.Column(db.Integer, server_default='0')
    weightNeto = db.Column(db.Numeric(
        precision=10, scale=2, asdecimal=False, decimal_return_scale=None), server_default='0')
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    fruitPallet_lines_rels = db.relationship(
        'ClosingData', backref='fruitPalletCreation_lines')


class DeliveryNote_header(db.Model):
    __tablename__ = "deliveryNote_header"
    __table_args__ = (
        db.UniqueConstraint('season', 'deliveryNoteNum'),
    )
    id = db.Column(db.Integer,  primary_key=True)
    season = db.Column(db.Integer,  nullable=False)
    deliveryNoteNum = db.Column(db.Integer,  nullable=False)
    deliveryDate = db.Column(db.Date, nullable=False)
    traderID = db.Column(db.Integer, db.ForeignKey(
        'traders.id'), nullable=False)
    traderPrcnt = db.Column(db.Numeric(
        precision=10, scale=2, asdecimal=False, decimal_return_scale=None), server_default='0')
    distributerPrcnt = db.Column(db.Numeric(
        precision=10, scale=2, asdecimal=False, decimal_return_scale=None), server_default='0')
    VAT = db.Column(db.Numeric(precision=10, scale=2, asdecimal=False,
                    decimal_return_scale=None), server_default='0')
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    deliveryNote_header_rels = db.relationship(
        'DeliveryNote_lines', backref='deliveryNote_header')
    invoice_header_deliveryNote_rels = db.relationship(
        'Invoice_lines', backref='deliveryNote_header')


class DeliveryNote_lines(db.Model):
    __tablename__ = "deliveryNote_lines"

    id = db.Column(db.Integer,  primary_key=True)
    deliveryNote_headerID = db.Column(db.Integer, db.ForeignKey(
        'deliveryNote_header.id'), nullable=False)
    fruitPalletCreation_headerID = db.Column(db.Integer, db.ForeignKey(
        'fruitPalletCreation_header.id'), nullable=False)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())


class Manufacturer_Invoice(db.Model):
    __tablename__ = "manufacturer_Invoice"
    __table_args__ = (
        db.UniqueConstraint('season', 'ManufacturerInvNum'),
    )

    id = db.Column(db.Integer,  primary_key=True)
    season = db.Column(db.Integer,  nullable=False)
    ManufacturerInvNum = db.Column(db.String(30), nullable=False)
    invoiceTotal = db.Column(db.Numeric(
        precision=10, scale=2, asdecimal=False, decimal_return_scale=None), server_default='0')
    invoiceDate = db.Column(db.Date, nullable=False)
    invoiceRemarks = db.Column(db.String(120), nullable=True)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    manufacturer_Invoice_rels = db.relationship(
        'Invoice_header', backref='manufacturer_Invoice')


class ClosingData(db.Model):
    __tablename__ = "closingData"

    id = db.Column(db.Integer,  primary_key=True)
    fruitPalletCreationLineID = db.Column(db.Integer, db.ForeignKey(
        'fruitPalletCreation_lines.id'), nullable=False)
    closeWeight = db.Column(db.Numeric(
        precision=10, scale=2, asdecimal=False, decimal_return_scale=None), server_default='0')
    closePrice = db.Column(db.Numeric(
        precision=10, scale=2, asdecimal=False, decimal_return_scale=None), server_default='0')
    closeDate = db.Column(db.Date, nullable=False)
    closeRemarks = db.Column(db.String(120), nullable=True)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())


class Invoice_header(db.Model):
    __tablename__ = "invoice_header"
    __table_args__ = (
        db.UniqueConstraint('season', 'invoiceNum'),
    )
    id = db.Column(db.Integer,  primary_key=True)
    season = db.Column(db.Integer,  nullable=False)
    invoiceNum = db.Column(db.Integer,  nullable=False)
    invoiceDate = db.Column(db.Date, nullable=False)
    traderID = db.Column(db.Integer, db.ForeignKey(
        'traders.id'), nullable=False)
    manufacturerInvoiceID = db.Column(db.Integer, db.ForeignKey(
        'manufacturer_Invoice.id'), nullable=True)
    invoiceStatus = db.Column(db.String(30), server_default='פתוחה')
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    invoice_header_rels = db.relationship(
        'Invoice_lines', backref='invoice_header')
    invoiceReceipt_header_rels = db.relationship(
        'Receipt_header', backref='invoice_header')


class Invoice_lines(db.Model):
    __tablename__ = "invoice_lines"

    id = db.Column(db.Integer,  primary_key=True)
    invoiceHeaderID = db.Column(db.Integer, db.ForeignKey(
        'invoice_header.id'),  unique=True, nullable=False)
    deliveryNote_headerID = db.Column(db.Integer, db.ForeignKey(
        'deliveryNote_header.id'), unique=True,  nullable=False)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())


class Receipt_header(db.Model):
    __tablename__ = "receipt_header"
    __table_args__ = (
        db.UniqueConstraint('season', 'receiptNum'),
    )
    id = db.Column(db.Integer,  primary_key=True)
    season = db.Column(db.Integer,  nullable=False)
    receiptNum = db.Column(db.Integer,  nullable=False)
    receiptDate = db.Column(db.Date, nullable=False)
    invoiceHeaderID = db.Column(db.Integer, db.ForeignKey(
        'invoice_header.id'), nullable=False)
    receiptRemarks = db.Column(db.String(30), nullable=True)
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
    receipt_header_rels = db.relationship(
        'Receipt_lines', backref='receipt_header')


class Receipt_lines(db.Model):
    __tablename__ = "receipt_lines"

    id = db.Column(db.Integer,  primary_key=True)
    receiptHeaderID = db.Column(db.Integer, db.ForeignKey(
        'receipt_header.id'),  nullable=False)
    paymentType = db.Column(db.String(30), nullable=False)
    checkNum = db.Column(db.String(30), nullable=True)
    bankName = db.Column(db.String(30), nullable=True)
    paymentDueDate = db.Column(db.Date, nullable=True)
    sumPayment = db.Column(db.Numeric(
        precision=10, scale=2, asdecimal=False, decimal_return_scale=None), server_default='0')
    created_date = db.Column(
        db.DateTime, server_default=db.func.current_timestamp())
