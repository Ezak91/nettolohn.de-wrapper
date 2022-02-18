# from nettolohnde.model.salary_calculation_info import SalaryCalculationInfo


from utils.salary_utils import SalaryUtils


def calculate_net():

    cookie_value = SalaryUtils.get_cookie()
    print(cookie_value)
    # url = "https://www.nettolohn.de/"

    # payload = "salary_data%5Bmodus%5D=BN&salary_data%5Bsalary_brutto%5D=3550&salary_data%5Bis_glz%5D=0&salary_data%5Bperiod%5D=1&salary_data%5Bbav_brutto%5D=&salary_data%5Bgwv_brutto%5D=&salary_data%5Byear%5D=2022&salary_data%5Bfreibetrag%5D=&salary_data%5Btax_class%5D=1&salary_data%5Bfaktor%5D=0.9&salary_data%5Bis_church%5D=1&salary_data%5Bstate_id%5D=13&salary_data%5Bakb%5D=0&salary_data%5Bkv_status%5D=1&salary_data%5Bkv_satz%5D=14%2C6&salary_data%5Bkv_zuschlag%5D=1.6&salary_data%5Bpkv_brutto%5D=&salary_data%5Bpkv_chef%5D=1&salary_data%5Bhas_child%5D=0&salary_data%5Bchildren%5D=x&salary_data%5Bage%5D=30&salary_data%5Brv_status%5D=1&salary_data%5Bav_status%5D=1&salary_data%5Bworking_hours%5D=40&salary_data%5Bamount_salarys%5D=12&salary_data%5Bgeodb_loc_id%5D=&autocomplete_salary_data%5Bgeodb_loc_id%5D=&salary_data%5Bjob_id%5D=&autocomplete_salary_data%5Bjob_id%5D=&salary_data%5Bsector_id%5D=&autocomplete_salary_data%5Bsector_id%5D=&salary_data%5Bgender%5D=1"
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    #     "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Content-Type": "application/x-www-form-urlencoded",
    #     "Origin": "https://www.nettolohn.de",
    #     "Connection": "keep-alive",
    #     "Referer": "https://www.nettolohn.de/",
    #     # "Cookie": "nl_keks=3sk6aqq9imi5k6aa18ij6kk0rd; dsgvocookieconsent=2",
    #     "Upgrade-Insecure-Requests": "1",
    #     "Sec-Fetch-Dest": "document",
    #     "Sec-Fetch-Mode": "navigate",
    #     "Sec-Fetch-Site": "same-origin",
    #     "Sec-Fetch-User": "?1",
    # }

    # response = requests.request("POST", url, headers=headers, data=payload)


calculate_net()
