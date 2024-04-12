from google.auth.transport import requests
from google.oauth2 import id_token


class Google:
    """Google class to fetch the user info and return it"""

    @staticmethod
    def validate(auth_token):
        """
        validate method queries the Google oAUTH2 api to fetch the user info
        :param auth_token:
        :return:
        """

        try:
            id_info = id_token.verify_oauth2_token(auth_token, requests.Request())
            if "accounts.google.com" in id_info["iss"]:
                return id_info
        except:
            return "The token is not valid or has expired"
