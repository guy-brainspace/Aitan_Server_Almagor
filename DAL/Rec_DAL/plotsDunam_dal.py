from Models.Models import PlotsDunam


class PlotsDunam_DAL():
    def __init__(self):
        pass

    def get_all_plots(self, filteredSeason):
        if filteredSeason!=2999:
            plots = PlotsDunam.query.filter(PlotsDunam.season == filteredSeason).all()
        else:
             plots = PlotsDunam.query.all()
        return plots

    def add_plot(self, data):
        new_record = PlotsDunam(
            season=data['season'],
            plotName=data['plotName'],
            fruitTypeID=data['fruitTypeID'],
            plantYear=data['plantYear'],
            assamblyYear=data['assamblyYear'],
            dunam=data['dunam'],
            plotOwner=data['plotOwner'],
            isActive=data['isActive']    
            )
        return new_record

    def delete_plot(self, id):
        status = PlotsDunam.query.filter(PlotsDunam.id == id).delete()
        return status

    def update_plot(self, plotID, data):
        # if data['assamblyYear']=='':
            # data['assamblyYear']=None
        record = PlotsDunam.query.filter_by(id=plotID).first()
        record.season = data['season']
        record.plotName = data['plotName']
        record.fruitTypeID = data['fruitTypeID']
        record.plantYear = data['plantYear']
        record.assamblyYear = data['assamblyYear']
        record.dunam = data['dunam']
        record.plotOwner = data['plotOwner']
        record.isActive = data['isActive']
        return ('plot was updated!')
