from flask import make_response, request
import jwt
import os

from DAL.Users_DAL.users_dal import Users_DAL
from BL.Users_BL.users_bl import Users_BL


class Auth_BL:
    def __init__(self):
        self.__key = os.environ.get("DB_KEY")
        self.__algorithm =  os.environ.get("DB_ALGORITHM")

        self.users_dal = Users_DAL()
        self.users_bl = Users_BL()

    # ----------------------------------------------------------------------------------
    # ---2
    # Check existance of that user in data source and if exists - returns a unique value
    def __check_user(self, username, password):
        users_list = self.users_dal.get_all_users()
        for user in users_list:
            if user['userName'] == username and user['password'] == password:
                return user['id']

        return None

    # ---1
    def get_token(self, username, password):
        user_id = self.__check_user(
            username, password)  # verify against user DB
        if user_id is not None:
            token = jwt.encode({"id": user_id}, self.__key, self.__algorithm)
            return make_response({"token": token}, 200)
        else:
            return -1

    # ----------------------------------------------------------------------------------

    # ---4
    def verify_token(self, token):
        try:
            data = jwt.decode(token, self.__key, self.__algorithm)
            user_id = data["id"]
        except:
            user_id = 0

        users_all_data_list = self.users_bl.get_usernames()
        for u in users_all_data_list:
            if u["id"] == user_id:
                return True, u # == exist, user
        return False, []

    # ---3

    def token_verification(self):
        if request.headers and request.headers.get("x-access-token") != 'undefined':
            token = request.headers.get("x-access-token")
            exist, userData = self.verify_token(token)
            if exist:
                return userData
            else:
                return "not authorized"  # in case the client provided a token which is fake one
        else:
            return "not authorized"  # in case the client didnt provid any token
