from enums.url_enums import General, Training
from enums.enums import Stats
import time
from . import driver, MAIN_LINK, HASH_CODE
from util import wait_until_find_xpath, wait_until_find_xpaths, log


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


