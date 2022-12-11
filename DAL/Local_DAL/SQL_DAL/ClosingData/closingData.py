sql_query_closingData = '''
                select
                    c.id,
                    ph.season,
                    dh.deliveryNoteNum,
                    pl.id as fruitPalletCreationLineID,
                    t.traderName,
                    ph.palletNum,
                    f.fruitName,
                    f.fruitType,
                    fs.size,
                    mf.quality,
                    mpm.marketPackingType,
                    pl.packMatQty,
                    pl.weightNeto,
                    c.closeWeight,
                    c.closePrice,
                    c.closeDate,
                    c.closeRemarks
                from 
                fruitpalletcreation_lines pl 
                    left join fruitpalletcreation_header ph on (pl.fruitPalletCreation_headerID=ph.id)
                    left join deliverynote_lines dl on (dl.fruitPalletCreation_headerID=ph.id)
                    left join deliverynote_header dh on (dh.id=dl.deliveryNote_headerID)
                    left join traders t on (t.id=dh.traderID)
                    left join market_packing_mat mpm on (pl. marketPackingMatTypeID=mpm.id)
                    left join market_fruits mf on (pl.matketFruitID = mf.id)
                    left join fruits f on (mf.fruitID=f.id)
                    left join fruitsize fs on (mf.sizeID=fs.id)
                left join   closingdata c on (pl.id=c.fruitPalletCreationLineID)
                where ph.season =(%s)
                and deliveryNoteNum is not null
       
                            
'''
