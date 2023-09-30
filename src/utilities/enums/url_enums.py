# from enum import Enum

class General():
	CHARACTER = "?mod=overview&sh="
	AUCTION = '?mod=auction&sh='
	M_AUCTION = 'mod=auction&ttype=3&sh='


class Unnecessary():
	YUKSEK_SKOR_URL = '?mod=highscore&sh='
	SILAH_URL = '?mod=inventory&sub=1&sh='
	ZIRH_URL = '?mod=inventory&sub=2&sh='
	PAZAR_YERI_URL = '?mod=inventory&sub=3&sh='
	SIMYACI_URL = '?mod=inventory&sub=4&sh='


class Pvp():
	ARENA = '?mod=arena&sh='
	P_ARENA = '?mod=arena&submod=serverArena&aType=2&sh='
	CIRCUS = '?mod=arena&submod=grouparena&sh='
	P_CIRCUS = "?mod=arena&submod=serverArena&aType=3&sh="


class Training():
	STR = '?mod=training&submod=train&skillToTrain=1&sh='
	AGI = '?mod=training&submod=train&skillToTrain=2&sh='
	DEX = '?mod=training&submod=train&skillToTrain=3&sh='
	END = '?mod=training&submod=train&skillToTrain=4&sh='
	CHA = '?mod=training&submod=train&skillToTrain=5&sh='
	INT = '?mod=training&submod=train&skillToTrain=6&sh='