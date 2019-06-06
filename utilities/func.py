from util import waitUntilFindXpath, waitUntilFindXpaths
from enums.enums import Stats
from enums.xpath_enums import Character, ExpeditionAttack
from enums.url_enums import General, Training
import time
from . import driver


BONUS_BOX = '//*[@id="blackoutDialogLoginBonus"]'
MAIN_LINK = ""
HASH_CODE = ""


def login(id, password, server):
    global MAIN_LINK
    global HASH_CODE

    driver.get("https://tr.gladiatus.gameforge.com/game")
    time.sleep(3)
    waitUntilFindXpath(".//input[@id='login_username']").send_keys(id)
    waitUntilFindXpath(".//input[@id='login_password']").send_keys(password)
    dropDownList = waitUntilFindXpath("//select[@id='login_server']")
    time.sleep(3)
    if waitUntilFindXpath(BONUS_BOX): # Arada cikan metin2 reklami
        waitUntilFindXpath(BONUS_BOX + "//button").click()
    for i in dropDownList.find_elements_by_xpath(".//option"):
        if str(server) in i.text:
            i.click()
            break
    waitUntilFindXpath(".//input[@id='loginsubmit']").click()
    MAIN_LINK = 'https://s{}-tr.gladiatus.gameforge.com/game/index.php'.format(server)
    HASH_CODE = driver.current_url.split("=")[4]



training_dict = {}
training_dict[Stats.STR] = Training.STR
training_dict[Stats.AGI] = Training.AGI
training_dict[Stats.DEX] = Training.DEX
training_dict[Stats.END] = Training.END
training_dict[Stats.CHA] = Training.CHA
training_dict[Stats.INT] = Training.INT
def train(stat):
    driver.get(MAIN_LINK + training_dict[stat] + HASH_CODE)
    time.sleep(2)
    driver.get(MAIN_LINK + General.CHARACTER + HASH_CODE)


def getStats():
    print("*********************")
    print("STR: " + driver.find_element_by_xpath(Character.STR).text)
    print("AGI: " + driver.find_element_by_xpath(Character.AGI).text)
    print("DEX: " + driver.find_element_by_xpath(Character.DEX).text)
    print("END: " + driver.find_element_by_xpath(Character.END).text)
    print("CHA: " + driver.find_element_by_xpath(Character.CHA).text)
    print("INT: " + driver.find_element_by_xpath(Character.INT).text)
    print("------")
    print("Hp: " + driver.find_element_by_xpath(Character.HP).text)
    print("Exp: " + driver.find_element_by_xpath(Character.EXP).text)
    print("Lvl: " + driver.find_element_by_xpath(Character.LVL).text)
    print("Ruby: " + driver.find_element_by_xpath(Character.RUBY).text)
    print("*********************")


def chk_life():
    if int(waitUntilFindXpath(Character.HP).text[:-1]) < 40:
        print("Canin %40'dan az. Daha sonra dene.")
        return False
    else:
        return True


expedition_area_links = ['?mod=location&loc={}&sh='.format(i) for i in range(7)]
expedition_buttons = ['//*[@id="expedition_list"]/div[{}]/div[2]/button'.format(i+1) for i in range(4)]
def expedition(stage, enemy):
    checkPopup()
    driver.get(MAIN_LINK + expedition_area_links[stage] + hash_code)
    driver.find_element_by_xpath(expedition_buttons[enemy]).click()
    time.sleep(3)
    checkPopup()
    browser.get(MAIN_LINK + KARAKTER_URL + hash_code)


def report_expedition():
  if waitUntilFindXpath(".//div[@class='reportWin']") != None:
            print("Canavar savasi kazanildi.")
        elif waitUntilFindXpath(".//div[@class='reportLose']") != None:
            print("Canavar savasi kaybedildi.")
        else:
            print("Canavar savasi berabere bitti.")  


expedition_area_links = ['?mod=dungeon&loc={}&sh='.format(i) for i in range(7)]
def dungeon(stage):
    pass