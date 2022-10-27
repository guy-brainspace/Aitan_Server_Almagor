from Models.Models import Fixedinfo


class FixedInfo_DAL():
    def __init__(self):
        pass

    def get_all_fixedInfo(self):
        Allinfo = Fixedinfo.query.all()
        return Allinfo

    def update_info(self, InfoName, data):
        record = Fixedinfo.query.filter_by(name=InfoName).first()
        record.name = data['name']
        record.name_hebrew = data['name_hebrew']
        record.value = data['value']
        return ('info was updated!')
