from utilities.enums.enums import Stats, Areas, ExpeditionAttack
#from utilities.funcs import login
from utilities.funcs_training import train
from utilities.funcs_character import get_stats
from utilities.funcs_dungeon import dungeon_loop
from utilities.funcs_auction import beep_when_decent_item_found
from utilities import driver


if __name__ == '__main__':
	#login("bnmLe100Lesh", "dodo1234", 38)
	# get_stats()
	#train(Stats.AGI)
	#expedition(Areas.PIRATE_HARBOUR, ExpeditionAttack.FIRST)
	#dungeon_loop(dungeon=Areas.WOLF_CAVE, repeat_count=200, skip_boss=True)
	beep_when_decent_item_found(0)