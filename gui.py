import Tkinter,tkFileDialog
import Tkinter as tk
from Tkinter import *
from tkinter import ttk
import tkMessageBox
from utilities.enums.xpath_enums import Character
from utilities.enums.enums import Stats
from utilities.funcs_character import set_stat_labels, set_hp_labels, set_character_item_labels, set_point_labels
from utilities.funcs_training import set_training_stat_frames, calculate_ranged_training_cost

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


def set_selected_auction_chk_frequency(evt):
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


def activate():
	pass


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
	character_stats_frame = Frame(character_frame)
	character_stats_frame.pack(side=LEFT)
	stat_labels = []
	for i in range(6):
		stat_labels.append(Label(character_stats_frame))
		stat_labels[i].pack(side=TOP)
	set_stat_labels(stat_labels)
	
	character_hp_frame = Frame(character_frame)
	character_hp_frame.pack(side=LEFT)
	hp_labels = []
	for i in range(6):
		hp_labels.append(Label(character_hp_frame))
		hp_labels[i].pack(side=TOP)
	set_hp_labels(hp_labels)

	character_items_frame = Frame(character_frame)
	character_frame.pack(side=LEFT)
	character_item_labels = []
	for i in range(9):
		character_item_labels.append(Label(character_items_frame))
		character_item_labels[i].pack(side=TOP)
	set_character_item_labels(character_item_labels)

	character_points_frame = Frame(character_frame)
	character_points_frame.pack(side=LEFT)
	character_points_labels = []
	for i in range(4):
		character_points_labels.append(Label(character_points_frame))
		character_points_labels[i].pack(side=TOP)
	set_point_labels(character_points_labels)



	# mercenaries tab
	mercenaries_frame = Frame(mercenaries_tab)
	mercenaries_frame.pack()


	# training tab
	training_frame = Frame(training_tab)
	training_frame.pack()
	do_training_frame = Frame(training_frame)
	do_training_frame.pack(side=LEFT)

	training_stats_frame = Frame(training_frame)
	training_stats_frame.pack(side=LEFT)
	training_stat_labels = []
	for i in range(6):
		training_stat_labels.append(Label(training_frame))
		training_stat_labels[i].pack(side=TOP)
	set_stat_labels(training_stat_labels)


	training_stat_frames = []
	labels = []
	buttons = []
	cost_labels = []
	for i in range(6):
		training_stat_frames.append(Frame(do_training_frame))
		training_stat_frames[i].pack(side=TOP)
		labels.append(Label(training_stat_frames[i]))
		labels[i].pack(side=LEFT)
		buttons.append(Button(training_stat_frames[i], text="+", command=lambda:train(i)))
		buttons[i].pack(side=LEFT)
		cost_labels.append(Label(training_stat_frames[i]))
		cost_labels[i].pack(side=LEFT)
	set_training_stat_frames(labels, cost_labels)


	training_calculator_frame = Frame(training_frame)
	training_calculator_frame.pack(side=LEFT)
	training_calculator_listbox = Listbox(training_calculator_frame, height=10, width=10)
	training_calculator_listbox.pack(side=LEFT)
	current_attributes_frame = Frame(training_calculator_frame)
	current_attributes_frame.pack(side=LEFT)
	Label(current_attributes_frame, text="STR: ").pack(side=TOP)
	Label(current_attributes_frame, text="AGI: ").pack(side=TOP)
	Label(current_attributes_frame, text="DEX: ").pack(side=TOP)
	Label(current_attributes_frame, text="END: ").pack(side=TOP)
	Label(current_attributes_frame, text="CHA: ").pack(side=TOP)
	Label(current_attributes_frame, text="INT: ").pack(side=TOP)
	training_range_frame = Frame(training_calculator_frame)
	Label(training_range_frame, text="+").pack(side=LEFT)
	training_range_text = Text(training_range_frame, height=1, width=3)
	training_range_text.pack(side=LEFT)
	calculate_training_button = Button(training_calculator_frame, text="Calculate", command=lambda:calculate_ranged_training_cost(Stats.DEX, current=0, range=1)) # mocked
	calculate_training_button.pack(side=LEFT)
	calculated_cost_label = Label(training_calculator_frame, text="Cost:")
	calculated_cost_label.pack(side=LEFT)


	# arena tab
	arena_frame = Frame(arena_tab)
	arena_frame.pack()


	# auction tab
	auction_frame = Frame(auction_tab)
	auction_frame.pack(side=LEFT)
	auction_status = Label(auction_frame, text="Auction Remaining: ")
	auction_status.pack(side=TOP)
	m_auction_status = Label(m_auction_frame, text="Mercenary Auction Remaining: ")
	m_auction_status.pack(side=TOP)
	mercenary_auction_frame = Frame(auction_tab)
	mercenary_auction_frame.pack(side=LEFT)
	mercenary_auction_status = Label(mercenary_auction_frame, text="Remaining: ")
	wanted_items_frame = Frame(auction_tab)
	wanted_items_frame.pack(side=LEFT)
	wanted_item_add_frame = Frame(wanted_items_frame)
	wanted_item_add_frame.pack(side=TOP)
	wanted_item_text = Text(wanted_item_add_frame, height=1, width=15)
	wanted_item_text.pack(side=LEFT)
	wanted_item_add_button = Button(wanted_item_add_frame, text="Add", command=add_wanted_item)
	wanted_items_listbox = Listbox(wanted_items_frame, height=20, width=15)
	wanted_items_listbox.pack(side=TOP)
	wanted_items_listbox.bind('<<ListboxSelect>>', set_selected_index)
	wanted_item_delete_button = Button(wanted_items_frame, text="Delete", command=delete_wanted_item)

	auction_settings_frame = Frame(auction_tab)
	auction_settings_frame.pack(side=LEFT)

	auction_refresh_rate_frame = Frame(auction_settings_frame)
	auction_refresh_rate_frame.pack(side=LEFT)
	# refresh_loop = Checkbox(auction_refresh_rate_frame)
	# refresh_loop.pack(side=LEFT)
	Label(auction_refresh_rate_frame, text="Refresh per ").pack(side=LEFT)
	auction_refresh_rate_text = Text(auction_settings_frame, height=1, width=2)
	auction_refresh_rate_text.pack(side=LEFT)
	auction_refresh_rate_listbox = Listbox(auction_settings_frame)
	auction_refresh_rate_listbox.pack(side=LEFT)
	populate_auction_refresh_rate_listbox(auction_refresh_rate_listbox)
	auction_refresh_rate_listbox.bind('<<ListboxSelect>>', set_selected_auction_chk_frequency)

	auction_manual_refresh_button = Button(auction_settings_frame, text="Refresh Auctions", command=get_auction_time)
	auction_manual_refresh_button.pack(side=BOTTOM)
	auction_activate_automatic_chk_button = Button(auction_settings_frame, text="Set settings, activate check", command=activate)
	auction_activate_automatic_chk_button.pack(side=BOTTOM)


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