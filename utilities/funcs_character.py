from enums.xpath_enums import Character
from . import driver, MAIN_LINK, HASH_CODE
from util import wait_until_find_xpath, wait_until_find_xpaths, log


def get_stats():
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
    if int(wait_until_find_xpath(Character.HP).text[:-1]) < 40:
        log("Health is lower than %40")
        return False
    else:
        return True


def drag_item():
    log("Dragging food")
    actionChains = ActionChains(driver)
    actionChains.drag_and_drop(selected_element, avatar).perform()