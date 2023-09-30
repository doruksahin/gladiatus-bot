import time
from src.util import util
from src import driver

MAIN_LINK = ""
HASH_CODE = ""
LOGIN_PAGE_URL = "https://lobby.gladiatus.gameforge.com/en_GB/"
def login(id, password, server):
    global MAIN_LINK
    global HASH_CODE

    driver.get(LOGIN_PAGE_URL)
    time.sleep(3)
    try:
        util.wait_until_find_xpath("//button[text()='Accept Cookies']").click()
        time.sleep(0.5)
        util.wait_until_find_xpath('//ul[@class="tabsList"]/li[1]').click()
        print("sa")

        util.wait_until_find_xpath("//*[@id='loginForm']/div[2]/div/input").send_keys(id)
        util.wait_until_find_xpath("//*[@id='loginForm']/div[3]/div/input").send_keys(password)
        util.wait_until_find_xpath("//button[text()='Log in']").click()
        time.sleep(3)

        util.wait_until_find_xpath('//*[@class="openX_interstitial"]/div[@class="openX_int_closeButton"]/a').click()
        util.wait_until_find_xpath("//button[text()='Play']").click()
        util.wait_until_find_xpath("//button[text()='Play']").click()
        MAIN_LINK = 'https://s{}-en.gladiatus.gameforge.com/game/index.php'.format(server)
    except:
        time.sleep(20)
        raise



login("doruksahindev@gmail.com", "Knmd447345!", 66)
