sql_query_deliveryNote2prct = '''
                               
                    with allData as (
                    select
                        ph.palletNum,
                        f.fruitName,
                        f.fruitType,
                        fs.size,
                        mf.quality,
                        mpm.marketPackingType,
                        pl.packMatQty,
                        pl.weightNeto,
                        (pl.weightNeto*0.98) as weightNetoLess2prct
                    from deliverynote_header h
                        left join  deliverynote_lines l on (h.id=l.deliveryNote_headerID)
                        left join fruitpalletcreation_header ph on (l.fruitPalletCreation_headerID=ph.id)
                        left join fruitpalletcreation_lines pl on (ph.id = pl.fruitPalletCreation_headerID)
                        left join market_packing_mat mpm on (pl. marketPackingMatTypeID=mpm.id)
                        left join market_fruits mf on (pl.matketFruitID = mf.id)
                        left join fruits f on (mf.fruitID=f.id)
                        left join fruitsize fs on (mf.sizeID=fs.id)
                        where h.deliveryNoteNum=(%s)
                                        and h.season =(%s)
                    )
                    ,allData_pivot as(
                    select
                    If(Grouping(palletNum),'סהכ', palletNum) as  palletNum, 
                    If(Grouping(fruitName),'סהכ', fruitName) as  fruitName, 
                    If(Grouping(fruitType),'סהכ', fruitType) as  fruitType, 
                    If(Grouping(size),'סהכ', size) as  size, 
                    If(Grouping(quality),'סהכ', quality) as  quality, 
                    If(Grouping(marketPackingType),'סהכ', marketPackingType) as  marketPackingType,
                    sum(packMatQty) as packMatQty,
                    FORMAT(round(sum(weightNeto),0),0) as weightNeto,
                    FORMAT(round(sum(weightNetoLess2prct),0),0) as weightNetoLess2prct

                    from allData
                    Group By  palletNum, fruitName, fruitType, size, quality,  marketPackingType with rollup

                    )


                    select 
                    if(palletNum='סהכ', 'סהכ תעודת משלוח' , palletNum) as palletNum,
                    if(palletNum='סהכ', '' ,fruitName) as fruitName,
                    if(palletNum='סהכ', '' ,fruitType) as fruitType,
                    if(palletNum='סהכ', '' ,size) as size,
                    if(palletNum='סהכ', '' ,quality) as quality,
                    if (marketPackingType='סהכ','', marketPackingType) as marketPackingType,
                    if(palletNum='סהכ', '' ,packMatQty) as packMatQty,
                    weightNeto,
                    weightNetoLess2prct
                    from allData_pivot
                    where !(marketPackingType='סהכ' and quality!='סהכ' )
                    and !(quality='סהכ' and fruitName!='סהכ')
                    and !(fruitName='סהכ' and palletNum!='סהכ')

                            
'''
