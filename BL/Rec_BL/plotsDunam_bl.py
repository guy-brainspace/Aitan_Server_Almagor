from DAL.Rec_DAL.plotsDunam_dal import PlotsDunam_DAL


class PlotsDunam_BL:
    def __init__(self):
        self.plotsDunam_dal = PlotsDunam_DAL()

    def get_plots(self, filteredSeason):
        plots = self.plotsDunam_dal.get_all_plots(filteredSeason)
        plots_list = []
        for plot in plots:
            # if plot.assamblyYear==None:
            #     plot.assamblyYear=''
            d = {}
            d['id'] = plot.id
            d['season'] = plot.season
            d['plotName'] = plot.plotName
            d['fruitTypeID'] = plot.fruitTypeID
            d['fruitType'] = plot.fruits.fruitType
            d['plantYear'] = plot.plantYear
            d['assamblyYear'] = plot.assamblyYear
            d['dunam'] = plot.dunam
            d['plotOwner'] = plot.plotOwner
            d['isActive'] = plot.isActive

            plots_list.append(d)

        return plots_list

    def add_plot(self, data):
        # if (data['assamblyYear']==''):
        #     data['assamblyYear']=None
        record = {
            'season': data['season'],            
            'plotName': data['plotName'],
            'fruitTypeID': data['fruitTypeID'],            
            'plantYear': data['plantYear'],     
            'assamblyYear': data['assamblyYear'],               
            'dunam': data['dunam'],            
            'plotOwner': data['plotOwner'],                     
            'isActive': data['isActive']
        }
        if (record['isActive'] == ''):
            record['isActive'] = False
        
        new_record = self.plotsDunam_dal.add_plot(record)
        return new_record

    def delete_plot(self, id):
        status = self.plotsDunam_dal.delete_plot(id)
        return status

    def update_plot(self, id, data):
        status = self.plotsDunam_dal.update_plot(id, data)
        return status

    def copy_prev_years_plots (self,prev_year ):
        plots_prev_year_list=self.get_plots(prev_year)
        currentPlots_list=[]
        for plot in plots_prev_year_list:
            if plot['isActive']==1:
                plot['season']=prev_year+1 #==current year
                new_record=self.add_plot(plot)
                currentPlots_list.append(new_record)
        return currentPlots_list

