from utilities.enums.enums import Stats, Areas, ExpeditionAttack
#from utilities.funcs import login
from utilities.funcs_training import train
from utilities.funcs_character import get_stats
from utilities.funcs_dungeon import dungeon_loop
from utilities import driver

import Tkinter,tkFileDialog
import Tkinter as tk
from Tkinter import *
from tkinter import ttk
import tkMessageBox


def get_auction_time():
	pass




if __name__ == '__main__':
	root = Tkinter.Tk()
	

	tab_control = ttk.Notebook(root)
	character_tab = ttk.Frame(tab_control)            
	arena_tab = ttk.Frame(tab_control)
	auction_tab = ttk.Frame(tab_control)

	tab_control.add(character_tab, text='character')
	tab_control.add(arena_tab, text='Arena')
	tab_control.add(auction_tab, text='Auction')
	tab_control.pack(expand=1, fill="both")  # Pack to make visible
	root.mainloop()

	#login("bnmLe100Lesh", "dodo1234", 38)
	# get_stats()
	#train(Stats.AGI)
	#expedition(Areas.PIRATE_HARBOUR, ExpeditionAttack.FIRST)
	#dungeon_loop(dungeon=Areas.MISTY_MOUNTAINS, repeat_count=200)