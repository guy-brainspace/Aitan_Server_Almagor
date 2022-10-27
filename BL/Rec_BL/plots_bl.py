from DAL.Rec_DAL.plots_dal import Plots_DAL


class Plots_BL:
    def __init__(self):
        self.plots_dal = Plots_DAL()

    def get_plots(self):
        plots = self.plots_dal.get_all_plots()
        plots_list = []
        for plot in plots:
            d = {}
            d['id'] = plot.id
            d['plotName'] = plot.plotName
            d['isActive'] = plot.isActive
            plots_list.append(d)

        return plots_list

    def add_plot(self, data):
        record = {'plotName': data['plotName'],  'isActive': data['isActive']}
        if (record['isActive'] == ''):
            record['isActive'] = False
        new_record = self.plots_dal.add_plot(record)
        return new_record

    def delete_plot(self, id):
        status = self.plots_dal.delete_plot(id)
        return status

    def update_plot(self, id, data):
        status = self.plots_dal.update_plot(id, data)
        return status
