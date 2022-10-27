sql_summarySeasonGrowers = '''

               with summaryGrowerData as (
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
                )

                , summaryGrowerDataPivot as(
                Select 
                If(Grouping(growerName),'', growerName) as  growerName, 
                If(Grouping(fruitName),'', fruitName) as  fruitName, 
                If(Grouping(fruitType),'', fruitType) as  fruitType, 
                FORMAT(round(sum(weightNeto),0),0) as weightNeto,
                FORMAT(round(sum(total_weight_to_pay),0),0) as total_weight_to_pay,
                FORMAT(round(sum(payment),0),0) as payment
                From summaryGrowerData
                Group By  growerName, fruitName, fruitType with rollup

                )

                , summaryGrowers as(
                select 
                fruitName,   
                FORMAT(round(sum(weightNeto),0),0) as weightNeto,
                FORMAT(round(sum(total_weight_to_pay),0),0) as total_weight_to_pay,
                FORMAT(round(sum(payment),0),0) as payment
                from summaryGrowerData
                group by fruitName
                order by fruitName

                )


                select 
                growerName,
                fruitName,
                fruitType,
                weightNeto,
                total_weight_to_pay,
                payment
                from summaryGrowerDataPivot
                where !(growerName='' and payment !='' and fruitType='')

                union all 
                select 
                '' as growerName,
                '' as fruitName,
                '' as fruitType,
                '' as weightNeto,
                '' as total_weight_to_pay,
                '' as payment

                union all 

                select 
                '' as growerName,
                fruitName,
                '' as fruitType,
                weightNeto,
                total_weight_to_pay,
                payment
                from summaryGrowers
                '''
