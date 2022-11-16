# “Aitan”Packing House's management tool
This project was developed to assist the packinghouse to be more efficient by capturing it entire activities.

# Technological tools:
 ![image](https://user-images.githubusercontent.com/58429034/198946311-32c66cd0-5eed-421a-8c4b-35bfc9e88718.png)
 
# DataBase architecture:
Receiving Fruits section:
```mermaid
    erDiagram
        dealsname ||--o{ deals : "is part of"  
        fruits ||--o{ deals : "is part of"
     
        fruits ||--o{ receiving_fruits : "is part of"      
        plots ||--o{ receiving_fruits : "is part of"
        packing_mat ||--o{ receiving_fruits : "is part of"
        packing_house ||--o{ receiving_fruits : "is part of"
        growers ||--o{ receiving_fruits : "is part of"

fruits{
        int ID PK
        string fruitName "unique"
        string fruitType
        Boolean isActive
        date created_date
     }

dealsname{
        int ID  PK
        string DealName "unique"
        Boolean isActive
        date created_date
     }

deals{
        int ID  PK
        date fromDate  "unique"
        date toDate
        int season "unique"
        int dealNameID FK "unique"
        int fruitTypeID FK "unique"
        decimal price1
        date price1Date
        decimal price2
        date price2Date
        decimal price3
        date price3Date
        date created_date
     }

plots{
        int ID PK
        string PlotName "unique"
        Boolean isActive
        date created_date
     }

packing_mat{
        int ID PK
        string packingType "unique"
        decimal weight
        Boolean isActive
        date created_date
     }


packing_house{
        int ID PK
        string packingHouseName "unique"
        Boolean isActive
        date created_date
     }

growers{
        int ID PK
        string growerName "unique"
        Boolean isActive
        date created_date
     }

receiving_fruits{
        int ID PK
        date receiveDate "unique"
        int season
        int growerID FK
        string deliverNote
        int packingHouseID FK
        int dealNameID FK
        int packingMatID FK
        int qtyInPacking 
        int weightBruto 
        date created_date
    }
```



Local Market section:
```mermaid
    erDiagram
        fruits ||--|{ market_fruits : "is part of"
        fruitsize ||--|{ market_fruits : "is part of"
        market_packing_mat ||--o{ fruitPalletCreation_lines : "is part of"
        market_fruits ||--o{ fruitPalletCreation_lines : "is part of"
        palletsMat ||--|{ palletsMatCost : has
        palletsMat ||--o{ fruitPalletCreation_header : "is part of"
        fruitPalletCreation_header ||--|| deliveryNote_lines : "is part of"
        fruitPalletCreation_header ||--o{ fruitPalletCreation_lines : has
        traders ||--o{ deliveryNote_header : "is part of"
        traders ||--o{ invoice_header : "is part of"
        manufacturer_invoice ||--o{ invoice_header : "is conncted to"
        deliveryNote_header ||--o{ deliveryNote_lines : "is part of"
        deliveryNote_header ||--o{ invoice_lines : has
        invoice_header ||--o{ receipt_header : has
        invoice_header ||--o{ invoice_lines : has
        receipt_header ||--o{ receipt_lines : has
        fruitPalletCreation_lines ||--o{ closingData : has

fruits{
    int ID  PK
    string fruitName "unique"
    string fruitType
    Boolean isActive
    date created_date
    }

fruitsize{
    int ID  PK
    string size "unique"
    Boolean isActive
    date created_date
     }


market_fruits{
    int ID  PK
    int fruitID FK "unique"
    int sizeID FK "unique"
    string quality  "unique"
    Boolean isActive
    date created_date
     }

market_packing_mat{
    int ID  PK
    string marketPackingType  "unique"
    Boolean isActive
    date created_date
}

fruitPalletCreation_lines{
    int ID  PK
    int fruitPalletCreation_headerID FK 
    int marketFruitID FK 
    int marketPackingMatID FK
    int packMatQty
    int weightNeto
    date created_date
}

closingData{
    int ID  PK
    int fruitPalletCreationLineID FK "unique"
    decimal closeWeight 
    decimal closePrice
    date closeDate
    string closeRemarks
    date created_date
}

palletsMat{
    int ID  PK
    string palletMatType
    decimal palletMatWeight
    Boolean isActive
    date created_date
}

fruitPalletCreation_header{
    int ID  PK
    int season
    int palletTypeID FK
    date packingDate
    string palletRemarks
    date created_date
}

deliveryNote_lines{
    int ID  PK
    int deliveryNote_headerID FK
    int fruitPalletCreation_headerID
}

traders{
    int ID  PK
    string traderName "unique"
    string area
     Boolean isActive
}

deliveryNote_header{
    int ID  PK
    int season   "unique"
    int deliveryNoteNum "unique"
    date deliveryDate
    int traderID FK
    decimal traderPrcnt
    decimal distributerPrcnt
    decimal Vat
}

palletsMatCost{
    int ID  PK
    int palletMatID "unique"
    date costFromDate
    date costTillDate
    decimal palletMatCost
}


invoice_lines{
    int ID PK   
    int invoiceHeaderID FK "unique"
    int deliveryNote_headerID FK "unique"
}


manufacturer_invoice{
    int ID PK
    int season "unique"
    int manufacturerInvNum "unique"
    decimal invoiceTotal
    date invoiceDate
    string invoiceNotes
}


invoice_header{
    int ID PK
    int season "unique"
    int invoiceNum "unique"
    int traderID
    date invoiceDate
    int manufacturerInvoiceID
}

receipt_lines{
    int ID PK
    int receiptHeaderID "unique"
    string  paymentType 
    int checkNum
    string bankName
    date paymentDueDate
    decimal sumPayment
}

receipt_header{
    int ID PK
    int season "unique"
    int receiptNum "unique"
    date receiptDate
    int InvoiceHeaderID FK
    string invoiceRemarks


}
```



# Server architecture – example:
 ![image](https://user-images.githubusercontent.com/58429034/198946377-daca0a82-c42b-40d2-9b22-fc45c9886b7b.png)


# Client structure:
 * Components:
      * General comp – Popups, Generic components (table, updatesection , add, edit, table
      * Login –contain username & password (JWT)
      * Main page – contains how all the pages will be designed (main table and infrastructure, actions & reports)
      * Rec_fruit_comp / local market– for each DB table, we can do CRUD
      
 * Redux:
      * For each of the folders above we have the store data updates abilities:
      * Set action types, actions, reducer 
      * Root reducer – combines all the reducer
      * Set of store

 * UTLs:
      * Connections to API
