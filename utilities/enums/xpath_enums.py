# from enum import Enum


class Character():
	HP = '//*[@id="header_values_hp_percent"]'
	EXP = '//*[@id="header_values_xp_percent"]'
	LVL = '//*[@id="header_values_level"]'
	RUBY = '//*[@id="sstat_ruby_val"]'

	STR = '//*[@id="char_f0"]' 
	AGI = '//*[@id="char_f1"]'
	DEX = '//*[@id="char_f2"]'
	END = '//*[@id="char_f3"]'
	CHA = '//*[@id="char_f4"]'
	INT = '//*[@id="char_f5"]'


class Cooldown():
	EXPEDITION =  '//*[@id="cooldown_bar_text_expedition"]'
	ARENA = '//*[@id="cooldown_bar_text_arena"]'
	DUNGEON = '//*[@id="cooldown_bar_text_dungeon"]'
	P_ARENA = ''
	CIRCUS = '//*[@id="cooldown_bar_text_ct"]'
	P_CIRCUS = ''


class ArenaAttack():
	FIRST = '//*[@id="content"]/article/aside[2]/section/table/tbody/tr[2]/td[1]/a'
	SECOND = '//*[@id="content"]/article/aside[2]/section/table/tbody/tr[3]/td[1]/a'
	THIRD = '//*[@id="content"]/article/aside[2]/section/table/tbody/tr[4]/td[1]/a'
	FOURTH = '//*[@id="content"]/article/aside[2]/section/table/tbody/tr[5]/td[1]/a'


class CircusAttack():
	pass


class Reporting():
	WIN = '//*[@class="reportWin"]'
	LOSE = ".//div[@class='reportLose']"
	GOLD = '//*[@id="content"]/div[2]/section/table/tbody/tr[1]/td/p[1]'


class Dungeon():
	RESTART_BUTTON = "//*[@id='content']/div[2]/div/form/table/tbody/tr/td[1]/input"


class Ads():
	BONUS_BOX = '//*[@id="blackoutDialogLoginBonus"]'


