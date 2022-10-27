sql_query_invoiceLines = '''
                               
                    
                      with invoiceData as (
                        select 
                        dnh.deliveryDate,
                        dnh.deliveryNoteNum,
                        ph.palletNum,
                        f.fruitName,
                        f.fruitType,
                        fs.size,
                        mf.quality,
                        c.closePrice,
                        c.closeWeight,
                        c.closePrice *c.closeWeight as total
                        from invoice_header ih 
                        left join invoice_lines il on (il.invoiceHeaderID=ih.id)
                        left join deliveryNote_header dnh on (il.deliveryNote_headerID=dnh.id)
                        left join deliverynote_lines dnl on (dnl.deliveryNote_headerID=dnh.id)
                        left join fruitPalletCreation_header ph on (dnl.fruitPalletCreation_headerID=ph.id)
                        left join  fruitpalletcreation_lines pl on (pl.fruitPalletCreation_headerID=ph.id) 
                        left join closingData c on (c.fruitPalletCreationLineID=pl.id)
                        -- left join traders t on (t.id=dnh.traderID)
                        left join market_packing_mat mpm on (pl. marketPackingMatTypeID=mpm.id)
                        left join market_fruits mf on (pl.matketFruitID = mf.id)
                        left join fruits f on (mf.fruitID=f.id)
                        left join fruitSize fs on (mf.sizeID=fs.id)
                        -- left join palletsmat pm on (ph.palletMatID=pm.id)
                        -- left join manufacturer_invoice mi on (ih.manufacturerInvoiceID=mi.id)
                        where il.invoiceHeaderID=(%s)

                        )

                        , invoiceDataPivot as (
                        select

                        If(Grouping(fruitName),'סהכ', fruitName) as  fruitName, 
                        If(Grouping(fruitType),'סהכ', fruitType) as  fruitType, 
                        If(Grouping(size),'סהכ', size) as  size, 
                        If(Grouping(quality),'סהכ', quality) as  quality, 
                        If(Grouping(palletNum),'סהכ', palletNum) as  palletNum, 
                        If(Grouping(deliveryDate),'סהכ', deliveryDate) as  deliveryDate, 
                        If(Grouping(deliveryNoteNum),'סהכ', deliveryNoteNum) as  deliveryNoteNum, 
                        round(avg(closePrice),2)as closePrice,
                        round(sum(closeWeight),0 )as closeWeight,
                        round(sum(total),0) as total
                        from invoiceData
                        Group By  fruitName,  fruitType, size, quality,  palletNum, deliveryDate, deliveryNoteNum with rollup
                        order by If(Grouping(fruitName),'תתתת', fruitName), If(Grouping(fruitType),'תתתת', fruitType) , If(Grouping(palletNum),9999999, palletNum) 
                        )

                        select 
                        if(fruitName='סהכ', 'סהכ שורות' ,fruitName) as fruitName,
                        if(fruitType='סהכ', '' ,fruitType) as fruitType,
                        if(size='סהכ', '' ,size) as size,
                        if(quality='סהכ', '' ,quality) as quality,
                        if(palletNum='סהכ', '' ,palletNum) as palletNum,
                        if(deliveryDate='סהכ', '' ,deliveryDate) as deliveryDate,
                        if(deliveryNoteNum='סהכ', '' ,deliveryNoteNum) as deliveryNoteNum,

                        if(deliveryNoteNum='סהכ', '' ,closePrice) as closePrice,
                        closeWeight,
                        total
                        from invoiceDataPivot
                        where !(deliveryNoteNum='סהכ' and size!='סהכ' );

                            
'''
