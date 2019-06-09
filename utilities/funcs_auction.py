#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enums.url_enums import General
from util import wait_until_find_xpath, wait_until_find_xpaths, log
import os
from . import driver, MAIN_LINK, HASH_CODE
import time
import re



# Higher freq for main auction
# Longer noise for "too short" notification


# Parse values for better result.
def parse_data():
	text = '[[["Uzun k\u0131l\u0131\u00e7 g\u00fc\u00e7","lime; text-shadow: 0 0 2px #000, 0 0 2px lime"],["Hasar 21 - 26","#DDD"],["G\u00fc\u00e7 +10% (+2)","#DDD"],["Seviye 19","#808080"],["De\u011fer 1.321 <div class=\"icon_gold\"><\/div>","#DDDDDD"],["Dayan\u0131kl\u0131l\u0131k 28109\/28109 (100%)","#00ff00"],["Ar\u0131nd\u0131rma 0\/7028 (0%)","#808080"]],[["Elywens Sava\u015f Ora\u011f\u0131","lime; text-shadow: 0 0 2px #000, 0 0 2px lime"],["\u015eunun ruhuna ba\u011fl\u0131: bnmLe100Lesh","#DDD"],["Hasar 32 - 43","#DDD"],["Sa\u011fl\u0131k +180","#DDD"],["Beceri +5% (+2)","#DDD"],["\u00c7eviklik +5% (+3)","#DDD"],["Dayan\u0131kl\u0131l\u0131k +5% (+1)","#DDD"],["Seviye 28","#808080"],["De\u011fer 2.201 <div class=\"icon_gold\"><\/div>","#DDDDDD"],["Dayan\u0131kl\u0131l\u0131k 41983\/43028 (97%)","#06f800"],["Ar\u0131nd\u0131rma 0\/10758 (0%)","#808080"]]]'
	pattern = '\[?\w+]?'
	re.findall(pattern, text)	


# Should be together?
def beep_when_too_short():
	duration = 5  # seconds
	freq = 640  # Hz
	links = [MAIN_LINK + General.AUCTION + HASH_CODE, MAIN_LINK + General.M_AUCTION + HASH_CODE]
	for link in links:
		freq -= 200
		browser.get(link)
		remaining_time = driver.find_element_by_xpath('//*[@id="content"]/article/p[1]/span[2]/b').text
		if remaining_time == "çok kısa":
			os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))


# TODO: Save xpath of founded item.
def beep_when_decent_item_found(when=None):
	duration = 2  # seconds
	freq = 640  # Hz
	links = [MAIN_LINK + General.AUCTION + HASH_CODE, MAIN_LINK + General.M_AUCTION + HASH_CODE]

	for link in links:
		freq -= 200
		driver.get(link)
		remaining_time = driver.find_element_by_xpath('//*[@id="content"]/article/p[1]/span[2]/b').text.encode('utf-8')
		driver.find_element_by_xpath("//select[@name='itemType']/option[text()='Hepsi']").click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@id="content"]/article/section[1]/form/table/tbody/tr[5]/td/input').click()
		log("Remaining time: {}".format(remaining_time))
		time.sleep(2)
		
		row_count = len(driver.find_elements_by_xpath('//div[@id="auction_table"]/table/tbody/tr'))
		for i in range(row_count):
			item_tuple = driver.find_elements_by_xpath('//div[@id="auction_table"]/table/tbody/tr[{}]/td'.format(i+1))
			for j in range(2):
				item_has_bid = driver.find_element_by_xpath('//div[@id="auction_table"]/table/tbody/tr[{}]/td[{}]/div/form/div[@class="auction_bid_div"]/div'.format(i+1, j+1)).text.encode('utf-8')
				item_price = driver.find_element_by_xpath('//div[@id="auction_table"]/table/tbody/tr[{}]/td[{}]/div/form/div[@class="auction_bid_div"]/div[2]'.format(i+1, j+1)).text.encode('utf-8')
				# bid_item = driver.find_elements_by_xpath('//div[@id="auction_table"]/table/tbody/tr[{}]/td[{}]/div/form/div[@class="auction_bid_div"]/input[2]'.format(i+1, j+1)).click()
				# enter_item_price = item.find_element_by_xpath('/div/form/div[@id="auction_bid_div"]/input').send_keys()

				item_attributes = driver.find_element_by_xpath('//div[@id="auction_table"]/table/tbody/tr[{}]/td[{}]/div/form/div[@class="auction_item_div"]/div/div'.format(i+1, j+1))
				item_data = item_attributes.get_attribute("data-tooltip").encode('utf-8')
				if "D\u00f6v\u00fc\u015f" in item_data:
					print("Bid: {}".format(item_price))
					print("Has bid: {}".format(item_has_bid))
					print("Item_data: {}".format(item_data))
					os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
					time.sleep(5)


def bid_for_safe():
	pass


"ş: \u015f"
"ç: \u00e7"
"ğ: \u011f"
"ü: \u00fc"
"ö: \u00f6"
"ı: \u0131"

"İ: \u0130"
"Ü: \u00dc"
"Ö: \u00d6"
"Ç: \u00c7"
"Ş: \u015e"

