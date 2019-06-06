from utilities.enums.enums import Stats, Areas, ExpeditionAttack
from utilities.func import train, login, getStats
from utilities import driver


if __name__ == '__main__':
	login("bnmLe100Lesh", "dodo1234", 38)
	getStats()
	#train(Stats.AGI)
	expedition(Areas.PIRATE_HARBOUR, ExpeditionAttack.FIRST)