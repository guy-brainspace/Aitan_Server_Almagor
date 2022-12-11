sql_query_palletCost = '''
                               
                   with palletsCount as(
                        select 
                        pm.palletType,
                        ph.palletNum,
                        pmc.palletMatCost,
                        dnh.VAT,
                        pmc.palletMatCost*dnh.VAT as total
                        from invoice_header ih 
                        left join invoice_lines il on (il.invoiceHeaderID=ih.id)
                        left join deliverynote_header dnh on (il.deliveryNote_headerID=dnh.id)
                        left join deliverynote_lines dnl on (dnl.deliveryNote_headerID=dnh.id)
                        left join fruitpalletcreation_header ph on (dnl.fruitPalletCreation_headerID=ph.id)
                        left join palletsmat pm on (ph.palletMatID=pm.id)
                        left join palletsmatcost pmc on (pmc.palletMatID=pm.id
                                                                        and (dnh.deliveryDate>=pmc.fromDate and dnh.deliveryDate<=pmc.toDate)
                                                                        )
                        where il.invoiceHeaderID=(%s)

                        )

                        , palletsCountPivot as(
                        select 
                        If(Grouping(palletType),'סהכ', palletType) as  palletType, 
                        If(Grouping(palletNum),'סהכ',palletNum) as  palletNum, 
                        If(Grouping(palletMatCost), 'סהכ', palletMatCost) as  palletMatCost, 
                        If(Grouping(VAT),'סהכ',VAT) as  VAT, 
                        round(sum(total),2) as total
                        from palletsCount
                        group by palletType, palletNum, palletMatCost, VAT with rollup
                        )

                        select 
                        if(palletType='סהכ', 'סהכ עלות משטחים' ,palletType) as palletType,
                        if(palletNum='סהכ', '' ,palletNum) as palletNum,
                        if(palletMatCost='סהכ', '' ,palletMatCost) as palletMatCost,
                        if(VAT='סהכ', '' ,VAT) as VAT,
                        total
                        from palletsCountPivot
                        where !(VAT='סהכ' and palletNum!='סהכ');

                            
'''
