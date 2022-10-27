from DAL.Local_DAL.fixedInfo_dal import FixedInfo_DAL


class FixedInfo_BL:
    def __init__(self):
        self.fixedInfo_dal = FixedInfo_DAL()

    def get_info(self):
        info = self.fixedInfo_dal.get_all_fixedInfo()
        info_list = []
        for t in info:
            d = {}
            d['name'] = t.name
            d['name_hebrew'] = t.name_hebrew
            d['value'] = t.value
            info_list.append(d)
        return info_list

    def update_info(self, infoName, data):
        status = self.fixedInfo_dal.update_info(infoName, data)
        return status
