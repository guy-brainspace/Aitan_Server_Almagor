sql_query_palletsWOinvoices = '''

                      select 
                        deliveryDate,
                        deliveryNoteNum,
                        palletNum,
                        fruitName,
                        fruitType, 
                        size, 
                        quality
                        from deliverynote_header dnh
                        left join deliverynote_lines dnl on (dnl.deliveryNote_headerID=dnh.id)
                        left join invoice_lines il on (il.deliveryNote_headerID=dnh.id)
                        left join fruitpalletcreation_header ph on (dnl.fruitPalletCreation_headerID=ph.id)
                        left join  fruitpalletcreation_lines pl on (pl.fruitPalletCreation_headerID=ph.id) 
                        left join market_packing_mat mpm on (pl. marketPackingMatTypeID=mpm.id)
                        left join market_fruits mf on (pl.matketFruitID = mf.id)
                        left join fruits f on (mf.fruitID=f.id)
                        left join fruitsize fs on (mf.sizeID=fs.id)
                        left join traders t on (t.id=dnh.traderID)
                        where il.id is null
                        and dnl.id is not null
                        and deliveryDate>=(%s)and deliveryDate<=(%s)
                        and traderID=(%s)
               
'''
