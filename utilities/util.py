import time
from datetime import datetime
from . import driver

def wait_until_find_xpath(xpath):
    t = True
    failCount = 0
    maxFail = 5

    while t and failCount < maxFail:
        try:
            element = driver.find_element_by_xpath(xpath)
            t = False
        except:
            t = True
            failCount = failCount + 1
            time.sleep(0.1)
    if (failCount == maxFail):
        return None
    else:
        return element


def wait_until_find_xpaths(xpath):
    t = True
    failCount = 0
    maxFail = 5

    while t and failCount < maxFail:
        try:
            element = driver.find_elements_by_xpath(xpath)
            t = False
        except:
            t = True
            failCount = failCount + 1
            time.sleep(0.1)
    if (failCount == maxFail):
        return None
    else:
        return element


def log(text):
  message = '['+str(datetime.now())+']$ '+ text
  file = open("automation.log","a") 
  file.write(message+'\n')
  file.close()
  print(message)