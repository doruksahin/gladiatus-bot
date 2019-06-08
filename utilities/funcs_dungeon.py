from enums.xpath_enums import Dungeon, Reporting
from random import randint
from pyautogui import *
import time
from . import driver, MAIN_LINK, HASH_CODE
from util import wait_until_find_xpath, wait_until_find_xpaths, log


def should_i_continue_dungeon(fail_count, max_fail):
    if not wait_until_find_xpath(Reporting.WIN):
        fail_count += 1
        log("Lost {} times in a row.".format(fail_count))
        if max_fail == fail_count:
            log("Restarting because: Lost {} times in a row.".format(fail_count))
            abandon_dungeon_button = driver.find_element_by_xpath('//input[@type="submit"]')
            time.sleep(5)
            abandon_dungeon_button.click()
    else:
        log("Battle won.")


# Chk if dungeon need to be restarted, or not.
# Restart if needed.
def restart_dungeon_if_needed():
    restart_dungeon_button = wait_until_find_xpath(Dungeon.RESTART_BUTTON)

    if(restart_dungeon_button != None):
        log("Dungeon restarted.")
        restart_dungeon_button.click()
        time.sleep(10)


dungeon_area_links = ['?mod=dungeon&loc={}&sh='.format(i) for i in range(7)]
def dungeon_loop(dungeon, repeat_count=1, max_fail=2, skip_boss=False):
    DUNGEON_URL = MAIN_LINK + dungeon_area_links[dungeon] + HASH_CODE
    print(DUNGEON_URL)
    counter = 0
    fail_count = 0
    while repeat_count > counter:
        boss_pic = None
        counter += 1
        driver.get(DUNGEON_URL)
        time.sleep(3)
        restart_dungeon_if_needed()

        try:
            log("Searching boss...")
            boss_pic = locateCenterOnScreen("boss.png")
        except:
            log("Boss not found.")

        if skip_boss and boss_pic:
            log("Skipping boss...")
            driver.find_element_by_xpath('//input[@type="submit"]').click()
            continue

        try:
            log("Searching image...")
            enemy_pic = locateCenterOnScreen("attack.png")
            click(enemy_pic)
            fail_count = should_i_continue_dungeon(fail_count=fail_count, max_fail=max_fail)
            time.sleep(65 + randint(0,10))
        except:
            if repeat_count > counter:
                log("No life left. Waiting...")
                time.sleep(900 + randint(0,10))


