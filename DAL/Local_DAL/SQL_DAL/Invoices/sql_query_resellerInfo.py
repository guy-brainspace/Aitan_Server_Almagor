sql_query_resellerInfo = '''                
                                
                with reseler_part as(
                    select 
                    ih.invoiceNum,
                    dnh.traderPrcnt,
                    dnh.distributerPrcnt,
                    dnh.VAT,
                    dnh.traderPrcnt+dnh.distributerPrcnt as total_reseller_prct,
                    -1*sum(c.closePrice *c.closeWeight) *(dnh.traderPrcnt+dnh.distributerPrcnt) as total_reseller_fee,
                    -1*sum(c.closePrice *c.closeWeight) *(dnh.traderPrcnt+dnh.distributerPrcnt)*dnh.VAT as VAT_cost,
                    (-1*sum(c.closePrice *c.closeWeight) *(dnh.traderPrcnt+dnh.distributerPrcnt))+(-1*sum(c.closePrice *c.closeWeight) *(dnh.traderPrcnt+dnh.distributerPrcnt)*dnh.VAT) as total_reduce_per_reseller
                    from invoice_header ih 
                    left join invoice_lines il on (il.invoiceHeaderID=ih.id)
                    left join deliverynote_header dnh on (il.deliveryNote_headerID=dnh.id)
                    left join deliverynote_lines dnl on (dnl.deliveryNote_headerID=dnh.id)
                    left join fruitpalletcreation_header ph on (dnl.fruitPalletCreation_headerID=ph.id)
                    left join  fruitpalletcreation_lines pl on (pl.fruitPalletCreation_headerID=ph.id) 
                    left join closingdata c on (c.fruitPalletCreationLineID=pl.id)
                    where il.invoiceHeaderID=(%s)
                    group by invoiceNum, VAT, traderPrcnt, distributerPrcnt
                    )

                    select 
                    max(traderPrcnt)+max(distributerPrcnt) as reseller_prct,
                    round(sum(total_reseller_fee),2) as total_reseller_fee,
                    round(sum(VAT_cost),2) as total_vat_cost,
                    round(sum(total_reduce_per_reseller),2) as total_reduction_fee
                    from reseler_part
                    group by invoiceNum
                            
'''
