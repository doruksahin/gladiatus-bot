from util import wait_until_find_xpath, wait_until_find_xpaths, log
import time
from . import driver
from random import randint


BONUS_BOX = '//*[@id="blackoutDialogLoginBonus"]'



# Metin2 advertisement can appear.
def chk_ads():
    if wait_until_find_xpath(BONUS_BOX):
        wait_until_find_xpath(BONUS_BOX + "//button").click()  


def check_notifications():
  # Possible event such as level up could break automation, thus we have to check and click
  found = True
  if check_bonus():
    time.sleep(1)
  
  while found:
    link_notification = SELECTORS.get_notification()
    if not (link_notification):
      return False
      
    try:
      link_notification.click()
      log("Notification closed")
    except (NoSuchElementException, ElementNotVisibleException):
      found = False
      log("No notifications found")
      
  return True

        