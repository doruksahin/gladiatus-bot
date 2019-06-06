from enum import Enum

class General(Enum):
	CHARACTER = "?mod=overview&sh="
	AUCTION = '?mod=auction&sh='
	M_AUCTION = 'mod=auction&ttype=3&sh='


class Unnecessary(Enum):
	YUKSEK_SKOR_URL = '?mod=highscore&sh='
	SILAH_URL = '?mod=inventory&sub=1&sh='
	ZIRH_URL = '?mod=inventory&sub=2&sh='
	PAZAR_YERI_URL = '?mod=inventory&sub=3&sh='
	SIMYACI_URL = '?mod=inventory&sub=4&sh='


class Expedition(Enum):
	HERMIT = '?mod=hermit&sh='
	STAGE_1 = '?mod=location&loc=0&sh='
	STAGE_2 = '?mod=location&loc=1&sh='
	STAGE_3 = '?mod=location&loc=2&sh='
	STAGE_4 = '?mod=location&loc=3&sh='
	STAGE_5 = '?mod=location&loc=4&sh='
	STAGE_6 = '?mod=location&loc=5&sh='
	STAGE_7 = '?mod=location&loc=6&sh='

class Dungeon(Enum):
	DUNGEON_1 = '?mod=dungeon&loc=0&sh='
	DUNGEON_2 = '?mod=dungeon&loc=1&sh='
	DUNGEON_3 = '?mod=dungeon&loc=2&sh='
	DUNGEON_4 = '?mod=dungeon&loc=3&sh='
	DUNGEON_5 = '?mod=dungeon&loc=4&sh='
	DUNGEON_6 = '?mod=dungeon&loc=5&sh='
	DUNGEON_7 = '?mod=dungeon&loc=6&sh='


class Pvp(Enum):
	ARENA = '?mod=arena&sh='
	P_ARENA = '?mod=arena&submod=serverArena&aType=2&sh='
	CIRCUS = '?mod=arena&submod=grouparena&sh='
	P_CIRCUS = "?mod=arena&submod=serverArena&aType=3&sh="


class Training(Enum):
	STR = '?mod=training&submod=train&skillToTrain=1&sh='
	AGI = '?mod=training&submod=train&skillToTrain=2&sh='
	DEX = '?mod=training&submod=train&skillToTrain=3&sh='
	END = '?mod=training&submod=train&skillToTrain=4&sh='
	CHA = '?mod=training&submod=train&skillToTrain=5&sh='
	INT = '?mod=training&submod=train&skillToTrain=6&sh='