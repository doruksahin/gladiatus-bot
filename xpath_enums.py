from enum import Enum


class Statistic(Enum):
	HP = '//*[@id="header_values_hp_percent"]'
	EXP = '//*[@id="header_values_xp_percent"]'
	LVL = '//*[@id="header_values_level"]'
	RUBY = '//*[@id="sstat_ruby_val"]'


class Cooldown(Enum):
	EXPEDITION =  '//*[@id="cooldown_bar_text_expedition"]'
	ARENA = '//*[@id="cooldown_bar_text_arena"]'
	DUNGEON = '//*[@id="cooldown_bar_text_dungeon"]'
	P_ARENA = ''
	CIRCUS = '//*[@id="cooldown_bar_text_ct"]'
	P_CIRCUS = ''


class ExpeditionAttack(Enum):
	FIRST = '//*[@id="expedition_list"]/div[1]/div[2]/button'
	SECOND = '//*[@id="expedition_list"]/div[2]/div[2]/button'
	THIRD = '//*[@id="expedition_list"]/div[3]/div[2]/button'
	FOURTH = '//*[@id="expedition_list"]/div[4]/div[2]/button'


class ArenaAttack(Enum):
	FIRST = '//*[@id="content"]/article/aside[2]/section/table/tbody/tr[2]/td[1]/a'
	SECOND = '//*[@id="content"]/article/aside[2]/section/table/tbody/tr[3]/td[1]/a'
	THIRD = '//*[@id="content"]/article/aside[2]/section/table/tbody/tr[4]/td[1]/a'
	FOURTH = '//*[@id="content"]/article/aside[2]/section/table/tbody/tr[5]/td[1]/a'


class CircusAttack(Enum):
	pass


class Reporting(Enum):
	IS_WIN = '//*[@class="reportWin"]'
	GOLD = '//*[@id="content"]/div[2]/section/table/tbody/tr[1]/td/p[1]' 


