from enums.url_enums import General, Training
from enums.xpath_enums import Character
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


def calculate_training_cost(stat, current):
	return 100


def calculate_ranged_training_cost(stat, current, range):
	return 200


def set_training_stat_frames(labels, cost_labels):
	values = []
	values.append("STR: " + driver.find_element_by_xpath(Character.STR).text)
	values.append("AGI: " + driver.find_element_by_xpath(Character.AGI).text)
	values.append("DEX: " + driver.find_element_by_xpath(Character.DEX).text)
	values.append("END: " + driver.find_element_by_xpath(Character.END).text)
	values.append("CHA: " + driver.find_element_by_xpath(Character.CHA).text)
	values.append("INT: " + driver.find_element_by_xpath(Character.INT).text)
	for i in range(len(labels)):
		labels[i]['text'] = values[i]

	cost_values =[]
	cost_values.append("Cost: {}".format(calculate_training_cost(0, int(driver.find_element_by_xpath(Character.STR).text))))
	cost_values.append("Cost: {}".format(calculate_training_cost(1, int(driver.find_element_by_xpath(Character.AGI).text))))
	cost_values.append("Cost: {}".format(calculate_training_cost(2, int(driver.find_element_by_xpath(Character.DEX).text))))
	cost_values.append("Cost: {}".format(calculate_training_cost(3, int(driver.find_element_by_xpath(Character.END).text))))
	cost_values.append("Cost: {}".format(calculate_training_cost(4, int(driver.find_element_by_xpath(Character.CHA).text))))
	cost_values.append("Cost: {}".format(calculate_training_cost(5, int(driver.find_element_by_xpath(Character.INT).text))))
	for i in range(len(cost_labels)):
		cost_labels[i]['text'] = cost_values[i]