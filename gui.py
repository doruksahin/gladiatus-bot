import Tkinter,tkFileDialog
import Tkinter as tk
from Tkinter import *
from tkinter import ttk
import tkMessageBox


def get_auction_time():
	pass


def calculate_training_cost(attribute, attribute_value):
	pass


wanted_items_list = []
def add_wanted_item(keyword):
	wanted_items_list.append(keyword)
	wanted_items_listbox.insert(END, keyword)


def set_selected_index(evt):
    global selected
    w = evt.widget
    index = int(w.curselection()[0])
    selected = index
    print("Selected item:", selected)


def set_selected_auction_chk_frequency(evt)
	global auction_chk_frequency_type
    w = evt.widget
    auction_chk_frequency_type = int(w.curselection()[0])


def delete_wanted_item():
	# wanted_items_list.remove()
	wanted_items_listbox.delete(selected)


def populate_auction_refresh_rate_listbox(listbox):
	listbox.insert(END, "second(s)")
	listbox.insert(END, "minute(s)")
	listbox.insert(END, "hour(s)")



if __name__ == '__main__':
	root = Tkinter.Tk()
	tab_control = ttk.Notebook(root)

	character_tab = ttk.Frame(tab_control)
	mercenaries_tab = ttk.Frame(tab_control)
	training_tab = ttk.Frame(tab_control)            
	arena_tab = ttk.Frame(tab_control)
	auction_tab = ttk.Frame(tab_control)
	suggestion_tab = ttk.Frame(tab_control)


	# character tab
	character_frame = Frame(character_tab)
	character_frame.pack()


	# mercenaries tab
	mercenaries_frame = Frame(mercenaries_tab)
	mercenaries_frame.pack()


	# training tab
	training_frame = Frame(training_tab)
	training_frame.pack()
	do_training_frame = Frame(training_frame)
	do_training_frame.pack(side=LEFT)

	str_frame = Frame(do_training_frame)
	str_frame.pack(side=TOP)
	Label(str_frame, text="STR").pack(side=LEFT)
	str_current_label = Label(str_frame, text= "Current {}".format(current_str))
	str_current_label.pack(side=LEFT)
	str_train_button = Button(str_frame, text="+", command=train(Stats.STR))
	str_train_button.pack(side=LEFT)
	str_train_cost = Label(str_frame, "Cost: {}".format(calculate_training_cost(Stats.STR, current_str)))
	str_train_cost.pack(side=LEFT)

	agi_frame = Frame(do_training_frame)
	agi_frame.pack(side=TOP)
	Label(agi_frame, text="AGI").pack(side=LEFT)
	agi_current_label = Label(agi_frame, text= "Current {}".format(current_agi))
	agi_current_label.pack(side=LEFT)
	agi_train_button = Button(agi_frame, text="+", command=train(Stats.AGI))
	agi_train_button.pack(side=LEFT)
	agi_train_cost = Label(agi_frame, "Cost: {}".format(calculate_training_cost(Stats.AGI, current_agi)))
	agi_train_cost.pack(side=LEFT)

	dex_frame = Frame(do_training_frame)
	dex_frame.pack(side=TOP)
	Label(dex_frame, text="DEX").pack(side=LEFT)
	dex_current_label = Label(dex_frame, text= "Current {}".format(current_dex))
	dex_current_label.pack(side=LEFT)
	dex_train_button = Button(dex_frame, text="+", command=train(Stats.DEX))
	dex_train_button.pack(side=LEFT)
	dex_train_cost = Label(dex_frame, "Cost: {}".format(calculate_training_cost(Stats.DEX, current_dex, range=1)))
	dex_train_cost.pack(side=LEFT)

	end_frame = Frame(do_training_frame)
	end_frame.pack(side=TOP)
	Label(end_frame, text="END").pack(side=LEFT)
	end_current_label = Label(end_frame, text= "Current {}".format(current_end))
	end_current_label.pack(side=LEFT)
	end_train_button = Button(end_frame, text="+", command=train(Stats.END))
	end_train_button.pack(side=LEFT)
	end_train_cost = Label(end_frame, "Cost: {}".format(calculate_training_cost(Stats.END, current_end)))
	end_train_cost.pack(side=LEFT)

	cha_frame = Frame(do_training_frame)
	cha_frame.pack(side=TOP)
	Label(cha_frame, text="CHA").pack(side=LEFT)
	cha_current_label = Label(cha_frame, text= "Current {}".format(current_cha))
	cha_current_label.pack(side=LEFT)
	cha_train_button = Button(cha_frame, text="+", command=train(Stats.CHA))
	cha_train_button.pack(side=LEFT)
	cha_train_cost = Label(cha_frame, "Cost: {}".format(calculate_training_cost(Stats.CHA, current_cha)))
	cha_train_cost.pack(side=LEFT)

	int_frame = Frame(do_training_frame)
	int_frame.pack(side=TOP)
	Label(int_frame, text="INT").pack(side=LEFT)
	int_current_label = Label(int_frame, text= "Current {}".format(current_int))
	int_current_label.pack(side=LEFT)
	int_train_button = Button(int_frame, text="+", command=train(Stats.INT))
	int_train_button.pack(side=LEFT)
	int_train_cost = Label(int_frame, "Cost: {}".format(calculate_training_cost(Stats.INT, current_int)))
	int_train_cost.pack(side=LEFT)

	training_calculator_frame = Frame(training_frame)
	training_calculator_frame.pack(side=LEFT)
	training_calculator_listbox = Listbox(training_calculator_frame, height=10, width=10)
	training_calculator_listbox.pack(side=LEFT)
	current_attributes_frame = Frame(training_calculator_frame)
	current_attributes_frame.pack(side=LEFT)
	Label(current_attributes_frame, "STR: {}".format(current_str)).pack(side=TOP)
	Label(current_attributes_frame, "AGI: {}".format(current_agi)).pack(side=TOP)
	Label(current_attributes_frame, "DEX: {}".format(current_dex)).pack(side=TOP)
	Label(current_attributes_frame, "END: {}".format(current_end)).pack(side=TOP)
	Label(current_attributes_frame, "CHA: {}".format(current_cha)).pack(side=TOP)
	Label(current_attributes_frame, "INT: {}".format(current_int)).pack(side=TOP)
	training_range_frame = Frame(training_calculator_frame)
	Label(training_range_frame, "+").pack(side=LEFT)
	training_range_text = Text(training_range_frame, height=1, width=3)
	training_range_text.pack(side=LEFT)
	calculate_training_button = Button(training_calculator_frame, text="Calculate", command=calculate_ranged_training_cost(Stats.DEX, current_dex, range=1))
	calculate_training_button.pack(side=LEFT)
	calculated_cost_label = Label(training_calculator_frame, "Cost:")
	calculated_cost_label.pack(side=LEFT)


	# arena tab
	arena_frame = Frame(arena_tab)
	arena_frame.pack()


	# auction tab
	auction_frame = Frame(auction_tab)
	auction_frame.pack(side=LEFT)
	auction_status = Label(auction_frame, text="Remaining: {}".format(auction_remaining))
	auction_status.pack()
	mercenary_auction_frame = Frame(auction_tab)
	mercenary_auction_frame.pack(side=LEFT)
	mercenary_auction_status = Label(mercenary_auction_frame, text="Remaining: {}".format(mercenary_auction_remaining))
	wanted_items_frame = Frame(auction_tab)
	wanted_items_frame.pack(side=LEFT)
	wanted_item_add_frame = Frame(wanted_items_frame)
	wanted_item_add_frame.pack(side=TOP)
	wanted_item_text = Text(wanted_item_add_frame, height=1, width=50)
	wanted_item_text.pack(side=LEFT)
	wanted_item_add_button = Button(wanted_item_add_frame, text="Add", command=add_wanted_item)
	wanted_items_listbox = Listbox(wanted_items_frame, height=30, width=60)
	wanted_items_listbox.pack(side=TOP)
	wanted_items_listbox.bind('<<ListboxSelect>>', set_selected_index)
	wanted_item_delete_button = Button(wanted_items_frame, text="Delete", command=delete_wanted_item)

	auction_settings_frame = Frame(auction_tab)
	auction_settings_frame.pack(side=LEFT)

	auction_refresh_rate_frame = Frame(auction_settings_frame)
	refresh_loop = Checkbox(auction_refresh_rate_frame)
	refresh_loop.pack(side=LEFT)
	Label(auction_refresh_rate_frame, text="Refresh per ").pack(side=LEFT)
	auction_refresh_rate_text = Text(auction_settings_frame, height=1, width=2)
	auction_refresh_rate_text.pack(side=LEFT)
	auction_refresh_rate_listbox = Listbox(auction_settings_frame)
	auction_refresh_rate_listbox.pack(side=LEFT)
	populate_auction_refresh_rate_listbox(auction_refresh_rate_listbox)
	auction_refresh_rate_listbox.bind('<<ListboxSelect>>', set_selected_auction_chk_frequency)

	auction_manual_refresh_button = Button(auction_settings_frame, text="Refresh Auctions", command=get_auction_time)
	auction_manual_refresh_button.pack(side=BOTTOM)


	# suggestion tab
	suggestion_frame = Frame(suggestion_tab)
	suggestion_frame.pack()


	

	tab_control.add(character_tab, text='character')
	tab_control.add(mercenaries_tab, text='mercenaries')
	tab_control.add(training_tab, text='training')
	tab_control.add(arena_tab, text='arena')
	tab_control.add(auction_tab, text='auction')
	tab_control.add(suggestion_tab, text='suggestions')
	tab_control.pack(expand=1, fill="both")  # Pack to make visible
	root.mainloop()