sql_query_perDeal = '''
                with MonthlyData as (
                    select 

                    rec.id as recId,
                    rec.receivingDate,
                    rec.season,
                    rec.qtyInPacking,
                    rec.weightBruto,
                    growers.growerName,
                    rec.deliverNote,
                    packinghouse.packingHouseName,
                    packinghouse.location as packingHouseLocation,
                    plots.plotName,
                    fruits.fruitType,
                    fruits.fruitName,
                    dealnames.dealName,
                    packing_mat.packingType,
                    packing_mat.weight,
                    deals.id as DealsID,
                    deals.fromDate,
                    deals.toDate,
                    deals.price1,
                    deals.price1Date,
                    deals.price2,
                    deals.price2Date,
                    deals.price3,
                    deals.price3Date,
                    deals.price1 + deals.price2+ deals.price3 as total_price,
                    IF (packing_mat.packingType='מיכל', rec.weightBruto-(40*rec.qtyInPacking) ,IF(packing_mat.packingType='ארגז', rec.weightBruto-(1.5*rec.qtyInPacking)-15,IF(packing_mat.packingType='קרטון', rec.weightBruto-(0.65*rec.qtyInPacking)-15,0))) as weightNeto,

                    0.95* (IF (packing_mat.packingType='מיכל', rec.weightBruto-(40*rec.qtyInPacking) ,IF(packing_mat.packingType='ארגז', rec.weightBruto-(1.5*rec.qtyInPacking)-15,IF(packing_mat.packingType='קרטון', rec.weightBruto-(0.65*rec.qtyInPacking)-15,0))))  as total_weight_to_pay,

                    deals.price1*0.95* (IF (packing_mat.packingType='מיכל', rec.weightBruto-(40*rec.qtyInPacking) ,IF(packing_mat.packingType='ארגז', rec.weightBruto-(1.5*rec.qtyInPacking)-15,IF(packing_mat.packingType='קרטון', rec.weightBruto-(0.65*rec.qtyInPacking)-15,0)))) as payment1,

                    deals.price2*0.95* (IF (packing_mat.packingType='מיכל', rec.weightBruto-(40*rec.qtyInPacking) ,IF(packing_mat.packingType='ארגז', rec.weightBruto-(1.5*rec.qtyInPacking)-15,IF(packing_mat.packingType='קרטון', rec.weightBruto-(0.65*rec.qtyInPacking)-15,0)))) as payment2,


                    deals.price3*0.95* (IF (packing_mat.packingType='מיכל', rec.weightBruto-(40*rec.qtyInPacking) ,IF(packing_mat.packingType='ארגז', rec.weightBruto-(1.5*rec.qtyInPacking)-15,IF(packing_mat.packingType='קרטון', rec.weightBruto-(0.65*rec.qtyInPacking)-15,0)))) as payment3,

                    (deals.price1+deals.price2+deals.price3)* (0.95* (IF (packing_mat.packingType='מיכל', rec.weightBruto-(40*rec.qtyInPacking) ,IF(packing_mat.packingType='ארגז', rec.weightBruto-(1.5*rec.qtyInPacking)-15,IF(packing_mat.packingType='קרטון', rec.weightBruto-(0.65*rec.qtyInPacking)-15,0))))) as payment
                    from aitan_roni.receiving_fruits rec
                    left join aitan_roni.deals deals on rec.fruitTypeID=deals.fruitTypeID 
                                                                and rec.dealNameID=deals.dealNameID 
                                                                and rec.receivingDate between deals.fromDate and  deals.toDate
                    left join  aitan_roni.growers growers on rec.growerID=growers.id
                    left join  aitan_roni.packinghouse packinghouse on rec.packingHouseID=packinghouse.id
                    left join  aitan_roni.plots plots on rec.plotID=plots.id
                    left join  aitan_roni.fruits fruits on rec.fruitTypeID=fruits.id
                    left join  aitan_roni.dealnames dealnames on rec.dealnameID=dealnames.id
                    left join  aitan_roni.packing_mat packing_mat on rec.packingMaterialID=packing_mat.id
                    where rec.season= (%s)
                    and rec.growerID=(%s)
                    and month(rec.receivingDate)=(%s)
                    )

                    ,monthlyReportPivot as(
                    Select 
                    fruitName,
                    If(Grouping(fruitType),'', fruitType) as  fruitType, 
                    If(Grouping(dealName),'', dealName) as  dealName, 
                    price1,
                    price2,
                    price3,
                    If(Grouping(packingType),'', packingType) as  packingType, 
                    sum(qtyInPacking) as qtyInPacking,
                    FORMAT(round(sum(weightBruto),0),0) as weightBruto,
                    FORMAT(round(sum(weightNeto),0),0) as weightNeto,
                    FORMAT(round(sum(total_weight_to_pay),0),0) as total_weight_to_pay,
                    FORMAT(round(sum(payment),0),0) as payment

                    From MonthlyData
                    Group By  fruitName  , fruitType, dealName, packingType with rollup

                    )

                    ,monthlyReport_PackingPivot as(
                    select 
                    fruitName,  packingType, 
                    sum(qtyInPacking) as qtyInPacking, 
                    FORMAT(round(sum(weightBruto),0),0) as weightBruto,
                    FORMAT(round(sum(weightNeto),0),0) as weightNeto,
                    FORMAT(round(sum(total_weight_to_pay),0),0) as total_weight_to_pay,
                    FORMAT(round(sum(payment),0),0) as payment
                    from MonthlyData
                    group by fruitName, packingType 

                    )


                    select 
                    fruitName,
                    fruitType, 
                    dealName,
                    if (dealName='', '', price1) as price1,
                    if (dealName='', '', price2) as price2,
                    if (dealName='', '', price3) as price3,
                    packingType, 
                    if(packingType='','', qtyInPacking)  as qtyInPacking,
                    weightBruto,
                    weightNeto,
                    total_weight_to_pay,
                    payment
                    from monthlyReportPivot
                    where fruitName !=''
                    and !( dealName!='' and packingType='')

                    union all
                    select 
                    '' as fruitName,
                    '' as fruitType, 
                    '' as dealName,
                    '' as price1,
                    '' as price2,
                    '' as price3,
                    '' as packingType, 
                    '' as  qtyInPacking,
                    '' as weightBruto,
                    '' as  weightNeto,
                    '' as total_weight_to_pay,
                    '' as payment


                    union all

                    select 
                    fruitName,
                    '', -- as  fruitType
                    '', -- as  dealName
                    '', -- as price1
                    '', -- as price2
                    '', -- as price3
                    concat('סהכ ' ,packingType)  as packingType,
                    qtyInPacking,
                    weightBruto,
                    weightNeto,
                    total_weight_to_pay,
                    payment
                    from monthlyReport_PackingPivot
                    '''
