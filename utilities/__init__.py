from selenium import webdriver
driver = webdriver.Chrome()
from util import wait_until_find_xpath, wait_until_find_xpaths, log
import time

MAIN_LINK = ""
HASH_CODE = ""
def login(id, password, server):
    global MAIN_LINK
    global HASH_CODE

    driver.get("https://tr.gladiatus.gameforge.com/game")
    time.sleep(3)
    wait_until_find_xpath(".//input[@id='login_username']").send_keys(id)
    wait_until_find_xpath(".//input[@id='login_password']").send_keys(password)
    drop_down_list = wait_until_find_xpath("//select[@id='login_server']")
    time.sleep(3)

    for i in drop_down_list.find_elements_by_xpath(".//option"):
        if str(server) in i.text:
            i.click()
            break
    wait_until_find_xpath(".//input[@id='loginsubmit']").click()
    MAIN_LINK = 'https://s{}-tr.gladiatus.gameforge.com/game/index.php'.format(server)
    HASH_CODE = driver.current_url.split("=")[4]

# login("bnmLe100Lesh", "dodo1234", 38)