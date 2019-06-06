import time
from . import driver


def waitUntilFindXpath(xpath):
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


def waitUntilFindXpaths(xpath):
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