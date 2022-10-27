from Models.Models import Plots


class Plots_DAL():
    def __init__(self):
        pass

    def get_all_plots(self):
        plots = Plots.query.all()
        return plots

    def add_plot(self, data):
        new_record = Plots(
            plotName=data['plotName'], isActive=data['isActive'])
        return new_record

    def delete_plot(self, id):
        status = Plots.query.filter(Plots.id == id).delete()
        return status

    def update_plot(self, plotID, data):
        record = Plots.query.filter_by(id=plotID).first()
        record.plotName = data['plotName']
        record.isActive = data['isActive']
        return ('plot was updated!')
