from enums.xpath_enums import Reporting
import time
from . import driver, MAIN_LINK, HASH_CODE
from util import wait_until_find_xpath, wait_until_find_xpaths, log


expedition_area_links = ['?mod=location&loc={}&sh='.format(i) for i in range(7)]
expedition_buttons = ['//*[@id="expedition_list"]/div[{}]/div[2]/button'.format(i+1) for i in range(4)]
def expedition(stage, enemy):
    driver.get(MAIN_LINK + expedition_area_links[stage] + HASH_CODE)
    driver.find_element_by_xpath(expedition_buttons[enemy]).click()
    time.sleep(3)
    driver.get(MAIN_LINK + KARAKTER_URL + HASH_CODE)


def report_expedition():
    if wait_until_find_xpath(Reporting.WIN) != None:
        log("Battle won.")
    elif wait_until_find_xpath(Reporting.LOSE) != None:
        log("Battle lost.")
    else:
        log("Battle tie.")  