from DAL.Users_DAL.users_dal import Users_DAL


class Users_BL():
    def __init__(self):
        self.users_dal = Users_DAL()


# -------------- for login ---------------------


    def get_usernames(self):
        users_DB = self.users_dal.get_all_users()
        username_list = []

        for ud in users_DB:
            u = {}
            u["id"] = ud["id"]
            u["userName"] = ud["userName"]
            username_list.append(u)
        return username_list
