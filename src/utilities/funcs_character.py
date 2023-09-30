from enums.xpath_enums import Character, Cooldown, PointRemaining, PointMax, ArenaRank
from . import driver
from src.util.util import wait_until_find_xpath, log


def set_stat_labels(labels):
    values = []
    values.append("STR: " + driver.find_element_by_xpath(Character.STR).text)
    values.append("AGI: " + driver.find_element_by_xpath(Character.AGI).text)
    values.append("DEX: " + driver.find_element_by_xpath(Character.DEX).text)
    values.append("END: " + driver.find_element_by_xpath(Character.END).text)
    values.append("CHA: " + driver.find_element_by_xpath(Character.CHA).text)
    values.append("INT: " + driver.find_element_by_xpath(Character.INT).text)
    for i in range(len(labels)):
        labels[i]['text'] = values[i]


def set_hp_labels(labels):
    values = []
    values.append("Hp: " + driver.find_element_by_xpath(Character.HP).text)
    values.append("Exp: " + driver.find_element_by_xpath(Character.EXP).text)
    values.append("Lvl: " + driver.find_element_by_xpath(Character.LVL).text)
    values.append("Ruby: " + driver.find_element_by_xpath(Character.RUBY).text)
    values.append("Rank: " + driver.find_element_by_xpath(Character.RANK).text)
    values.append("Gold: " + driver.find_element_by_xpath(Character.GOLD).text)
    for i in range(len(labels)):
        labels[i]['text'] = values[i]


def set_character_item_labels(labels):
    item_data_array = []
    for i in range(len(labels)):
        item = driver.find_element_by_xpath('//div[@id="char"]/div[@class="ui-droppable"][{}]/div'.format(i+1))
        item_data = item.get_attribute("data-tooltip").encode('utf-8')
        print(item_data)
        item_data_array.append(item_data)

    for i in range(len(labels)):
        labels[i]['text'] = item_data_array[i]


def set_point_labels(labels):
    points = []
    points.append("{}/{} - Expedition: {}".format(driver.find_element_by_xpath(PointRemaining.EXPEDITION).text, driver.find_element_by_xpath(PointMax.EXPEDITION).text, driver.find_element_by_xpath(Cooldown.EXPEDITION).text.encode('utf-8')))
    points.append("{} - Arena: {}".format(driver.find_element_by_xpath(ArenaRank.ARENA).text, driver.find_element_by_xpath(Cooldown.ARENA).text.encode('utf-8')))
    points.append("{}/{} - Dungeon: {}".format(driver.find_element_by_xpath(PointRemaining.DUNGEON).text, driver.find_element_by_xpath(PointMax.DUNGEON).text, driver.find_element_by_xpath(Cooldown.DUNGEON).text.encode('utf-8')))
    points.append("{} - Circus: {}".format(driver.find_element_by_xpath(ArenaRank.CIRCUS).text, driver.find_element_by_xpath(Cooldown.CIRCUS).text.encode('utf-8')))
    for i in range(len(labels)):
        labels[i]['text'] = points[i]


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