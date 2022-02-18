import requests

MAIN_URL = "https://www.nettolohn.de"


class SalaryUtils:
    """class for the salary utils"""

    def get_cookie() -> str:
        """call nettolohn.de and get a cookie for requests

        Returns:
            str: the cookie value
        """
        payload = {}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) \
                Gecko/20100101 Firefox/97.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,\
                image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
        }

        response = requests.request("GET", MAIN_URL, headers=headers, data=payload)

        cookies_dict = response.cookies.get_dict()
        cookie_value = cookies_dict["nl_keks"]
        return cookie_value
