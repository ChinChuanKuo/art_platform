def solution_website(json):
    from selenium import webdriver
    from chromedriver_py import binary_path
    from selenium.webdriver.support.ui import Select
    from time import sleep
    json_data = json["info"]
    url = "https://member.moc.gov.tw/MOCMC/T0001/list?SYS_ID=EVENT_CKSMH"
    driver = webdriver.Chrome(executable_path=binary_path)
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_xpath("//input[@id='ACCOUNT']").send_keys(json_data["account"])
    driver.find_element_by_xpath("//input[@id='PASSWORD']").send_keys(json_data["password"])
    sleep(8)
    driver.find_element_by_xpath("(//input[@class='btn bg_green btn-lg btn-block'])").click()
    sleep(2)
    driver.find_element_by_xpath("(//a[@class='menuLink menuTw'])[5]").click()
    sleep(2)
    driver.find_element_by_xpath("//input[@id='form1_queryBean_searchActName']").send_keys(json_data["searchKey"])
    driver.find_element_by_xpath("(//div[@class='search'])").find_element_by_xpath("(//input[@value='送出'])").click()
    sleep(20)

def get_json():
    import json
    with open("main.json", "r") as f:
        data = json.load(f)
        return data

if __name__ == "__main__":
    solution_website(get_json())